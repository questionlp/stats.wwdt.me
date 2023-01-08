# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2023 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Location name formatting functions used by the Stats Page"""

from typing import Dict, Union


def format_location_name(location: Dict) -> Union[str, None]:
    """Returns a string with a combination of venue name, city
    and state, depending on what information is available"""

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
