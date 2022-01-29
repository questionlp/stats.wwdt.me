# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Main Redirects Module and Blueprint Views"""
import pytest

from tests.fixture import client


def test_guest(client):
    """Testing main_redirects.guest"""
    response = client.get("/guest")
    assert response.status_code == 302
    assert response.location


def test_help(client):
    """Testing main_redirects.help"""
    response = client.get("/help")
    assert response.status_code == 302
    assert response.location


def test_host(client):
    """Testing main_redirects.host"""
    response = client.get("/host")
    assert response.status_code == 302
    assert response.location


def test_location(client):
    """Testing main_redirects.location"""
    response = client.get("/guest")
    assert response.status_code == 302
    assert response.location


def test_scorekeeper(client):
    """Testing main_redirects.scorekeeper"""
    response = client.get("/guest")
    assert response.status_code == 302
    assert response.location


def test_search(client):
    """Testing main_redirects.search"""
    response = client.get("/search")
    assert response.status_code == 302
    assert response.location


def test_show(client):
    """Testing main_redirects.show"""
    response = client.get("/show")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize("show_date", ["2018-10-27"])
def test_npr_show_redirect(client, show_date: str):
    """Testing main_redirects.guest"""
    response = client.get(f"/s/{show_date}")
    assert response.status_code == 302
    assert response.location
