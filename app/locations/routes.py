# Copyright (c) 2018-2024 Linh Pham
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


def random_location_slug() -> str | None:
    """Return a random location slug from ww_locations table."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = database_connection.cursor(dictionary=False)
    query = (
        "SELECT l.locationslug FROM ww_locations l "
        "WHERE l.locationslug <> 'tbd' "
        "ORDER BY RAND() "
        "LIMIT 1;"
    )
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    database_connection.close()

    if not result:
        return None

    return str(result[0])


@blueprint.route("/")
def index() -> Response | str:
    """View: Locations Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    location_list = location.retrieve_all(
        current_app.config["app_settings"]["sort_by_venue"]
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
    details = location.retrieve_details_by_slug(slug)
    database_connection.close()

    if not details:
        return redirect_url(url_for("locations.index"))

    # Redirect back to /locations for certain placeholder locations
    if "id" in details and (details["id"] == 3 or details["id"] == 38):
        return redirect_url(url_for("locations.index"))

    # Template expects a list of location(s)
    locations = []
    locations.append(details)
    return render_template(
        "locations/single.html",
        locations=locations,
        location_details=details,
        decimal_to_degrees=decimal_to_degrees,
        format_latitude=format_latitude,
        format_longitude=format_longitude,
        format_location_name=format_location_name,
    )


@blueprint.route("/all")
def all() -> Response | str:
    """View: Location Details for All Locations."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    locations = location.retrieve_all_details()
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
    _slug = random_location_slug()
    return redirect_url(url_for("locations.details", location_slug=_slug))
