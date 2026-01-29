# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Main Routes for Wait Wait Stats Page."""

import json
from datetime import date
from pathlib import Path

import mysql.connector
from flask import Blueprint, Response, current_app, render_template, request, send_file
from wwdtm.guest import Guest
from wwdtm.host import Host
from wwdtm.location import Location
from wwdtm.panelist import Panelist
from wwdtm.scorekeeper import Scorekeeper
from wwdtm.show import Show

from app.config import DEFAULT_RECENT_DAYS_AHEAD, DEFAULT_RECENT_DAYS_BACK
from app.locations.utility import (
    decimal_to_degrees,
    format_latitude,
    format_location_name,
    format_longitude,
)

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


@blueprint.route("/understanding-data")
def understanding_data() -> Response:
    """View: Understanding Wait Wait Stats Page Data."""
    _examples: date = current_app.config["app_settings"]["examples"]
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    host = Host(database_connection=database_connection)
    location = Location(database_connection=database_connection)
    panelist = Panelist(database_connection=database_connection)
    scorekeeper = Scorekeeper(database_connection=database_connection)
    show = Show(database_connection=database_connection)

    _guest = guest.retrieve_details_by_slug(guest_slug=_examples["guest"])
    _host = host.retrieve_details_by_slug(host_slug=_examples["host"])
    _location = location.retrieve_details_by_slug(location_slug=_examples["location"])
    _panelist = panelist.retrieve_details_by_slug(panelist_slug=_examples["panelist"])
    _scorekeeper = scorekeeper.retrieve_details_by_slug(
        scorekeeper_slug=_examples["scorekeeper"]
    )
    _show = show.retrieve_details_by_date(
        year=_examples["show"].year,
        month=_examples["show"].month,
        day=_examples["show"].day,
        include_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"],
    )

    if all((_guest, _host, _location, _panelist, _show)):
        return render_template(
            "pages/understanding-data.html",
            valid_data=True,
            guests=[_guest],
            guest_name=_guest["name"],
            hosts=[_host],
            host_name=_host["name"],
            locations=[_location],
            location_details=_location,
            panelists=[_panelist],
            panelist_name=_panelist["name"],
            scorekeepers=[_scorekeeper],
            scorekeeper_name=_scorekeeper["name"],
            show_date=_examples["show"],
            shows=[_show],
            decimal_to_degrees=decimal_to_degrees,
            format_latitude=format_latitude,
            format_location_name=format_location_name,
            format_longitude=format_longitude,
            display_location_map=False,
            exclude_panelist_appearances=True,
            exclude_description=True,
            exclude_notes=True,
            exclude_recordings=True,
        )
    else:
        return render_template("pages/understanding-data.html")


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
    return render_template("pages/site-history.html")


@blueprint.route("/teapot", methods=["GET", "POST"])
def teapot() -> Response:
    """View: Teapot."""
    return render_template("pages/teapot.html"), 418


@blueprint.route("/", methods=["BREW"])
@blueprint.route("/teapot", methods=["BREW"])
def teapot_brew() -> Response:
    """View Teapot Brew Method."""
    _content_type = request.headers.get("Content-Type")
    if _content_type == "application/coffee-pot-command":
        _response_data = {"data": "I'm a teapot."}
        return (
            Response(json.dumps(_response_data), content_type="application/json"),
            418,
        )

    _response_data = {"data": "Move along home"}
    return Response(json.dumps(_response_data), content_type="application/json"), 404
