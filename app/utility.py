# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Utility functions used by the Wait Wait Stats Page"""
import json

from datetime import datetime
from dateutil import parser
from flask import current_app
import pytz


def current_year(time_zone: pytz.timezone = pytz.timezone("UTC")):
    """Return the current year"""
    now = datetime.now(time_zone)
    return now.strftime("%Y")


def date_string_to_date(**kwargs):
    """Used to convert an ISO-style date string into a datetime object"""
    if "date_string" in kwargs and kwargs["date_string"]:
        try:
            date_object = parser.parse(kwargs["date_string"])
            return date_object

        except ValueError:
            return None

    return None


def generate_date_time_stamp(time_zone: pytz.timezone = pytz.timezone("UTC")):
    """Generate a current date/timestamp string"""
    now = datetime.now(time_zone)
    return now.strftime("%Y-%m-%d %H:%M:%S %Z")


def pretty_jsonify(data):
    """Returns a prettier JSON output for an object than Flask's default
    tojson filter"""
    return json.dumps(data, indent=2)


def redirect_url(url: str, status_code: int = 302):
    """Returns a redirect response for a given URL"""

    # Use a custom response class to force set response headers
    # and handle the redirect to prevent browsers from caching redirect
    response = current_app.response_class(response=None,
                                          status=status_code,
                                          mimetype="text/plain")

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = 0
    response.headers["Location"] = url
    return response


def time_zone_parser(time_zone: str) -> pytz.timezone:
    """Parses a time zone name into a pytz.timezone object.

    Returns pytz.timezone object and string if time_zone is valid.
    Otherwise, returns UTC if time zone is not a valid tz value."""

    try:
        time_zone_object = pytz.timezone(time_zone)
        time_zone_string = time_zone_object.zone
    except (pytz.UnknownTimeZoneError, AttributeError, ValueError):
        time_zone_object = pytz.timezone("UTC")
        time_zone_string = time_zone_object.zone

    return time_zone_object, time_zone_string
