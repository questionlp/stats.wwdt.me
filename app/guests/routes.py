# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Guests Routes for Wait Wait Stats Page"""
from flask import Blueprint, current_app, redirect, render_template, url_for
import mysql.connector
from wwdtm.guest import Guest

from app.utility import redirect_url

blueprint = Blueprint("guests", __name__)


def random_guest_slug() -> str:
    """Return a random guest slug from ww_guests table"""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = database_connection.cursor(dictionary=False)
    query = (
        "SELECT g.guestslug FROM ww_guests g "
        "WHERE g.guestslug <> 'none' "
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
    """View: Guests Index"""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    guests = guest.retrieve_all()
    database_connection.close()

    if not guests:
        return redirect(url_for("main.index"))

    return render_template("guests/index.html", guests=guests)


@blueprint.route("/<string:guest_slug>")
def details(guest_slug: str):
    """View: Guest Details"""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    details = guest.retrieve_details_by_slug(guest_slug)
    database_connection.close()

    if not details:
        return redirect(url_for("guests.index"))

    guests = []
    guests.append(details)
    return render_template(
        "guests/single.html", guest_name=details["name"], guests=guests
    )


@blueprint.route("/all")
def all():
    """View: Guest Details for All Guests"""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    guest = Guest(database_connection=database_connection)
    guests = guest.retrieve_all_details()
    database_connection.close()

    if not guests:
        return redirect(url_for("guests.index"))

    return render_template("guests/all.html", guests=guests)


@blueprint.route("/random")
def random():
    """View: Random Guest Redirect"""
    _slug = random_guest_slug()
    return redirect_url(url_for("guests.details", guest_slug=_slug))
