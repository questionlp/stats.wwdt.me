# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Locations Module and Blueprint Views."""
import pytest
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from app.locations.utility import format_location_name


def test_index(client: FlaskClient) -> None:
    """Testing locations.index."""
    response: TestResponse = client.get("/locations/")
    assert response.status_code == 200
    assert b"Locations" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("location_slug", ["chase-auditorium-chicago-il"])
def test_details(client: FlaskClient, location_slug: str) -> None:
    """Testing locations.details."""
    response: TestResponse = client.get(f"/locations/{location_slug}")
    assert response.status_code == 200
    assert b"Location Details" in response.data
    assert b"DB ID" in response.data
    assert b"Recordings" in response.data


def test_all(client: FlaskClient) -> None:
    """Testing locations._all."""
    response: TestResponse = client.get("/locations/all")
    assert response.status_code == 200
    assert b"Location Details" in response.data
    assert b"DB ID" in response.data
    assert b"Recordings" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing locations.random."""
    response: TestResponse = client.get("/locations/random")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize(
    "location",
    [
        {
            "venue": "Chase Auditorium",
            "city": "Chicago",
            "state": "IL",
        }
    ],
)
def test_format_location_name(location: dict[str, str]) -> None:
    """Testing locations.utility.format_location_name()."""
    name: str | None = format_location_name(location)
    assert name
