# Copyright (c) 2018-2026 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Configuration Loading and Parsing for Wait Wait Stats Page."""

import copy
import json
from datetime import date
from pathlib import Path
from typing import Any

from app import utility

DEFAULT_RECENT_DAYS_AHEAD = 2
DEFAULT_RECENT_DAYS_BACK = 30

DEFAULT_URL_REDIRECTS: dict[str, dict[str, None]] = {
    "guests": {
        "slugs": None,
    },
    "hosts": {
        "slugs": None,
    },
    "locations": {
        "slugs": None,
    },
    "panelists": {
        "slugs": None,
    },
    "scorekeepers": {
        "slugs": None,
    },
    "shows": {
        "dates": None,
    },
}


def load_config(
    config_file_path: str = "config.json",
    connection_pool_size: int = 12,
    connection_pool_name: str = "wwdtm_stats",
    app_time_zone: str = "UTC",
) -> dict[str, dict[str, Any]]:
    """Read configuration and database settings."""
    _config_file_path = Path(config_file_path)
    with _config_file_path.open(mode="r", encoding="utf-8") as config_file:
        app_config = json.load(config_file)

    database_config = app_config.get("database", None)
    settings_config = app_config.get("settings", None)

    # Process database configuration settings
    if database_config:
        # Set database connection pooling settings if and only if there
        # is a ``use_pool`` key and it is set to True. Remove the key
        # after parsing through the configuration to prevent issues
        # with mysql.connector.connect()
        use_pool = database_config.get("use_pool", False)

        if use_pool:
            pool_name = database_config.get("pool_name", connection_pool_name)
            pool_size = database_config.get("pool_size", connection_pool_size)
            if pool_size < connection_pool_size:
                pool_size = connection_pool_size

            database_config["pool_name"] = pool_name
            database_config["pool_size"] = pool_size
            del database_config["use_pool"]
        else:
            if "pool_name" in database_config:
                del database_config["pool_name"]

            if "pool_size" in database_config:
                del database_config["pool_size"]

            if "use_pool" in database_config:
                del database_config["use_pool"]

    # Process time zone configuration settings
    time_zone = settings_config.get("time_zone", app_time_zone)
    time_zone_object, time_zone_string = utility.time_zone_parser(time_zone)
    settings_config["app_time_zone"] = time_zone_object
    settings_config["time_zone"] = time_zone_string
    database_config["time_zone"] = time_zone_string

    # Read in setting to override locations sorting
    settings_config["sort_by_venue"] = bool(settings_config.get("sort_by_venue", False))

    # Read in setting on whether to use decimal scores
    settings_config["use_decimal_scores"] = bool(
        settings_config.get("use_decimal_scores", False)
    )

    # Read in Umami Analytics settings
    if "umami_analytics" in settings_config:
        _umami = dict(settings_config["umami_analytics"])
        settings_config["umami"] = {
            "enabled": bool(_umami.get("enabled", False)),
            "url": _umami.get("url"),
            "website_id": _umami.get("data_website_id"),
            "auto_track": bool(_umami.get("data_auto_track", True)),
            "host_url": _umami.get("data_host_url"),
            "domains": _umami.get("data_domains"),
        }

        del settings_config["umami_analytics"]
    else:
        settings_config["umami"] = {
            "enabled": False,
        }

    # Read in setting on whether to display location map
    settings_config["display_location_map"] = bool(
        settings_config.get("display_location_map", False)
    )

    # Parse example objects
    _examples: dict[str, str] = settings_config.get("examples")
    examples = {}
    if _examples:
        examples["guest"] = _examples.get("guest", "stephen-colbert")
        examples["host"] = _examples.get("host", "josh-gondelman")
        examples["location"] = _examples.get(
            "location", "arlene-schnitzer-concert-hall-portland-or"
        )
        examples["panelist"] = _examples.get("panelist", "hari-kondabolu")
        examples["scorekeeper"] = _examples.get("scorekeeper", "bill-kurtis")
        _show_date: date = _examples.get("show", "2017-08-26")
        try:
            _date = date.fromisoformat(_show_date)
        except ValueError:
            _date = date(year=2017, month=8, day=26)
        finally:
            examples["show"] = _date

    settings_config["examples"] = examples

    return {
        "database": database_config,
        "settings": settings_config,
    }


def load_url_redirects(
    url_redirects_path: str = "url-redirects.json",
) -> dict[str, dict[str, str | None]]:
    """Read URL Redirect Settings."""
    _redirects = copy.deepcopy(DEFAULT_URL_REDIRECTS)
    _url_redirects_path = Path(url_redirects_path)
    if not _url_redirects_path.exists:
        return DEFAULT_URL_REDIRECTS

    with _url_redirects_path.open(mode="r", encoding="utf-8") as url_redirects_file:
        url_redirects: dict[str, dict[str, str | None]] = json.load(url_redirects_file)

    if "guests" in url_redirects:
        _redirects["guests"]["slugs"] = url_redirects["guests"].get("slugs")

    if "hosts" in url_redirects:
        _redirects["hosts"]["slugs"] = url_redirects["hosts"].get("slugs")

    if "locations" in url_redirects:
        _redirects["locations"]["slugs"] = url_redirects["locations"].get("slugs")

    if "panelists" in url_redirects:
        _redirects["panelists"]["slugs"] = url_redirects["panelists"].get("slugs")

    if "scorekeepers" in url_redirects:
        _redirects["scorekeepers"]["slugs"] = url_redirects["scorekeepers"].get("slugs")

    if "shows" in url_redirects:
        _redirects["shows"]["dates"] = url_redirects["shows"].get("dates")

    return _redirects
