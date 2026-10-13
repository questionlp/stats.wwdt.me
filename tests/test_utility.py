# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Utility Functions."""

import pytest

from app.utility import format_social_account_name, format_social_network_icon


@pytest.mark.parametrize("network_slug", ["bluesky", "reddit", "tumblr"])
def test_format_social_network_icon(network_slug: str):
    """Testing utility.format_social_network_icon."""
    _icon = format_social_network_icon(network_slug=network_slug)

    assert _icon, "No string was returned"
    assert _icon.startswith("bi-"), "String does not start with the bi- prefix"


@pytest.mark.parametrize(
    "username, network_slug",
    [("username", "bluesky"), ("username", "reddit"), ("username", "tumblr")],
)
def test_format_social_account_name(username: str, network_slug: str):
    """Testing utility.format_social_media_icon."""
    _name = format_social_account_name(username=username, network_slug=network_slug)

    assert _name, "No string was returned"
