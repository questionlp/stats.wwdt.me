# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Hosts Blueprint Views"""
import pytest

from tests.fixture import client


def test_index(client):
    """Testing hosts.index"""
    response = client.get("/hosts")
    assert response.status_code == 200
    assert b"Hosts" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("host_slug", ["faith-salie"])
def test_details(client, host_slug: str):
    """Testing hosts.details"""
    response = client.get(f"/hosts/{host_slug}")
    assert response.status_code == 200
    assert b"Host Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_all(client):
    """Testing hosts.all"""
    response = client.get("/hosts/all")
    assert response.status_code == 200
    assert b"Host Details" in response.data
    assert b"DB ID" in response.data
    assert b"Appearances" in response.data


def test_random(client):
    """Testing hosts.random"""
    response = client.get("/hosts/random")
    assert response.status_code == 302
    assert response.location
