# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Location name formatting functions used by the Stats Page."""


def format_location_name(location: dict) -> str | None:
    """Formats a location's name."""
    if not location:
        return None

    if "venue" not in location and "city" not in location and "state" not in location:
        return None

    if location["venue"] and location["city"] and location["state"]:
        return "{} ({}, {})".format(
            location["venue"], location["city"], location["state"]
        )
    elif location["venue"] and (not location["city"] and not location["state"]):
        return location["venue"]
    elif location["city"] and location["state"] and not location["venue"]:
        return "({}, {})".format(location["city"], location["state"])
    elif location["city"] and not location["state"]:
        return location["city"]
