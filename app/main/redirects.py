# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Main Redirect Routes for Wait Wait Stats Page."""

from datetime import datetime

import mysql.connector
from flask import Blueprint, Response, current_app, url_for
from wwdtm.show import ShowUtility

from app.utility import date_string_to_date, redirect_url

blueprint = Blueprint("main_redirects", __name__)


@blueprint.route("/favicon.ico")
def favicon() -> Response:
    """Redirect: /favicon.ico to /static/favicon.ico."""
    return redirect_url(url_for("static", filename="favicon.ico"))


@blueprint.route("/guest")
@blueprint.route("/guest/")
@blueprint.route("/guests")
def guests() -> Response:
    """Redirect: /guest and /guests to /guests/."""
    return redirect_url(url_for("guests.index"))


@blueprint.route("/guest/<string:guest_slug>")
def guests_details(guest_slug: str) -> Response:
    """Redirect: /guest/<guest_slug> to /guests/<guest_slug>."""
    return redirect_url(
        url_for("guests.details", guest_slug=guest_slug), status_code=301
    )


@blueprint.route("/help")
def help_page() -> Response:
    """Redirect: /help to /."""
    return redirect_url(url_for("main.index"))


@blueprint.route("/host")
@blueprint.route("/host/")
@blueprint.route("/hosts")
def hosts() -> Response:
    """Redirect: /host and /hosts to /hosts/."""
    return redirect_url(url_for("hosts.index"))


@blueprint.route("/host/<string:host_slug>")
def hosts_details(host_slug: str) -> Response:
    """Redirect: /host/<host_slug> to /hosts/<host_slug>."""
    return redirect_url(url_for("hosts.details", host_slug=host_slug), status_code=301)


@blueprint.route("/info")
def info_page() -> Response:
    """Redirect: /info to /understanding-data."""
    return redirect_url(url_for("main.understanding_data"))


@blueprint.route("/location")
@blueprint.route("/location/")
@blueprint.route("/locations")
def locations() -> Response:
    """Redirect: /location and /locations to /locations/."""
    return redirect_url(url_for("locations.index"))


@blueprint.route("/location/<string:location_slug>")
def locations_details(location_slug: str) -> Response:
    """Redirect: /location/<location_slug> to /locations/<location_slug>."""
    return redirect_url(
        url_for("locations.details", location_slug=location_slug), status_code=301
    )


@blueprint.route("/panelist")
@blueprint.route("/panelist/")
@blueprint.route("/panelists")
def panelists() -> Response:
    """Redirect: /panelist and /panelists to /panelists/."""
    return redirect_url(url_for("panelists.index"))


@blueprint.route("/panelist/<string:panelist_slug>")
def panelists_details(panelist_slug: str) -> Response:
    """Redirect: /panelist/<panelist_slug> to /panelists/<panelist_slug>."""
    return redirect_url(
        url_for("panelists.details", panelist_slug=panelist_slug), status_code=301
    )


@blueprint.route("/scorekeeper")
@blueprint.route("/scorekeeper/")
@blueprint.route("/scorekeepers")
def scorekeepers() -> Response:
    """Redirect: /scorekeeper and /scorekeepers to /scorekeepers/."""
    return redirect_url(url_for("scorekeepers.index"))


@blueprint.route("/scorekeeper/<string:scorekeeper_slug>")
def scorekeepers_details(scorekeeper_slug: str) -> Response:
    """Redirect: /scorekeeper/<scorekeeper_slug> to /scorekeepers/<scorekeeper_slug>."""
    return redirect_url(
        url_for("scorekeepers.details", scorekeeper_slug=scorekeeper_slug),
        status_code=301,
    )


@blueprint.route("/search")
def search() -> Response:
    """Redirect: /search to /."""
    return redirect_url(url_for("main.index"))


@blueprint.route("/show")
@blueprint.route("/show/")
@blueprint.route("/shows")
def shows() -> Response:
    """Redirect: /show and /shows to /shows/."""
    return redirect_url(url_for("shows.index"))


@blueprint.route("/show/<string:iso_date_string>")
def shows_date_string(iso_date_string: str) -> Response:
    """Redirect: /show/<iso_date_string_year> to /shows/<iso_date_string>."""
    return redirect_url(
        url_for("shows.date_string", iso_date_string=iso_date_string), status_code=301
    )


@blueprint.route("/show/<int:show_year>")
def shows_year(show_year: int) -> Response:
    """Redirect: /show/<show_year> to /shows/<show_year>."""
    return redirect_url(url_for("shows.year", show_year=show_year), status_code=301)


@blueprint.route("/show/<int:show_year>/<int:show_month>")
def shows_year_month(show_year: int, show_month: int) -> Response:
    """Redirect: /show/<show_year>/<show_month> to /shows/<show_year>/<show_month>."""
    return redirect_url(
        url_for("shows.year_month", show_year=show_year, show_month=show_month),
        status_code=301,
    )


@blueprint.route("/show/<int:show_year>/<int:show_month>/<int:show_day>")
def shows_year_month_day(show_year: int, show_month: int, show_day: int) -> Response:
    """Redirect: /show/<show_year>/<show_month>/<show_day> to /shows/<show_year>/<show_month>/<show_day>."""
    return redirect_url(
        url_for(
            "shows.year_month_day",
            show_year=show_year,
            show_month=show_month,
            show_day=show_day,
        ),
        status_code=301,
    )


@blueprint.route("/shows/best-of-repeats")
def shows_best_of_repeats() -> Response:
    """Redirect: /shows/best-of-repeats to /shows/repeat-best-ofs."""
    return redirect_url(url_for("shows.repeat_best_ofs"))


@blueprint.route("/s/<string:show_date>")
def npr_show_redirect(show_date: str) -> Response:
    """Redirects users to the appropriate show page on NPR.org."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show_utility = ShowUtility(database_connection=database_connection)
    show_date_object = date_string_to_date(date_string=show_date)

    if not show_date_object:
        database_connection.close()
        return redirect_url(url_for("main.index"))

    if show_utility.date_exists(
        year=show_date_object.year,
        month=show_date_object.month,
        day=show_date_object.day,
    ):
        current_url_prefix = (
            "https://www.npr.org/programs/wait-wait-dont-tell-me/archive?date="
        )
        legacy_url_prefix = "https://legacy.npr.org/programs/waitwait/archrndwn"
        legacy_url_suffix = ".waitwait.html"
        if show_date_object >= datetime(year=2006, month=1, day=7):
            show_date_string = show_date_object.strftime("%m-%d-%Y")
            url = f"{current_url_prefix}{show_date_string}"
        else:
            show_date_string = show_date_object.strftime("%y%m%d")
            year = show_date_object.strftime("%Y")
            month = show_date_object.strftime("%b").lower()
            url = f"{legacy_url_prefix}/{year}/{month}/{show_date_string}{legacy_url_suffix}"

        database_connection.close()

        return redirect_url(url)

    database_connection.close()
    return redirect_url(url_for("main.index"))


@blueprint.route("/stats")
@blueprint.route("/stats/")
def stats() -> Response:
    """Redirect: /stats and /stats/ to /."""
    return redirect_url(url_for("main.index"), status_code=301)
