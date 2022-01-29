# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Error Handlers Module for Wait Wait Stats Page"""
from flask import render_template
from werkzeug.exceptions import HTTPException


def not_found(error):
    """Handle resource not found conditions"""
    return render_template("errors/404.html",
                           error_description=error.description), 404


def handle_exception(error):
    """Handle exceptions in a slightly more graceful manner"""
    # Pass through any HTTP errors and exceptions
    if isinstance(error, HTTPException):
        return error

    # Handle everything else with a basic 500 error page
    return render_template("errors/500.html"), 500
