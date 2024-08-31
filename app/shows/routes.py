# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Shows Routes for Wait Wait Stats Page."""
import datetime
from datetime import date
from typing import Any

import mysql.connector
from flask import Blueprint, Response, current_app, render_template, url_for
from wwdtm.show import Show, ShowUtility

from app.locations.utility import format_location_name
from app.utility import redirect_url

blueprint = Blueprint("shows", __name__, template_folder="templates")


def random_show_date() -> str | None:
    """Return a random show date from the ww_shows table."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    cursor = database_connection.cursor(dictionary=False)
    query = (
        "SELECT s.showdate FROM ww_shows s "
        "WHERE s.showdate <= NOW() "
        "ORDER BY RAND() "
        "LIMIT 1;"
    )
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    database_connection.close()

    if not result:
        return None

    return result[0].strftime("%Y/%m/%d")


@blueprint.route("/")
def index() -> Response | str:
    """View: Shows Index."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    years = show.retrieve_years()
    database_connection.close()

    if not years:
        return redirect_url(url_for("main.index"))

    return render_template("shows/index.html", show_years=years)


@blueprint.route("/<string:iso_date_string>")
def date_string(iso_date_string: str) -> Response:
    """View: Show Details for a given ISO Date String."""
    try:
        parsed_date = datetime.datetime.strptime(iso_date_string, "%Y-%m-%d")
        database_connection = mysql.connector.connect(**current_app.config["database"])
        show_utility = ShowUtility(database_connection=database_connection)
        if not show_utility.date_exists(
            year=parsed_date.year, month=parsed_date.month, day=parsed_date.day
        ):
            return redirect_url(url_for("shows.index"))

        return redirect_url(
            url_for(
                "shows.year_month_day",
                show_year=parsed_date.year,
                show_month=parsed_date.month,
                show_day=parsed_date.day,
            ),
            301,
        )
    except ValueError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))


@blueprint.route("/<int:show_year>")
def year(show_year: str | int) -> Response | str:
    """View: List of Available Months for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _year = int(show_year)
        date_year = date(year=_year, month=1, day=1)
        show_months = show.retrieve_months_by_year(year=_year)
        database_connection.close()

        if not show_months:
            return redirect_url(url_for("shows.index"))

        months = []
        for month in show_months:
            months.append(date(year=_year, month=month, day=1))

        return render_template("shows/year.html", year=date_year, show_months=months)
    except ValueError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))


@blueprint.route("/<int:show_year>/<int:show_month>")
def year_month(show_year: int, show_month: int) -> Response | str:
    """View: Show Details for Year, Month."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _year_month = date(year=show_year, month=show_month, day=1)
        shows = show.retrieve_details_by_year_month(
            year=show_year,
            month=show_month,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )
        database_connection.close()

        if not shows:
            return redirect_url(url_for("shows.year", year=show_year))

        return render_template(
            "shows/year_month.html",
            year_month=_year_month,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", year=show_year))


@blueprint.route("/<int:show_year>/<int:show_month>/<int:show_day>")
def year_month_day(show_year: int, show_month: int, show_day: int) -> Response | str:
    """View: Show Details for a given Year, Month, Day."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        show_date = date(year=show_year, month=show_month, day=show_day)
        details = show.retrieve_details_by_date(
            year=show_year,
            month=show_month,
            day=show_day,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )
        database_connection.close()

        if not details:
            return redirect_url(
                url_for("shows.year_month", year=show_year, month=show_month)
            )

        show_list = []
        show_list.append(details)
        return render_template(
            "shows/single.html",
            show_date=show_date,
            shows=show_list,
            format_location_name=format_location_name,
        )
    except ValueError:
        database_connection.close()
        return redirect_url(url_for("shows.index"))


@blueprint.route("/<int:show_year>/all")
def year_all(show_year: int) -> Response | str | Any:
    """View: Show Details for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _ = date(year=show_year, month=1, day=1)
        shows = show.retrieve_details_by_year(
            year=show_year,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )
        database_connection.close()

        if not shows:
            return redirect_url(url_for("shows.index"))

        return render_template(
            "shows/year_all.html",
            year=show_year,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", show_year=show_year))


@blueprint.route("/all")
def _all() -> Response | str:
    """View: Show Details for All Shows."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        show_years = show.retrieve_years()

        if not show_years:
            return redirect_url(url_for("shows.index"))

        _shows_by_year = {}
        for _year in show_years:
            shows = show.retrieve_details_by_year(
                year=_year,
                include_decimal_scores=current_app.config["app_settings"][
                    "use_decimal_scores"
                ],
            )
            _shows_by_year[_year] = shows

        database_connection.close()

        return render_template(
            "shows/all.html",
            show_years=show_years,
            shows=_shows_by_year,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.index"))


@blueprint.route("/on-this-day")
def on_this_day() -> Response | str:
    """View: Show Details for Shows Aired On This Day."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    today = date.today()
    shows = show.retrieve_details_by_month_day(
        month=today.month,
        day=today.day,
        include_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"],
    )
    database_connection.close()

    if not shows:
        return redirect_url(url_for("shows.index"))

    return render_template(
        "shows/on_this_day.html", shows=shows, format_location_name=format_location_name
    )


@blueprint.route("/random")
def random() -> Response:
    """View: Random Show Redirect."""
    _date = random_show_date()
    return redirect_url(url_for("shows.date_string", iso_date_string=_date))


@blueprint.route("/recent")
def recent() -> Response:
    """Redirect: /shows/recent to /."""
    return redirect_url(url_for("main.index"))
