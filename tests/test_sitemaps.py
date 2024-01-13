# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Sitemaps Module and Blueprint Views."""
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_primary(client: FlaskClient) -> None:
    """Testing sitemaps.primary."""
    response: TestResponse = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_guest(client: FlaskClient) -> None:
    """Testing sitemaps.guests."""
    response: TestResponse = client.get("/sitemap-guests.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_hosts(client: FlaskClient) -> None:
    """Testing sitemaps.hosts."""
    response: TestResponse = client.get("/sitemap-hosts.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_locations(client: FlaskClient) -> None:
    """Testing sitemaps.primary."""
    response: TestResponse = client.get("/sitemap-locations.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_panelists(client: FlaskClient) -> None:
    """Testing sitemaps.panelists."""
    response: TestResponse = client.get("/sitemap-panelists.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_scorekeepers(client: FlaskClient) -> None:
    """Testing sitemaps.scorekeepers."""
    response: TestResponse = client.get("/sitemap-scorekeepers.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_shows(client: FlaskClient) -> None:
    """Testing sitemaps.shows."""
    response: TestResponse = client.get("/sitemap-shows.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data
