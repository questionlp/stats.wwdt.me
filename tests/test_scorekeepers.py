# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Scorekeepers Module and Blueprint Views"""
import pytest


def test_index(client):
    """Testing scorekeepers.index"""
    response = client.get("/scorekeepers")
    assert response.status_code == 200
    assert b"Panelists" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("scorekeepers_slug", ["bill-kurtis"])
def test_details(client, scorekeepers_slug: str):
    """Testing scorekeepers.details"""
    response = client.get(f"/scorekeepers/{scorekeepers_slug}")
    assert response.status_code == 200
    assert b"Scorekeeper Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_all(client):
    """Testing scorekeepers.all"""
    response = client.get("/scorekeepers/all")
    assert response.status_code == 200
    assert b"Scorekeeper Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client):
    """Testing scorekeepers.random"""
    response = client.get("/scorekeepers/random")
    assert response.status_code == 302
    assert response.location
