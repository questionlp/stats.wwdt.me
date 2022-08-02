# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Main Redirect Routes for Wait Wait Stats Page"""
from datetime import datetime
from flask import Blueprint, current_app, url_for
import mysql.connector
from wwdtm.show import ShowUtility

from app.utility import date_string_to_date, redirect_url

blueprint = Blueprint("main_redirects", __name__)


@blueprint.route("/favicon.ico")
def favicon():
    """Redirect: /favicon.ico to /static/favicon.ico"""
    return redirect_url(url_for("static", filename="favicon.ico"))


@blueprint.route("/guest")
@blueprint.route("/guest/")
@blueprint.route("/guests")
def guests():
    """Redirect: /guest and /guests to /guests/"""
    return redirect_url(url_for("guests.index"))


@blueprint.route("/help")
def help():
    """Redirect: /help to /"""
    return redirect_url(url_for("main.index"))


@blueprint.route("/host")
@blueprint.route("/host/")
@blueprint.route("/hosts")
def hosts():
    """Redirect: /host and /hosts to /hosts/"""
    return redirect_url(url_for("hosts.index"))


@blueprint.route("/location")
@blueprint.route("/location/")
@blueprint.route("/locations")
def locations():
    """Redirect: /location and /locations to /locations/"""
    return redirect_url(url_for("locations.index"))


@blueprint.route("/panelist")
@blueprint.route("/panelist/")
@blueprint.route("/panelists")
def panelists():
    """Redirect: /panelist and /panelists to /panelists/"""
    return redirect_url(url_for("panelists.index"))


@blueprint.route("/scorekeeper")
@blueprint.route("/scorekeeper/")
@blueprint.route("/scorekeepers")
def scorekeepers():
    """Redirect: /scorekeeper and /scorekeepers to /scorekeepers/"""
    return redirect_url(url_for("scorekeepers.index"))


@blueprint.route("/search")
def search():
    """Redirect: /search to /"""
    return redirect_url(url_for("main.index"))


@blueprint.route("/show")
@blueprint.route("/show/")
@blueprint.route("/shows")
def shows():
    """Redirect: /show and /shows to /shows/"""
    return redirect_url(url_for("shows.index"))


@blueprint.route("/s/<string:show_date>")
def npr_show_redirect(show_date: str):
    """Takes an ISO-like date string and redirects to the appropriate
    show page on NPR's website."""
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
