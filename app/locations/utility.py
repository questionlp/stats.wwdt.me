# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Location name formatting functions used by the Stats Page."""
from decimal import Decimal
from math import copysign, floor


def decimal_to_degrees(decimal_value: Decimal) -> tuple[Decimal, Decimal, Decimal]:
    """Converts decimal coordinate to degrees.

    Adapted from LatLon23: https://github.com/NOAA-ORR-ERD/lat_lon_parser
    """
    degrees, remainder = divmod(abs(decimal_value), 1)
    minutes, remainder = divmod(remainder * 60, 1)

    return copysign(degrees, decimal_value), minutes, remainder * 60


def format_latitude(degrees: Decimal, minutes: Decimal, seconds: Decimal) -> str:
    """Formats latitude tuple as a string."""
    n_degrees = f"{floor(abs(degrees))}"
    n_minutes = f"{floor(minutes)}"
    n_seconds = f"{floor(seconds)}"

    if degrees > 0:
        return f"{n_degrees}&deg; {n_minutes}&prime; {n_seconds}&Prime; N"
    elif degrees == 0:
        return f"{n_degrees}&deg; {n_minutes}&prime; {n_seconds}&Prime;"
    else:
        return f"{n_degrees}&deg; {n_minutes}&prime; {n_seconds}&Prime; S"


def format_longitude(degrees: Decimal, minutes: Decimal, seconds: Decimal) -> str:
    """Formats longitude tuple as a string."""
    n_degrees = f"{floor(abs(degrees))}"
    n_minutes = f"{floor(minutes)}"
    n_seconds = f"{floor(seconds)}"

    if degrees > 0:
        return f"{n_degrees}&deg; {n_minutes}&prime; {n_seconds}&Prime; E"
    elif degrees == 0:
        return f"{n_degrees}&deg; {n_minutes}&prime; {n_seconds}&Prime;"
    else:
        return f"{n_degrees}&deg; {n_minutes}&prime; {n_seconds}&Prime; W"


def format_location_name(location: dict, state_name: str = None) -> str | None:
    """Formats a location's name."""
    if not location:
        return None

    if "venue" not in location and "city" not in location and "state" not in location:
        return None

    if location["state"] and state_name:
        state = state_name if state_name else location["state"]
    elif location["state"]:
        state = location["state"]
    else:
        state = None

    if location["venue"] and location["city"] and state:
        return "{} ({}, {})".format(location["venue"], location["city"], state)
    elif location["venue"] and (not location["city"] and not state):
        return location["venue"]
    elif location["city"] and location["state"] and not location["venue"]:
        return "({}, {})".format(location["city"], state)
    elif location["city"] and not state:
        return location["city"]
