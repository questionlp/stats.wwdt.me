# Copyright (c) 2018-2025 Linh Pham
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


@blueprint.route("/best-ofs")
def best_ofs() -> Response:
    """View: Show Details for all Best Of shows."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    _best_ofs = show.retrieve_all_best_ofs_details(
        include_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"]
    )
    database_connection.close()
    if not _best_ofs:
        return redirect_url(url_for("main.index"))

    return render_template(
        "shows/best-ofs.html",
        shows=_best_ofs,
        format_location_name=format_location_name,
    )


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
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>")
def year(show_year: str | int) -> Response | str:
    """View: List of Available Months for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _year = int(show_year)
        date_year = date(year=_year, month=1, day=1)
        show_months = show.retrieve_months_by_year(year=_year)
        show_counts = show.retrieve_counts_by_year(year=_year, inclusive=True)

        if not show_months:
            return redirect_url(url_for("shows.index"))

        months = []
        for month in show_months:
            months.append(date(year=_year, month=month, day=1))

        return render_template(
            "shows/year.html",
            year=date_year,
            show_months=months,
            show_counts=show_counts,
        )
    except ValueError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>/all")
def year_all(show_year: int) -> Response | str | Any:
    """View: Show Details for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _date = date(year=show_year, month=1, day=1)
        shows = show.retrieve_details_by_year(
            year=_date.year,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )

        if not shows:
            return redirect_url(url_for("shows.index"))

        return render_template(
            "shows/year-all.html",
            year=_date.year,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", show_year=show_year))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>/best-ofs")
def year_best_ofs(show_year: str | int) -> Response | str:
    """View: Best Of Shows for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _date = date(year=show_year, month=1, day=1)
        shows = show.retrieve_best_ofs_details_by_year(
            year=show_year,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )

        if not shows:
            return redirect_url(url_for("shows.year", show_year=show_year))

        return render_template(
            "shows/year-best-ofs.html",
            year=_date.year,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", show_year=show_year))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>/<int:show_month>")
def year_month(show_year: int, show_month: int) -> Response | str:
    """View: Show Details for Year, Month."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _date = date(year=show_year, month=show_month, day=1)
        shows = show.retrieve_details_by_year_month(
            year=_date.year,
            month=_date.month,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )

        if not shows:
            return redirect_url(url_for("shows.year", show_year=show_year))

        return render_template(
            "shows/year-month.html",
            year_month=_date,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", show_year=show_year))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>/<int:show_month>/<int:show_day>")
def year_month_day(show_year: int, show_month: int, show_day: int) -> Response | str:
    """View: Show Details for a given Year, Month, Day."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _date = date(year=show_year, month=show_month, day=show_day)
        details = show.retrieve_details_by_date(
            year=_date.year,
            month=_date.month,
            day=_date.day,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )

        if not details:
            return redirect_url(
                url_for(
                    "shows.year_month", show_year=_date.year, show_month=_date.month
                )
            )

        show_list = []
        show_list.append(details)
        return render_template(
            "shows/single.html",
            show_date=_date,
            shows=show_list,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>/repeat-best-ofs")
def year_repeat_best_ofs(show_year: str | int) -> Response | str:
    """View: Repeat Best Of Shows for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _date = date(year=show_year, month=1, day=1)
        shows = show.retrieve_repeat_best_ofs_details_by_year(
            year=_date.year,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )

        if not shows:
            return redirect_url(url_for("shows.year", show_year=_date.year))

        return render_template(
            "shows/year-repeat-best-ofs.html",
            year=_date.year,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", show_year=show_year))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/<int:show_year>/repeats")
def year_repeats(show_year: str | int) -> Response | str:
    """View: Best Of Shows for Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _date = date(year=show_year, month=1, day=1)
        shows = show.retrieve_repeats_details_by_year(
            year=_date.year,
            include_decimal_scores=current_app.config["app_settings"][
                "use_decimal_scores"
            ],
        )

        if not shows:
            return redirect_url(url_for("shows.year", show_year=_date.year))

        return render_template(
            "shows/year-repeats.html",
            year=_date.year,
            shows=shows,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.year", show_year=show_year))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


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

        return render_template(
            "shows/all.html",
            show_years=show_years,
            shows=_shows_by_year,
            format_location_name=format_location_name,
        )
    except ValueError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


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
        "shows/on-this-day.html", shows=shows, format_location_name=format_location_name
    )


@blueprint.route("/random")
def random() -> Response:
    """View: Random Show Redirect."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    _date = show.retrieve_random_date_object()
    database_connection.close()

    if not _date:
        return redirect_url(url_for("shows.index"))

    return redirect_url(
        url_for(
            "shows.year_month_day",
            show_year=_date.year,
            show_month=_date.month,
            show_day=_date.day,
        )
    )


@blueprint.route("/random/<int:show_year>")
def random_year_show(show_year: int) -> Response:
    """View: Random Show for a Given Year."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)

    try:
        _year = int(show_year)
        _ = date(year=_year, month=1, day=1)
        _date = show.retrieve_random_date_object_by_year(year=show_year)

        if not _date:
            return redirect_url(url_for("shows.index"))

        return redirect_url(
            url_for(
                "shows.year_month_day",
                show_year=_date.year,
                show_month=_date.month,
                show_day=_date.day,
            )
        )
    except ValueError:
        return redirect_url(url_for("shows.index"))
    except TypeError:
        return redirect_url(url_for("shows.index"))
    except OverflowError:
        return redirect_url(url_for("shows.index"))
    finally:
        database_connection.close()


@blueprint.route("/recent")
def recent() -> Response:
    """Redirect: /shows/recent to /."""
    return redirect_url(url_for("main.index"))


@blueprint.route("/repeat-best-ofs")
def repeat_best_ofs() -> Response:
    """View: Show Details for all Repeat Best Of shows."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    _shows = show.retrieve_all_repeat_best_ofs_details(
        include_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"]
    )
    database_connection.close()
    if not _shows:
        return redirect_url(url_for("main.index"))

    return render_template(
        "shows/repeat-best-ofs.html",
        shows=_shows,
        format_location_name=format_location_name,
    )


@blueprint.route("/repeats")
def repeats() -> Response:
    """View: Show Details for all Repeat shows."""
    database_connection = mysql.connector.connect(**current_app.config["database"])
    show = Show(database_connection=database_connection)
    _repeats = show.retrieve_all_repeats_details(
        include_decimal_scores=current_app.config["app_settings"]["use_decimal_scores"]
    )
    database_connection.close()
    if not _repeats:
        return redirect_url(url_for("main.index"))

    return render_template(
        "shows/repeats.html",
        shows=_repeats,
        format_location_name=format_location_name,
    )
