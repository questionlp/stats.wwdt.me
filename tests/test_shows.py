# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Shows Module and Blueprint Views."""

import pytest
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing shows.index."""
    response: TestResponse = client.get("/shows/")
    assert response.status_code == 200
    assert b"Shows" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("date_string", ["2018-10-27"])
def test_date_string(client: FlaskClient, date_string: str) -> None:
    """Testing shows.date_string."""
    response: TestResponse = client.get(f"/shows/{date_string}")
    assert response.status_code == 301
    assert response.location


@pytest.mark.parametrize("date_string", ["abcd-ef-gh", "1-2", "3-2-1"])
def test_date_string_invalid_value(client: FlaskClient, date_string: str) -> None:
    """Testing shows.date_string with invalid date strings."""
    response: TestResponse = client.get(f"/shows/{date_string}")
    assert response.status_code in (301, 302)
    assert response.location


@pytest.mark.parametrize("year", [2018])
def test_year(client: FlaskClient, year: int) -> None:
    """Testing shows.year."""
    response: TestResponse = client.get(f"/shows/{year}")
    assert response.status_code == 200
    assert b"January" in response.data
    assert b"All Shows from" in response.data


@pytest.mark.parametrize("year", [2018])
def test_year_all(client: FlaskClient, year: int) -> None:
    """Testing shows.year_all."""
    response: TestResponse = client.get(f"/shows/{year}/all")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year", [2008, 2010])
def test_year_best_ofs(client: FlaskClient, year: int) -> None:
    """Testing shows.year_best_ofs."""
    response: TestResponse = client.get(f"/shows/{year}/best-ofs")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Best Ofs" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year, month", [(2018, 10)])
def test_year_month(client: FlaskClient, year: int, month: int) -> None:
    """Testing shows.year_month."""
    response: TestResponse = client.get(f"/shows/{year}/{month}")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year, month, day", [(2018, 10, 27)])
def test_year_month_day(client: FlaskClient, year: int, month: int, day: int) -> None:
    """Testing shows.year_month_day."""
    response: TestResponse = client.get(f"/shows/{year}/{month}/{day}")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year", [2008, 2010])
def test_year_repeat_best_ofs(client: FlaskClient, year: int) -> None:
    """Testing shows.year_repeat_best_ofs."""
    response: TestResponse = client.get(f"/shows/{year}/repeat-best-ofs")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Best Ofs" in response.data
    assert b"Repeat:" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year", [2008, 2010])
def test_year_repeats(client: FlaskClient, year: int) -> None:
    """Testing shows.year_repeats."""
    response: TestResponse = client.get(f"/shows/{year}/repeats")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Repeat:" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_all(client: FlaskClient) -> None:
    """Testing shows._all."""
    response: TestResponse = client.get("/shows/all")
    assert response.status_code == 200
    assert b"All Show Details" in response.data
    assert b"show years" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_best_ofs(client: FlaskClient) -> None:
    """Testing shows.best_ofs."""
    response: TestResponse = client.get("/shows/best-ofs")
    assert response.status_code == 200
    assert b"Show Details: Best Ofs" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_on_this_day(client: FlaskClient) -> None:
    """Testing shows.on_this_day."""
    response: TestResponse = client.get("/shows/on-this-day")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"On This Day" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing shows.random."""
    response: TestResponse = client.get("/shows/random")
    assert response.status_code == 302
    assert response.location
    assert "/shows/" in response.location


@pytest.mark.parametrize("year", [1998, 2020])
def test_random_year_show(client: FlaskClient, year: int) -> None:
    """Testing shows.random_year_show."""
    response: TestResponse = client.get(f"/shows/random/{year}")
    assert response.status_code == 302
    assert str(year) in response.location


def test_recent(client: FlaskClient) -> None:
    """Testing shows.recent."""
    response: TestResponse = client.get("/shows/recent")
    assert response.status_code == 302
    assert response.location


def test_repeat_best_ofs(client: FlaskClient) -> None:
    """Testing shows.repeat_best_ofs."""
    response: TestResponse = client.get("/shows/repeat-best-ofs")
    assert response.status_code == 200
    assert b"Show Details: Repeat Best Ofs" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_repeats(client: FlaskClient) -> None:
    """Testing shows.repeats."""
    response: TestResponse = client.get("/shows/repeats")
    assert response.status_code == 200
    assert b"Show Details: Repeats" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data
