# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Main Routes for Wait Wait Stats Page"""
from flask import Blueprint, current_app, render_template
import mysql.connector
from wwdtm.show import Show

from app.config import DEFAULT_RECENT_DAYS_AHEAD, DEFAULT_RECENT_DAYS_BACK
from app.locations.utility import format_location_name

blueprint = Blueprint("main", __name__)


@blueprint.route("/")
def index():
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    _settings = current_app.config["app_settings"]

    try:
        if "recent_days_ahead" in _settings:
            days_ahead = int(_settings["recent_days_ahead"])
            days_back = int(_settings["recent_days_back"])
        else:
            days_ahead = DEFAULT_RECENT_DAYS_AHEAD
            days_back = DEFAULT_RECENT_DAYS_BACK
    except TypeError:
        days_ahead = DEFAULT_RECENT_DAYS_AHEAD
        days_back = DEFAULT_RECENT_DAYS_BACK
    except ValueError:
        days_ahead = DEFAULT_RECENT_DAYS_AHEAD
        days_back = DEFAULT_RECENT_DAYS_BACK

    try:
        show = Show(database_connection=_database_connection)
        recent = show.retrieve_recent_details(include_days_ahead=days_ahead,
                                              include_days_back=days_back)
        recent.reverse()
    except AttributeError:
        recent = show.retrieve_recent_details()
        recent.reverse()
    finally:
        _database_connection.close()

    return render_template("pages/index.html",
                           shows=recent,
                           format_location_name=format_location_name)


@blueprint.route("/about")
def about():
    return render_template("pages/about.html")


@blueprint.route("/site-history")
def site_history():
    return render_template("pages/site_history.html")
