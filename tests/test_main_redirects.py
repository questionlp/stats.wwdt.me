# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Main Redirects Module and Blueprint Views."""

import pytest
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_favicon(client: FlaskClient) -> None:
    """Testing main_redirects.favicon."""
    response: TestResponse = client.get("/favicon.ico")
    assert response.status_code == 302
    assert response.location


def test_guests(client: FlaskClient) -> None:
    """Testing main_redirects.guests."""
    response: TestResponse = client.get("/guest")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/guest/")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/guests")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("guest_slug", ["tom-hanks"])
def test_guests_details(client: FlaskClient, guest_slug: str) -> None:
    """Testing main_redirects.guests_details."""
    response: TestResponse = client.get(f"/guest/{guest_slug}")
    assert response.status_code == 301
    assert response.location


def test_help(client: FlaskClient) -> None:
    """Testing main_redirects.help_page."""
    response: TestResponse = client.get("/help")
    assert response.status_code == 302
    assert response.location


def test_hosts(client: FlaskClient) -> None:
    """Testing main_redirects.hosts."""
    response: TestResponse = client.get("/host")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/host/")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/hosts")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("host_slug", ["faith-salie"])
def test_hosts_details(client: FlaskClient, host_slug: str) -> None:
    """Testing main_redirects.hosts_details."""
    response: TestResponse = client.get(f"/host/{host_slug}")
    assert response.status_code == 301
    assert response.location


def test_info(client: FlaskClient) -> None:
    """Testing main_redirects.info."""
    response: TestResponse = client.get("info")
    assert response.status_code == 302
    assert response.location
    assert "understanding-data" in response.location


def test_locations(client: FlaskClient) -> None:
    """Testing main_redirects.locations."""
    response: TestResponse = client.get("/location")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/location/")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/locations")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize(
    "location_slug",
    [
        "comerica-theatre-phoenix-az",
        "arizona-financial-theatre-comerica-theatre-phoenix-az",
    ],
)
def test_locations_details(client: FlaskClient, location_slug: str) -> None:
    """Testing main_redirects.locations_details."""
    response: TestResponse = client.get(f"/location/{location_slug}")
    assert response.status_code == 301
    assert response.location


def test_panelists(client: FlaskClient) -> None:
    """Testing main_redirects.panelists."""
    response: TestResponse = client.get("/panelist")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/panelist/")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/panelists")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("panelist_slug", ["faith-salie"])
def test_panelists_details(client: FlaskClient, panelist_slug: str) -> None:
    """Testing main_redirects.panelists_details."""
    response: TestResponse = client.get(f"/panelist/{panelist_slug}")
    assert response.status_code == 301
    assert response.location


def test_scorekeepers(client: FlaskClient) -> None:
    """Testing main_redirects.scorekeepers."""
    response: TestResponse = client.get("/scorekeeper")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/scorekeeper/")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/scorekeepers")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("scorekeeper_slug", ["bill-kurtis"])
def test_scorekeepers_details(client: FlaskClient, scorekeeper_slug: str) -> None:
    """Testing main_redirects.scorekeepers_details."""
    response: TestResponse = client.get(f"/scorekeeper/{scorekeeper_slug}")
    assert response.status_code == 301
    assert response.location


def test_search(client: FlaskClient) -> None:
    """Testing main_redirects.search."""
    response: TestResponse = client.get("/search")
    assert response.status_code == 302
    assert response.location


def test_shows(client: FlaskClient) -> None:
    """Testing main_redirects.shows."""
    response: TestResponse = client.get("/show")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/show/")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/shows")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("iso_date_string", ["2018-10-27"])
def test_shows_date_string(client: FlaskClient, iso_date_string: str) -> None:
    """Testing main_redirects.shows_date_string."""
    response: TestResponse = client.get(f"/show/{iso_date_string}")
    assert response.status_code == 301
    assert response.location


@pytest.mark.parametrize("year", [2018])
def test_shows_year(client: FlaskClient, year: int) -> None:
    """Testing main_redirects.shows_year."""
    response: TestResponse = client.get(f"/show/{year}")
    assert response.status_code == 301
    assert response.location


@pytest.mark.parametrize("year, month", [(2018, 10)])
def test_shows_year_month(client: FlaskClient, year: int, month: int) -> None:
    """Testing main_redirects.shows_year_month."""
    response: TestResponse = client.get(f"/show/{year}/{month}")
    assert response.status_code == 301
    assert response.location


@pytest.mark.parametrize("year, month, day", [(2018, 10, 27)])
def test_shows_year_month_day(
    client: FlaskClient, year: int, month: int, day: int
) -> None:
    """Testing main_redirects.shows_year_month_day."""
    response: TestResponse = client.get(f"/show/{year}/{month}/{day}")
    assert response.status_code == 301
    assert response.location


def test_shows_best_of_repeats(client: FlaskClient) -> None:
    """Testing main_redirects.shows_best_of_repeats."""
    response: TestResponse = client.get("/shows/best-of-repeats")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("show_date", ["1998-01-03", "1998-01-08", "2018-10-27"])
def test_npr_show_redirect(client: FlaskClient, show_date: str) -> None:
    """Testing main_redirects.guest."""
    response: TestResponse = client.get(f"/s/{show_date}")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("show_date", ["abcd"])
def test_npr_show_redirect_invalid_date(client: FlaskClient, show_date: str) -> None:
    """Testing main_redirects.guest."""
    response: TestResponse = client.get(f"/s/{show_date}")
    assert response.status_code == 302
    assert response.location


def test_stats(client: FlaskClient) -> None:
    """Testing main_redirects.stats."""
    response: TestResponse = client.get("/stats")
    assert response.status_code == 301
    assert response.location

    response: TestResponse = client.get("/stats/")
    assert response.status_code == 301
    assert response.location
