# Copyright (c) 2018-2024 Linh Pham
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


@pytest.mark.parametrize("year", [2018])
def test_year(client: FlaskClient, year: int) -> None:
    """Testing shows.year."""
    response: TestResponse = client.get(f"/shows/{year}")
    assert response.status_code == 200
    assert b"January" in response.data
    assert b"All Shows from" in response.data


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


@pytest.mark.parametrize("year", [2018])
def test_year_all(client: FlaskClient, year: int) -> None:
    """Testing shows.year_all."""
    response: TestResponse = client.get(f"/shows/{year}/all")
    assert response.status_code == 200
    assert b"Show Details" in response.data
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


def test_recent(client: FlaskClient) -> None:
    """Testing shows.recent."""
    response: TestResponse = client.get("/shows/recent")
    assert response.status_code == 302
    assert response.location
