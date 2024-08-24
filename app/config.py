# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Configuration Loading and Parsing for Wait Wait Stats Page."""
import json
from pathlib import Path
from typing import Any

from app import utility

DEFAULT_RECENT_DAYS_AHEAD = 2
DEFAULT_RECENT_DAYS_BACK = 30


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

    return {
        "database": database_config,
        "settings": settings_config,
    }
