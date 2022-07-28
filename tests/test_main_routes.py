# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Main Routes Module and Blueprint Views"""
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_index(client: FlaskClient):
    """Testing main.index"""
    response: TestResponse = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Wait Wait" in response.data
    assert b"DB ID:" in response.data


def test_robots_txt(client: FlaskClient):
    """Testing main.robots_txt"""
    response: TestResponse = client.get("/robots.txt")
    assert response.status_code == 200
    assert b"Sitemap:" in response.data
    assert b"User-agent:" in response.data


def test_about(client: FlaskClient):
    """Testing main.about"""
    response: TestResponse = client.get("/about")
    assert response.status_code == 200
    assert b"Overview" in response.data
    assert b"Source Code" in response.data


def test_site_history(client: FlaskClient):
    """Testing main.site_history"""
    response: TestResponse = client.get("/site-history")
    assert response.status_code == 200
    assert b"Versions 1 and 2" in response.data
    assert b"Version 4" in response.data
