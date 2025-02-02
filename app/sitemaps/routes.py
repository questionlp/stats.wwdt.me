# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Sitemap Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, render_template
from wwdtm.guest import Guest
from wwdtm.host import Host
from wwdtm.location import Location
from wwdtm.panelist import Panelist
from wwdtm.scorekeeper import Scorekeeper
from wwdtm.show import Show

blueprint = Blueprint("sitemaps", __name__)


@blueprint.route("/sitemap.xml")
def primary() -> Response | None:
    """View: Primary Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    years = show.retrieve_years()
    database_connection.close()

    if not years:
        return None

    sitemap = render_template("sitemaps/sitemap.xml", show_years=years)

    return Response(sitemap, mimetype="text/xml")


@blueprint.route("/sitemap-guests.xml")
def guests() -> Response | None:
    """View: Guests Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    _guests = guest.retrieve_all()
    database_connection.close()

    if not guests:
        return None

    sitemap = render_template("sitemaps/guests.xml", guests=_guests)

    return Response(sitemap, mimetype="text/xml")


@blueprint.route("/sitemap-hosts.xml")
def hosts() -> Response | None:
    """View: Hosts Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=database_connection)
    _hosts = host.retrieve_all()
    database_connection.close()

    if not hosts:
        return None

    sitemap = render_template("sitemaps/hosts.xml", hosts=_hosts)

    return Response(sitemap, mimetype="text/xml")


@blueprint.route("/sitemap-locations.xml")
def locations() -> Response | None:
    """View: Locations Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    location = Location(database_connection=database_connection)
    _locations = location.retrieve_all(sort_by_venue=True)
    database_connection.close()

    if not locations:
        return None

    sitemap = render_template("sitemaps/locations.xml", locations=_locations)

    return Response(sitemap, mimetype="text/xml")


@blueprint.route("/sitemap-panelists.xml")
def panelists() -> Response | None:
    """View: Panelists Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=database_connection)
    _panelists = panelist.retrieve_all()

    if not panelists:
        return None

    sitemap = render_template("sitemaps/panelists.xml", panelists=_panelists)

    return Response(sitemap, mimetype="text/xml")


@blueprint.route("/sitemap-scorekeepers.xml")
def scorekeepers() -> Response | None:
    """View: Scorekeepers Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    scorekeeper = Scorekeeper(database_connection=database_connection)
    _scorekeepers = scorekeeper.retrieve_all()
    database_connection.close()

    if not scorekeepers:
        return None

    sitemap = render_template("sitemaps/scorekeepers.xml", scorekeepers=_scorekeepers)

    return Response(sitemap, mimetype="text/xml")


@blueprint.route("/sitemap-shows.xml")
def shows() -> Response | None:
    """View: Shows Sitemap XML."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    dates = show.retrieve_all_dates_tuple()
    years_months = show.retrieve_all_shows_years_months_tuple()
    database_connection.close()

    if not dates or not years_months:
        return None

    sitemap = render_template(
        "sitemaps/shows.xml", show_dates=dates, show_years_months=years_months
    )

    return Response(sitemap, mimetype="text/xml")
