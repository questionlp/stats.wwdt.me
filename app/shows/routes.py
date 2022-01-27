# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Shows Routes for Wait Wait Stats Page"""
from datetime import date

from dateutil import parser
from flask import Blueprint, current_app, render_template, url_for
import mysql.connector
from typing import Union
from wwdtm.show import Show
from app.locations.utility import format_location_name

from app.utility import redirect_url

blueprint = Blueprint("shows", __name__)


def random_show_date() -> str:
    """Return a random show date from the ww_shows table"""
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = _database_connection.cursor(dictionary=False)
    query = ("SELECT s.showdate FROM ww_shows s "
             "WHERE s.showdate <= NOW() "
             "ORDER BY RAND() "
             "LIMIT 1;")
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if not result:
        return None

    return result[0].isoformat()


@blueprint.route("/")
def index():
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=_database_connection)
    years = show.retrieve_years()
    _database_connection.close()

    if not years:
        return redirect_url(url_for("main.index"))

    return render_template("shows/shows.html", show_years=years)


@blueprint.route("/<string:date_string>")
def date_string(date_string: int):
    try:
        parsed_date = parser.parse(date_string)
        return redirect_url(url_for("shows.year_month_day",
                                    year=parsed_date.year,
                                    month=parsed_date.month,
                                    day=parsed_date.day))
    except parser.ParserError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))


@blueprint.route("/<int:year>")
def year(year: Union[str, int]):
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=_database_connection)

    try:
        year = int(year)
        date_year = date(year=year, month=1, day=1)
        show_months = show.retrieve_months_by_year(year=year)
        _database_connection.close()

        if not show_months:
            return redirect_url(url_for("shows.index"))

        months = []
        for month in show_months:
            months.append(date(year=year, month=month, day=1))

        return render_template("shows/year.html",
                               year=date_year,
                               show_months=months)
    except ValueError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))


@blueprint.route("/<int:year>/<int:month>")
def year_month(year: int, month: int):
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=_database_connection)

    try:
        year_month = date(year=year, month=month, day=1)
        shows = show.retrieve_details_by_year_month(year=year, month=month)
        _database_connection.close()

        if not shows:
            return redirect_url(url_for("shows.year"), year=year)

        return render_template("shows/year_month.html",
                               year_month=year_month,
                               shows=shows,
                               format_location_name=format_location_name)
    except ValueError:
        return redirect_url(url_for("shows.year"), year=year)


@blueprint.route("/<int:year>/<int:month>/<int:day>")
def year_month_day(year: int, month: int, day: int):
    _database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=_database_connection)

    try:
        show_date = date(year=year, month=month, day=day)
        details = show.retrieve_details_by_date(year=year, month=month, day=day)

        if not details:
            return redirect_url(url_for("shows.year_month",
                                year=year,
                                month=month))

        show_list = []
        show_list.append(details)
        return render_template("shows/single.html",
                               show_date=show_date,
                               shows=show_list,
                               format_location_name=format_location_name)
    except ValueError:
        return redirect_url(url_for("shows.index"))


@blueprint.route("/<int:year>/all")
def year_all(year: int):
    return f"All Details: Year {year}"


@blueprint.route("/all")
def all():
    return "Details: All Locations"


@blueprint.route("/on-this-day")
def on_this_day():
    return "Details: On This Day"


@blueprint.route("/random")
def random():
    _date = random_show_date()
    return redirect_url(url_for("shows.date_string", date_string=_date))


@blueprint.route("/recent")
def recent():
    return "Details: Recent"
