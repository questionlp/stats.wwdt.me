# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Locations Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, render_template, url_for
from slugify import slugify
from wwdtm.location import Location

from app.locations.utility import (
    decimal_to_degrees,
    format_latitude,
    format_location_name,
    format_longitude,
)
from app.utility import redirect_url

blueprint = Blueprint("locations", __name__, template_folder="templates")


@blueprint.route("/")
def index() -> Response | str:
    """View: Locations Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    location_list = location.retrieve_all(
        sort_by_venue=current_app.config["app_settings"]["sort_by_venue"]
    )
    database_connection.close()

    if not location_list:
        return redirect_url(url_for("main.index"))

    return render_template(
        "locations/index.html",
        locations=location_list,
        format_location_name=format_location_name,
    )


@blueprint.route("/<string:location_slug>")
def details(location_slug: str) -> Response | str:
    """View: Location Details."""
    slug = slugify(location_slug)
    if location_slug and location_slug != slug:
        return redirect_url(url_for("locations.details", location_slug=slug))

    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    _details = location.retrieve_details_by_slug(slug)
    database_connection.close()

    if not _details:
        return redirect_url(url_for("locations.index"))

    # Redirect back to /locations for certain placeholder locations
    if "id" in _details and (_details["id"] == 3 or _details["id"] == 38):
        return redirect_url(url_for("locations.index"))

    # Template expects a list of location(s)
    locations = []
    locations.append(_details)
    return render_template(
        "locations/single.html",
        locations=locations,
        location_details=_details,
        decimal_to_degrees=decimal_to_degrees,
        format_latitude=format_latitude,
        format_longitude=format_longitude,
        format_location_name=format_location_name,
    )


@blueprint.route("/all")
def _all() -> Response | str:
    """View: Location Details for All Locations."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    locations = location.retrieve_all_details(
        sort_by_venue=current_app.config["app_settings"]["sort_by_venue"]
    )
    database_connection.close()

    if not locations:
        return redirect_url(url_for("locations.index"))

    return render_template(
        "locations/all.html",
        locations=locations,
        decimal_to_degrees=decimal_to_degrees,
        format_latitude=format_latitude,
        format_longitude=format_longitude,
        format_location_name=format_location_name,
        display_location_map=False,
    )


@blueprint.route("/random")
def random() -> Response:
    """View: Random Location Redirect."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    _slug = location.retrieve_random_slug()
    return redirect_url(url_for("locations.details", location_slug=_slug))
