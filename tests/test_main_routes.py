# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Main Routes Module and Blueprint Views."""

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing main.index."""
    response: TestResponse = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Wait Wait" in response.data
    assert b"DB ID:" in response.data


def test_robots_txt(client: FlaskClient) -> None:
    """Testing main.robots_txt."""
    response: TestResponse = client.get("/robots.txt")
    assert response.status_code == 200
    assert b"Sitemap:" in response.data
    assert b"User-agent:" in response.data


def test_about(client: FlaskClient) -> None:
    """Testing main.about."""
    response: TestResponse = client.get("/about")
    assert response.status_code == 200
    assert b"Overview" in response.data
    assert b"Source Code" in response.data


def test_site_history(client: FlaskClient) -> None:
    """Testing main.site_history."""
    response: TestResponse = client.get("/site-history")
    assert response.status_code == 200
    assert b"Versions 1 and 2" in response.data
    assert b"Version 4" in response.data


def test_teapot(client: FlaskClient) -> None:
    """Testing main.teapot."""
    response: TestResponse = client.get("/teapot")
    assert response.status_code == 418
    assert b"I'm a little teapot" in response.data

    response = client.post("/teapot")
    assert response.status_code == 418
    assert b"I'm a little teapot" in response.data


def test_teapot_brew(client: FlaskClient) -> None:
    """Testing main.teapot_brew."""
    # Testing passing in valid Content-Type for both endpoints
    response = client.open(
        "/",
        method="BREW",
        headers={"Content-Type": "application/coffee-pot-command"},
    )
    assert response.status_code == 418
    assert response.content_type == "application/json"
    assert b"I'm a teapot" in response.data

    response = client.open(
        "/teapot",
        method="BREW",
        headers={"Content-Type": "application/coffee-pot-command"},
    )
    assert response.status_code == 418
    assert response.content_type == "application/json"
    assert b"I'm a teapot" in response.data

    # Testing passing in incorrect Content-Type for both endpoints
    response = client.open("/", method="BREW")
    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert b"Move along home" in response.data

    response = client.open("/teapot", method="BREW")
    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert b"Move along home" in response.data
