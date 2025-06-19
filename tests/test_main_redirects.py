# Copyright (c) 2018-2025 Linh Pham
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


def test_shows_best_of_repeats(client: FlaskClient) -> None:
    """Testing main_redirects.shows_best_of_repeats."""
    response: TestResponse = client.get("/shows/best-of-repeats")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("show_date", ["2018-10-27"])
def test_npr_show_redirect(client: FlaskClient, show_date: str) -> None:
    """Testing main_redirects.guest."""
    response: TestResponse = client.get(f"/s/{show_date}")
    assert response.status_code == 302
    assert response.location
