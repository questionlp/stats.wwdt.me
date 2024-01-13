# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Error Handlers Module for Wait Wait Stats Page."""
from typing import Literal

from flask import render_template


def not_found(error) -> tuple[str, Literal[404]]:
    """Handle resource not found conditions."""
    return render_template("errors/404.html", error_description=error.description), 404


def handle_exception(error) -> tuple[str, Literal[500]]:
    """Handle exceptions in a slightly more graceful manner."""
    _ = error
    return render_template("errors/500.html"), 500
