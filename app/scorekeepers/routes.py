# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Scorekeepers Routes for Wait Wait Stats Page."""

import mysql.connector
from flask import Blueprint, Response, current_app, redirect, render_template, url_for
from slugify import slugify
from wwdtm.scorekeeper import Scorekeeper

from app.utility import redirect_url

blueprint = Blueprint("scorekeepers", __name__, template_folder="templates")


@blueprint.route("/")
def index() -> Response | str:
    """View: Scorekeepers Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    scorekeeper = Scorekeeper(database_connection=database_connection)
    scorekeepers = scorekeeper.retrieve_all()
    database_connection.close()

    if not scorekeepers:
        return redirect(url_for("main.index"))

    return render_template("scorekeepers/index.html", scorekeepers=scorekeepers)


@blueprint.route("/<string:scorekeeper_slug>")
def details(scorekeeper_slug: str) -> Response | str:
    """View: Scorekeeper Details."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    scorekeeper = Scorekeeper(database_connection=database_connection)
    slugs = scorekeeper.retrieve_all_slugs()
    _slug = slugify(scorekeeper_slug)

    if _slug not in slugs:
        database_connection.close()
        _scorekeeper_redirects: dict[str, str] = current_app.config["url_redirects"][
            "scorekeepers"
        ]["slugs"]
        if _scorekeeper_redirects and _slug in _scorekeeper_redirects:
            if _scorekeeper_redirects[_slug]:
                return redirect(
                    url_for(
                        "scorekeepers.details",
                        scorekeeper_slug=_scorekeeper_redirects[_slug],
                    ),
                    code=301,
                )

            return redirect_url(url_for("scorekeepers.index"))

        return redirect_url(url_for("scorekeepers.index"))

    if _slug in slugs and _slug != scorekeeper_slug:
        return redirect_url(url_for("scorekeepers.details", scorekeeper_slug=_slug))

    _details = scorekeeper.retrieve_details_by_slug(scorekeeper_slug)
    database_connection.close()

    if not _details:
        return redirect(url_for("scorekeepers.index"))

    scorekeepers = []
    scorekeepers.append(_details)

    return render_template(
        "scorekeepers/single.html",
        scorekeeper_name=_details["name"],
        scorekeepers=scorekeepers,
    )


@blueprint.route("/all")
def _all() -> Response | str:
    """View: Scorekeeper Details for All Scorekeepers."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    scorekeeper = Scorekeeper(database_connection=database_connection)
    scorekeepers = scorekeeper.retrieve_all_details()
    database_connection.close()

    if not scorekeepers:
        return redirect(url_for("scorekeepers.index"))

    return render_template("scorekeepers/all.html", scorekeepers=scorekeepers)


@blueprint.route("/random")
def random() -> Response:
    """View: Random Scorekeeper Redirect."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    scorekeeper = Scorekeeper(database_connection=database_connection)
    _slug = scorekeeper.retrieve_random_slug()
    database_connection.close()

    return redirect_url(url_for("scorekeepers.details", scorekeeper_slug=_slug))
