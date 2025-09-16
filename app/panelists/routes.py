# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Panelists Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, redirect, render_template, url_for
from slugify import slugify
from wwdtm.panelist import Panelist

from app.utility import redirect_url

blueprint = Blueprint("panelists", __name__, template_folder="templates")


@blueprint.route("/")
def index() -> Response | str:
    """View: Panelists Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=database_connection)
    panelists = panelist.retrieve_all()
    database_connection.close()

    if not panelists:
        return redirect(url_for("main.index"))

    return render_template("panelists/index.html", panelists=panelists)


@blueprint.route("/<string:panelist_slug>")
def details(panelist_slug: str) -> Response | str:
    """View: Panelists Details."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=database_connection)
    slugs = panelist.retrieve_all_slugs()
    _slug = slugify(panelist_slug)

    if _slug not in slugs:
        database_connection.close()
        _panelist_redirects: dict[str, str] = current_app.config["url_redirects"][
            "panelists"
        ]["slugs"]
        if _panelist_redirects and _slug in _panelist_redirects:
            if _panelist_redirects[_slug]:
                return redirect(
                    url_for(
                        "panelists.details", panelist_slug=_panelist_redirects[_slug]
                    ),
                    code=301,
                )

            return redirect(url_for("panelists.index"))

        return redirect(url_for("panelists.index"))

    if _slug in slugs and _slug != panelist_slug:
        return redirect(url_for("panelists.details", panelist_slug=_slug))

    _details = panelist.retrieve_details_by_slug(
        panelist_slug,
        use_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"],
    )
    database_connection.close()

    if not _details:
        return redirect(url_for("panelists.index"))

    panelists = []
    panelists.append(_details)

    return render_template(
        "panelists/single.html", panelist_name=_details["name"], panelists=panelists
    )


@blueprint.route("/all")
def _all() -> Response | str:
    """View: Panelist Details for All Panelists."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=database_connection)
    panelists = panelist.retrieve_all_details(
        use_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"]
    )
    database_connection.close()

    if not panelists:
        return redirect(url_for("panelists.index"))

    return render_template("panelists/all.html", panelists=panelists)


@blueprint.route("/random")
def random() -> Response:
    """View: Random Panelist Redirect."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    panelist = Panelist(database_connection=database_connection)
    _slug = panelist.retrieve_random_slug()
    database_connection.close()

    return redirect_url(url_for("panelists.details", panelist_slug=_slug))
