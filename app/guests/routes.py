# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Guests Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, redirect, render_template, url_for
from slugify import slugify
from wwdtm.guest import Guest

from app.utility import redirect_url

blueprint = Blueprint("guests", __name__, template_folder="templates")


@blueprint.route("/")
def index() -> Response | str:
    """View: Guests Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    guests = guest.retrieve_all()
    database_connection.close()

    if not guests:
        return redirect(url_for("main.index"))

    return render_template("guests/index.html", guests=guests)


@blueprint.route("/<string:guest_slug>")
def details(guest_slug: str) -> Response | str:
    """View: Guest Details."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    slugs = guest.retrieve_all_slugs()
    _slug = slugify(guest_slug)

    if _slug not in slugs:
        return redirect(url_for("guests.index"))

    if _slug in slugs and _slug != guest_slug:
        return redirect(url_for("guests.details", guest_slug=_slug))

    _details = guest.retrieve_details_by_slug(guest_slug)
    database_connection.close()

    if not _details:
        return redirect(url_for("guests.index"))

    guests = []
    guests.append(_details)

    return render_template(
        "guests/single.html", guest_name=_details["name"], guests=guests
    )


@blueprint.route("/all")
def _all() -> Response | str:
    """View: Guest Details for All Guests."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    guests = guest.retrieve_all_details()
    database_connection.close()

    if not guests:
        return redirect(url_for("guests.index"))

    return render_template("guests/all.html", guests=guests)


@blueprint.route("/random")
def random() -> Response:
    """View: Random Guest Redirect."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    _slug = guest.retrieve_random_slug()
    database_connection.close()

    return redirect_url(url_for("guests.details", guest_slug=_slug))
