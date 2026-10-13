# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Utility Functions."""

import pytest

from app.utility import format_social_account_name, format_social_network_icon


@pytest.mark.parametrize("network_slug", ["bluesky", "mastodon"])
def test_format_social_network_icon(network_slug: str):
    """Testing utility.format_social_network_icon."""
    _icon = format_social_network_icon(network_slug=network_slug)

    assert _icon, "No string was returned"
    assert _icon.startswith("bi-"), "String does not start with the bi- prefix"


@pytest.mark.parametrize("network_slug", ["tumblr", "unknown"])
def test_format_social_network_icon_unknown(network_slug: str):
    """Testing utility.format_social_network_icon for an unknown network."""
    _icon = format_social_network_icon(network_slug=network_slug)

    assert _icon, "No string was returned"
    assert _icon == "bi-link-45deg", "Incorrect icon name returned"


@pytest.mark.parametrize(
    "username, network_slug",
    [("username", "bluesky"), ("username", "instagram")],
)
def test_format_social_account_name_at_prefix(username: str, network_slug: str):
    """Testing utility.format_social_media_icon for an @-prefix."""
    _name = format_social_account_name(username=username, network_slug=network_slug)

    assert _name, "No string was returned"
    assert _name.startswith("@"), "Returned username does not include an @-prefix"


@pytest.mark.parametrize("username, network_slug", [("username", "reddit")])
def test_format_social_account_name_reddit(username: str, network_slug: str):
    """Testing utility.format_social_media_icon for a Reddit username."""
    _name = format_social_account_name(username=username, network_slug=network_slug)

    assert _name, "No string was returned"
    assert _name.startswith("u/"), "Returned username does not include an @-prefix"
