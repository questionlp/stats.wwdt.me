# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Locations Routes for Wait Wait Stats Page"""
from flask import Blueprint, current_app, render_template, url_for
import mysql.connector
from slugify import slugify
from wwdtm.location import Location

from app.locations.utility import format_location_name
from app.utility import redirect_url

blueprint = Blueprint("locations", __name__, template_folder="templates")


def random_location_slug() -> str:
    """Return a random location slug from ww_locations table"""
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

    return result[0]


@blueprint.route("/")
def index():
    """View: Locations Index"""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    location_list = location.retrieve_all()
    database_connection.close()

    if not location_list:
        return redirect_url(url_for("main.index"))

    return render_template(
        "locations/index.html",
        locations=location_list,
        format_location_name=format_location_name,
    )


@blueprint.route("/<string:location_slug>")
def details(location_slug: str):
    """View: Location Details"""
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
    location_name = format_location_name(details)
    return render_template(
        "locations/single.html",
        locations=locations,
        location_name=location_name,
        format_location_name=format_location_name,
    )


@blueprint.route("/all")
def all():
    """View: Location Details for All Locations"""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    locations = location.retrieve_all_details()
    database_connection.close()

    if not locations:
        return redirect_url(url_for("locations.index"))

    return render_template(
        "locations/all.html",
        locations=locations,
        format_location_name=format_location_name,
    )


@blueprint.route("/random")
def random():
    """View: Random Location Redirect"""
    _slug = random_location_slug()
    return redirect_url(url_for("locations.details", location_slug=_slug))
