# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Guests Module and Blueprint Views."""

import pytest
from flask.testing import FlaskClient
from slugify import slugify
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing guests.index."""
    response: TestResponse = client.get("/guests/")
    assert response.status_code == 200
    assert b"Guests" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("guest_slug", ["tom-hanks"])
def test_details(client: FlaskClient, guest_slug: str) -> None:
    """Testing guests.details."""
    response: TestResponse = client.get(f"/guests/{guest_slug}")
    assert response.status_code == 200
    assert b"Guest Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


@pytest.mark.parametrize("guest_slug", ["Tom Hanks", "A'ja Wilson"])
def test_details_slug_match_redirect(client: FlaskClient, guest_slug: str) -> None:
    """Testing guests.details with slug matching redirection."""
    response: TestResponse = client.get(f"/guests/{guest_slug}")
    _slug = slugify(guest_slug)
    assert response.status_code == 302
    assert f"{_slug}" in response.headers["Location"]


@pytest.mark.parametrize("guest_slug", ["Thom Thanks", "A'j'a Wilsong"])
def test_details_slug_non_match_redirect(client: FlaskClient, guest_slug: str) -> None:
    """Testing guests.details with slug not matching redirection."""
    response: TestResponse = client.get(f"/guests/{guest_slug}")
    _slug = slugify(guest_slug)
    assert response.status_code == 302
    assert f"{_slug}" not in response.headers["Location"]


def test_all(client: FlaskClient) -> None:
    """Testing guests._all."""
    response: TestResponse = client.get("/guests/all")
    assert response.status_code == 200
    assert b"Guest Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing guests.random."""
    response: TestResponse = client.get("/guests/random")
    assert response.status_code == 302
    assert response.location
