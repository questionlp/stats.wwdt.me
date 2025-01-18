# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Hosts Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, redirect, render_template, url_for
from slugify import slugify
from wwdtm.host import Host

from app.utility import redirect_url

blueprint = Blueprint("hosts", __name__, template_folder="templates")


def random_host_slug() -> str | None:
    """Return a random host slug from ww_hosts table."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = database_connection.cursor(dictionary=False)
    query = (
        "SELECT h.hostslug FROM ww_hosts h "
        "WHERE h.hostslug <> 'tbd' "
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
    """View: Hosts Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=database_connection)
    hosts = host.retrieve_all()
    database_connection.close()

    if not hosts:
        return redirect(url_for("main.index"))

    return render_template("hosts/index.html", hosts=hosts)


@blueprint.route("/<string:host_slug>")
def details(host_slug: str) -> Response | str:
    """View: Host Details."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=database_connection)
    slugs = host.retrieve_all_slugs()
    _slug = slugify(host_slug)

    if _slug not in slugs:
        return redirect(url_for("hosts.index"))

    if _slug in slugs and _slug != host_slug:
        return redirect_url(url_for("hosts.details", host_slug=_slug))

    _details = host.retrieve_details_by_slug(host_slug)
    database_connection.close()

    if not _details:
        return redirect(url_for("hosts.index"))

    hosts = []
    hosts.append(_details)
    return render_template("hosts/single.html", host_name=_details["name"], hosts=hosts)


@blueprint.route("/all")
def _all() -> Response | str:
    """View: Host Details for All Hosts."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=database_connection)
    hosts = host.retrieve_all_details()
    database_connection.close()

    if not hosts:
        return redirect(url_for("hosts.index"))

    return render_template("hosts/all.html", hosts=hosts)


@blueprint.route("/random")
def random() -> Response:
    """View: Random Host Redirect."""
    _slug = random_host_slug()
    return redirect_url(url_for("hosts.details", host_slug=_slug))
