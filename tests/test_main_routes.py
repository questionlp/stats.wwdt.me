# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Testing Main Routes Module and Blueprint Views"""


def test_index(client):
    """Testing main.index"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Wait Wait" in response.data
    assert b"DB ID:" in response.data


def test_robots_txt(client):
    """Testing main.robots_txt"""
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert b"Sitemap:" in response.data
    assert b"User-agent:" in response.data


def test_about(client):
    """Testing main.about"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Overview" in response.data
    assert b"Source Code" in response.data


def test_site_history(client):
    """Testing main.site_history"""
    response = client.get("/site-history")
    assert response.status_code == 200
    assert b"Versions 1 and 2" in response.data
    assert b"Version 4" in response.data
