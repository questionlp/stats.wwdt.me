# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Locations Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, redirect, render_template, url_for
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
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    slugs = location.retrieve_all_slugs()
    _slug = slugify(location_slug)

    if _slug not in slugs:
        database_connection.close()
        _location_redirects: dict[str, str] = current_app.config["url_redirects"][
            "locations"
        ]["slugs"]
        if _location_redirects and _slug in _location_redirects:
            if _location_redirects[_slug]:
                return redirect(
                    url_for(
                        "locations.details", location_slug=_location_redirects[_slug]
                    ),
                    code=301,
                )

            return redirect_url(url_for("locations.index"))

        return redirect_url(url_for("locations.index"))

    _details = location.retrieve_details_by_slug(location_slug=_slug)
    database_connection.close()

    # Redirect back to /locations for certain placeholder locations
    _placeholder_ids: list[int] = current_app.config["location_placeholders"]
    if "id" in _details and _details["id"] in _placeholder_ids:
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
    database_connection.close()

    return redirect_url(url_for("locations.details", location_slug=_slug))
