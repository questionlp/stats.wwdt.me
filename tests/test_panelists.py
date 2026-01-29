# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Panelists Module and Blueprint Views."""

import pytest
from flask.testing import FlaskClient
from slugify import slugify
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing panelists.index."""
    response: TestResponse = client.get("/panelists/")
    assert response.status_code == 200
    assert b"Panelists" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("panelist_slug", ["faith-salie"])
def test_details(client: FlaskClient, panelist_slug: str) -> None:
    """Testing panelists.details."""
    response: TestResponse = client.get(f"/panelists/{panelist_slug}")
    assert response.status_code == 200
    assert b"Panelist Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


@pytest.mark.parametrize("panelist_slug", ["Luke Burbank", "Faith Salie"])
def test_details_slug_match_redirect(client: FlaskClient, panelist_slug: str) -> None:
    """Testing panelists.details with slug matching redirection."""
    response: TestResponse = client.get(f"/panelists/{panelist_slug}")
    _slug = slugify(panelist_slug)
    assert response.status_code == 302
    assert f"{_slug}" in response.headers["Location"]


@pytest.mark.parametrize("panelist_slug", ["Luuuke Burbonk", "Faiths Sally"])
def test_details_slug_non_match_redirect(
    client: FlaskClient, panelist_slug: str
) -> None:
    """Testing panelists.details with slug not matching redirection."""
    response: TestResponse = client.get(f"/panelists/{panelist_slug}")
    _slug = slugify(panelist_slug)
    assert response.status_code == 302
    assert f"{_slug}" not in response.headers["Location"]


def test_all(client: FlaskClient) -> None:
    """Testing panelists._all."""
    response: TestResponse = client.get("/panelists/all")
    assert response.status_code == 200
    assert b"Panelist Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing panelists.random."""
    response: TestResponse = client.get("/panelists/random")
    assert response.status_code == 302
    assert response.location
