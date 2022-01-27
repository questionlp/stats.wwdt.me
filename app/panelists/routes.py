# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Panelists Routes for Wait Wait Stats Page"""
from flask import Blueprint, current_app, redirect, render_template, url_for
import mysql.connector
from wwdtm.panelist import Panelist

from app.utility import redirect_url

blueprint = Blueprint("panelists", __name__)


def random_panelist_slug() -> str:
    """Return a random panelist slug from ww_panelists table"""
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = _database_connection.cursor(dictionary=False)
    query = ("SELECT p.panelistslug FROM ww_panelists p "
             "WHERE p.panelistslug <> 'multiple' "
             "ORDER BY RAND() "
             "LIMIT 1;")
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if not result:
        return None

    return result[0]


@blueprint.route("/")
def index():
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=_database_connection)
    panelists = panelist.retrieve_all()
    _database_connection.close()

    if not panelists:
        return redirect(url_for("main.index"))

    return render_template("panelists/panelists.html", panelists=panelists)


@blueprint.route("/<string:panelist_slug>")
def details(panelist_slug: str):
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=_database_connection)
    details = panelist.retrieve_details_by_slug(panelist_slug)
    _database_connection.close()

    if not details:
        return redirect(url_for("panelists.index"))

    panelists = []
    panelists.append(details)
    return render_template("panelists/single.html",
                           panelist_name=details["name"],
                           panelists=panelists)


@blueprint.route("/all")
def all():
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=_database_connection)
    panelists = panelist.retrieve_all_details()
    _database_connection.close()

    if not panelists:
        return redirect(url_for("panelists.index"))

    return render_template("panelists/all.html", panelists=panelists)


@blueprint.route("/random")
def random():
    _slug = random_panelist_slug()
    return redirect_url(url_for("panelists.details", panelist_slug=_slug))
