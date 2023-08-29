# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2023 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Configuration Loading and Parsing for Wait Wait Stats Page"""
import json
from typing import Any, Dict

from app import utility

DEFAULT_RECENT_DAYS_AHEAD = 2
DEFAULT_RECENT_DAYS_BACK = 30


def load_config(
    config_file_path: str = "config.json",
    connection_pool_size: int = 12,
    connection_pool_name: str = "wwdtm_stats",
    app_time_zone: str = "UTC",
) -> Dict[str, Dict[str, Any]]:
    with open(config_file_path, "r") as config_file:
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

    return {
        "database": database_config,
        "settings": settings_config,
    }
