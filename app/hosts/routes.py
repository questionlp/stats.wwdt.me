# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Hosts Routes for Wait Wait Stats Page"""
from flask import Blueprint, current_app, redirect, render_template, url_for
import mysql.connector
from wwdtm.host import Host

from app.utility import redirect_url

blueprint = Blueprint("hosts", __name__)


def random_host_slug() -> str:
    """Return a random host slug from ww_hosts table"""
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = _database_connection.cursor(dictionary=False)
    query = ("SELECT h.hostslug FROM ww_hosts h "
             "WHERE h.hostslug <> 'tbd' "
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
    host = Host(database_connection=_database_connection)
    hosts = host.retrieve_all()
    _database_connection.close()

    if not hosts:
        return redirect(url_for("main.index"))

    return render_template("hosts/hosts.html", hosts=hosts)


@blueprint.route("/<string:host_slug>")
def details(host_slug: str):
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=_database_connection)
    details = host.retrieve_details_by_slug(host_slug)
    _database_connection.close()

    if not details:
        return redirect(url_for("hosts.index"))

    hosts = []
    hosts.append(details)
    return render_template("hosts/single.html",
                           host_name=details["name"],
                           hosts=hosts)


@blueprint.route("/all")
def all():
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=_database_connection)
    hosts = host.retrieve_all_details()
    _database_connection.close()

    if not hosts:
        return redirect(url_for("hosts.index"))

    return render_template("hosts/all.html", hosts=hosts)


@blueprint.route("/random")
def random():
    _slug = random_host_slug()
    return redirect_url(url_for("hosts.details", host_slug=_slug))
