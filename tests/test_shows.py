# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Shows Module and Blueprint Views"""
import pytest

from tests.fixture import client


def test_index(client):
    """Testing shows.index"""
    response = client.get("/shows")
    assert response.status_code == 200
    assert b"Shows" in response.data
    assert b"Random" in response.data


@pytest.mark.parametrize("date_string", ["2018-10-27"])
def test_date_string(client, date_string: str):
    """Testing shows.date_string"""
    response = client.get(f"/shows/{date_string}")
    assert response.status_code == 301
    assert response.location


@pytest.mark.parametrize("year", [2018])
def test_year(client, year: int):
    """Testing shows.year"""
    response = client.get(f"/shows/{year}")
    assert response.status_code == 200
    assert b"January" in response.data
    assert b"All Shows from" in response.data


@pytest.mark.parametrize("year, month", [(2018, 10)])
def test_year_month(client, year: int, month: int):
    """Testing shows.year_month"""
    response = client.get(f"/shows/{year}/{month}")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year, month, day", [(2018, 10, 27)])
def test_year_month_day(client, year: int, month: int, day: int):
    """Testing shows.year_month_day"""
    response = client.get(f"/shows/{year}/{month}/{day}")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


@pytest.mark.parametrize("year", [2018])
def test_year_all(client, year: int):
    """Testing shows.year_all"""
    response = client.get(f"/shows/{year}/all")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_all(client):
    """Testing shows.all"""
    response = client.get("/shows/all")
    assert response.status_code == 200
    assert b"All Show Details" in response.data
    assert b"show years" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_on_this_day(client):
    """Testing shows.on_this_day"""
    response = client.get("/shows/on-this-day")
    assert response.status_code == 200
    assert b"Show Details" in response.data
    assert b"On This Day" in response.data
    assert b"Location" in response.data
    assert b"Host" in response.data
    assert b"Scorekeeper" in response.data


def test_random(client):
    """Testing shows.random"""
    response = client.get("/shows/random")
    assert response.status_code == 302
    assert response.location


def test_recent(client):
    """Testing shows.recent"""
    response = client.get("/shows/recent")
    assert response.status_code == 302
    assert response.location
