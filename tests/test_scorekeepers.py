# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Scorekeepers Module and Blueprint Views."""

import pytest
from flask.testing import FlaskClient
from slugify import slugify
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing scorekeepers.index."""
    response: TestResponse = client.get("/scorekeepers/")
    assert response.status_code == 200
    assert b"Scorekeepers" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("scorekeeper_slug", ["bill-kurtis"])
def test_details(client: FlaskClient, scorekeeper_slug: str) -> None:
    """Testing scorekeepers.details."""
    response: TestResponse = client.get(f"/scorekeepers/{scorekeeper_slug}")
    assert response.status_code == 200
    assert b"Scorekeeper Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


@pytest.mark.parametrize("scorekeeper_slug", ["Carl Kasell", "Chioke I'Anson"])
def test_details_slug_match_redirect(
    client: FlaskClient, scorekeeper_slug: str
) -> None:
    """Testing scorekeepers.details with slug matching redirection."""
    response: TestResponse = client.get(f"/scorekeepers/{scorekeeper_slug}")
    _slug = slugify(scorekeeper_slug)
    assert response.status_code == 302
    assert f"{_slug}" in response.headers["Location"]


@pytest.mark.parametrize("scorekeeper_slug", ["Karl Cassel", "Chi'oke Ianson"])
def test_details_slug_non_match_redirect(
    client: FlaskClient, scorekeeper_slug: str
) -> None:
    """Testing scorekeepers.details with slug not matching redirection."""
    response: TestResponse = client.get(f"/scorekeepers/{scorekeeper_slug}")
    _slug = slugify(scorekeeper_slug)
    assert response.status_code == 302
    assert f"{_slug}" not in response.headers["Location"]


def test_all(client: FlaskClient) -> None:
    """Testing scorekeepers._all."""
    response: TestResponse = client.get("/scorekeepers/all")
    assert response.status_code == 200
    assert b"Scorekeeper Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing scorekeepers.random."""
    response: TestResponse = client.get("/scorekeepers/random")
    assert response.status_code == 302
    assert response.location
