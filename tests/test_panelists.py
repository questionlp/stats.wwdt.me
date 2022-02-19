# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Panelists Module and Blueprint Views"""
import pytest


def test_index(client):
    """Testing panelists.index"""
    response = client.get("/panelists")
    assert response.status_code == 200
    assert b"Panelists" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("panelist_slug", ["faith-salie"])
def test_details(client, panelist_slug: str):
    """Testing panelists.details"""
    response = client.get(f"/panelists/{panelist_slug}")
    assert response.status_code == 200
    assert b"Panelist Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_all(client):
    """Testing panelists.all"""
    response = client.get("/panelists/all")
    assert response.status_code == 200
    assert b"Panelist Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client):
    """Testing panelists.random"""
    response = client.get("/panelists/random")
    assert response.status_code == 302
    assert response.location
