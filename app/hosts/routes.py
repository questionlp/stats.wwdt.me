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
        database_connection.close()
        _host_redirects: dict[str, str] = current_app.config["url_redirects"]["hosts"][
            "slugs"
        ]
        if _host_redirects and _slug in _host_redirects:
            if _host_redirects[_slug]:
                return redirect(
                    url_for("hosts.details", host_slug=_host_redirects[_slug]), code=301
                )

            return redirect_url(url_for("hosts.index"))

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
    database_connection = mysql.connector.connect(**current_app.config["database"])
    host = Host(database_connection=database_connection)
    _slug = host.retrieve_random_slug()
    database_connection.close()

    return redirect_url(url_for("hosts.details", host_slug=_slug))
