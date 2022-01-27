# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Locations Routes for Wait Wait Stats Page"""
from flask import Blueprint

blueprint = Blueprint("locations", __name__)


@blueprint.route("/")
def index():
    return "Location Index"


@blueprint.route("/<string:location_slug>")
def details(location_slug: str):
    return f"Details: {location_slug}"


@blueprint.route("/all")
def all():
    return "Details: All Locations"


@blueprint.route("/random")
def random():
    return "Details: Random"
