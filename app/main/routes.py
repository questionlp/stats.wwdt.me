# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Main Routes for Wait Wait Stats Page."""
from pathlib import Path

import mysql.connector
from flask import Blueprint, Response, current_app, render_template, send_file
from wwdtm.show import Show

from app.config import DEFAULT_RECENT_DAYS_AHEAD, DEFAULT_RECENT_DAYS_BACK
from app.locations.utility import format_location_name

blueprint = Blueprint("main", __name__)


@blueprint.route("/")
def index() -> str:
    """View: Site Index Page."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    _settings = current_app.config["app_settings"]

    try:
        if "recent_days_ahead" in _settings:
            days_ahead = int(_settings["recent_days_ahead"])
            days_back = int(_settings["recent_days_back"])
        else:
            days_ahead = DEFAULT_RECENT_DAYS_AHEAD
            days_back = DEFAULT_RECENT_DAYS_BACK
    except TypeError:
        days_ahead = DEFAULT_RECENT_DAYS_AHEAD
        days_back = DEFAULT_RECENT_DAYS_BACK
    except ValueError:
        days_ahead = DEFAULT_RECENT_DAYS_AHEAD
        days_back = DEFAULT_RECENT_DAYS_BACK

    try:
        show = Show(database_connection=database_connection)
        recent = show.retrieve_recent_details(
            include_days_ahead=days_ahead,
            include_days_back=days_back,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )
        recent.reverse()
    except AttributeError:
        recent = show.retrieve_recent_details()
        recent.reverse()
    finally:
        database_connection.close()

    return render_template(
        "pages/index.html", shows=recent, format_location_name=format_location_name
    )


@blueprint.route("/robots.txt")
def robots_txt() -> Response:
    """View: robots.txt File."""
    robots_txt_path = Path(current_app.root_path) / "static" / "robots.txt"
    if not robots_txt_path.exists():
        response = render_template("robots.txt")
        return Response(response, mimetype="text/plain")

    return send_file(robots_txt_path, mimetype="text/plain")


@blueprint.route("/about")
def about() -> str:
    """View: About Page."""
    return render_template("pages/about.html")


@blueprint.route("/site-history")
def site_history() -> str:
    """View: Site History Page."""
    return render_template("pages/site_history.html")
