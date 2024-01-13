# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Panelists Module and Blueprint Views."""
import pytest
from flask.testing import FlaskClient
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


def test_all(client: FlaskClient) -> None:
    """Testing panelists.all."""
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
