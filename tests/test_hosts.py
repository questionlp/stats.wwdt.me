# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Hosts Module and Blueprint Views."""
import pytest
from flask.testing import FlaskClient
from slugify import slugify
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing hosts.index."""
    response: TestResponse = client.get("/hosts/")
    assert response.status_code == 200
    assert b"Hosts" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("host_slug", ["faith-salie"])
def test_details(client: FlaskClient, host_slug: str) -> None:
    """Testing hosts.details."""
    response: TestResponse = client.get(f"/hosts/{host_slug}")
    assert response.status_code == 200
    assert b"Host Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


@pytest.mark.parametrize("host_slug", ["Tom Hanks", "Luke Burbank"])
def test_details_slug_match_redirect(client: FlaskClient, host_slug: str) -> None:
    """Testing hosts.details with slug matching redirection."""
    response: TestResponse = client.get(f"/hosts/{host_slug}")
    _slug = slugify(host_slug)
    assert response.status_code == 302
    assert f"{_slug}" in response.headers["Location"]


@pytest.mark.parametrize("host_slug", ["Thom Thanks", "Luuuke Burbonk"])
def test_details_slug_non_match_redirect(client: FlaskClient, host_slug: str) -> None:
    """Testing hosts.details with slug not matching redirection."""
    response: TestResponse = client.get(f"/hosts/{host_slug}")
    _slug = slugify(host_slug)
    assert response.status_code == 302
    assert f"{_slug}" not in response.headers["Location"]


def test_all(client: FlaskClient) -> None:
    """Testing hosts._all."""
    response: TestResponse = client.get("/hosts/all")
    assert response.status_code == 200
    assert b"Host Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing hosts.random."""
    response: TestResponse = client.get("/hosts/random")
    assert response.status_code == 302
    assert response.location
