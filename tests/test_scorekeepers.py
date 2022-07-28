# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Scorekeepers Module and Blueprint Views"""
from flask.testing import FlaskClient
import pytest
from werkzeug.test import TestResponse


def test_index(client: FlaskClient):
    """Testing scorekeepers.index"""
    response: TestResponse = client.get("/scorekeepers/")
    assert response.status_code == 200
    assert b"Scorekeepers" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("scorekeepers_slug", ["bill-kurtis"])
def test_details(client: FlaskClient, scorekeepers_slug: str):
    """Testing scorekeepers.details"""
    response: TestResponse = client.get(f"/scorekeepers/{scorekeepers_slug}")
    assert response.status_code == 200
    assert b"Scorekeeper Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_all(client: FlaskClient):
    """Testing scorekeepers.all"""
    response: TestResponse = client.get("/scorekeepers/all")
    assert response.status_code == 200
    assert b"Scorekeeper Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client: FlaskClient):
    """Testing scorekeepers.random"""
    response: TestResponse = client.get("/scorekeepers/random")
    assert response.status_code == 302
    assert response.location
