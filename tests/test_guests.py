# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Guests Module and Blueprint Views"""
from flask.testing import FlaskClient
import pytest
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing guests.index"""
    response: TestResponse = client.get("/guests/")
    assert response.status_code == 200
    assert b"Guests" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("guest_slug", ["tom-hanks"])
def test_details(client: FlaskClient, guest_slug: str) -> None:
    """Testing guests.details"""
    response: TestResponse = client.get(f"/guests/{guest_slug}")
    assert response.status_code == 200
    assert b"Guest Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_all(client: FlaskClient) -> None:
    """Testing guests.all"""
    response: TestResponse = client.get("/guests/all")
    assert response.status_code == 200
    assert b"Guest Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client: FlaskClient) -> None:
    """Testing guests.random"""
    response: TestResponse = client.get("/guests/random")
    assert response.status_code == 302
    assert response.location
