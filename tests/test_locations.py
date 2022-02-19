# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Locations Module and Blueprint Views"""
from typing import Any, Dict

import pytest

from app.locations.utility import format_location_name


def test_index(client):
    """Testing locations.index"""
    response = client.get("/locations")
    assert response.status_code == 200
    assert b"Locations" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("location_slug", ["chase-auditorium-chicago-il"])
def test_details(client, location_slug: str):
    """Testing locations.details"""
    response = client.get(f"/locations/{location_slug}")
    assert response.status_code == 200
    assert b"Location Details" in response.data
    assert b"DB ID" in response.data
    assert b"Recordings" in response.data


def test_all(client):
    """Testing locations.all"""
    response = client.get("/locations/all")
    assert response.status_code == 200
    assert b"Location Details" in response.data
    assert b"DB ID" in response.data
    assert b"Recordings" in response.data


def test_random(client):
    """Testing locations.random"""
    response = client.get("/locations/random")
    assert response.status_code == 302
    assert response.location


@pytest.mark.parametrize(
    "location",
    [
        {
            "venue": "Chase Auditorium",
            "city": "Chicago",
            "state": "IL",
        }
    ],
)
def test_format_location_name(client, location: Dict[str, Any]):
    """Testing locations.utility.format_location_name()"""
    name = format_location_name(location)
    assert name
