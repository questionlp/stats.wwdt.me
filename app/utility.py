# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Utility functions used by the Wait Wait Stats Page."""

import json
import re
from datetime import datetime
from decimal import Decimal

import markdown
import pytz
from flask import current_app


def current_year(time_zone: str = "UTC") -> str:
    """Return the current year."""
    _time_zone = pytz.timezone(time_zone)
    now = datetime.now(_time_zone)
    return now.strftime("%Y")


def date_string_to_date(**kwargs) -> datetime | None:
    """Used to convert an ISO-style date string into a datetime object."""
    if "date_string" in kwargs and kwargs["date_string"]:
        try:
            date_object = datetime.strptime(kwargs["date_string"], "%Y-%m-%d")
        except ValueError:
            return None

        return date_object

    return None


def join_decimals(decimals: list[Decimal], delimiter: str = ", ") -> str:
    """Return a joined string of formatted decimals."""
    normalized: list[str] = [str(Decimal.normalize(d)) for d in decimals]
    return delimiter.join(normalized)


def generate_date_time_stamp(time_zone: str = "UTC") -> str:
    """Generate a current date/timestamp string."""
    _time_zone = pytz.timezone(time_zone)
    now = datetime.now(_time_zone)
    return now.strftime("%Y-%m-%d %H:%M:%S %Z")


def md_to_html(markdown_text: str):
    """Converts Markdown text into HTML."""
    html_text = markdown.markdown(markdown_text, output_format="html")
    site_url = current_app.jinja_env.globals["site_url"]

    if html_text and site_url:
        pattern = r'(<a\s+href="((?:(?!' + site_url + r').)*?)")>([^<]+)</a>'
        replacement = r'\1 target="_blank">\3<i class="bi bi-box-arrow-up-right px-1" aria-hidden="true"></i></a>'
        updated_html = re.sub(pattern, replacement, html_text, flags=re.DOTALL)

    return updated_html


def pretty_jsonify(data):
    """Returns a prettified JSON output of the data."""
    return json.dumps(data, indent=2)


def redirect_url(url: str, status_code: int = 302):
    """Returns a redirect response for a given URL."""
    # Use a custom response class to force set response headers
    # and handle the redirect to prevent browsers from caching redirect
    response = current_app.response_class(
        response=None, status=status_code, mimetype="text/plain"
    )

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = 0
    response.headers["Location"] = url
    return response


def time_zone_parser(time_zone: str) -> tuple:
    """Parses a time zone name into a pytz.timezone object.

    Returns pytz.timezone object and string if time_zone is valid.
    Otherwise, returns UTC if time zone is not a valid tz value.
    """
    try:
        time_zone_object = pytz.timezone(time_zone)
        time_zone_string = time_zone_object.zone
    except (pytz.UnknownTimeZoneError, AttributeError, ValueError):
        time_zone_object = pytz.timezone("UTC")
        time_zone_string = time_zone_object.zone

    return time_zone_object, time_zone_string
