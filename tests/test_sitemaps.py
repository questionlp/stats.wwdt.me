# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Sitemaps Module and Blueprint Views"""
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_primary(client: FlaskClient):
    """Testing sitemaps.primary"""
    response: TestResponse = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_guest(client: FlaskClient):
    """Testing sitemaps.guests"""
    response: TestResponse = client.get("/sitemap-guests.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_hosts(client: FlaskClient):
    """Testing sitemaps.hosts"""
    response: TestResponse = client.get("/sitemap-hosts.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_locations(client: FlaskClient):
    """Testing sitemaps.primary"""
    response: TestResponse = client.get("/sitemap-locations.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_panelists(client: FlaskClient):
    """Testing sitemaps.panelists"""
    response: TestResponse = client.get("/sitemap-panelists.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_scorekeepers(client: FlaskClient):
    """Testing sitemaps.scorekeepers"""
    response: TestResponse = client.get("/sitemap-scorekeepers.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data


def test_shows(client: FlaskClient):
    """Testing sitemaps.shows"""
    response: TestResponse = client.get("/sitemap-shows.xml")
    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/xml; charset=utf-8"
    assert b"?xml" in response.data
    assert b"urlset" in response.data
