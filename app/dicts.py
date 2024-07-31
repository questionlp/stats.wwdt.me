# Copyright (c) 2018-2024 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Dictionary objects used by the Wait Wait Stats Page."""
import mysql.connector

PANELIST_RANKS: dict[str, str] = {
    "1": "First",
    "1t": "First Tied",
    "2": "Second",
    "2t": "Second Tied",
    "3": "Third",
}


def postal_abbreviations(database_config: dict) -> dict:
    """Dictionary of postal abbrevations with state/province and country names."""
    database_connection = mysql.connector.connect(**database_config)
    cursor = database_connection.cursor(named_tuple=True)
    query = """
        SELECT postal_abbreviation, name, country
        FROM ww_postal_abbreviations
        ORDER BY postal_abbreviation ASC;
        """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    if not result:
        return {}

    abbreviations = {}
    for row in result:
        abbreviations[row.postal_abbreviation] = {
            "name": row.name,
            "country": row.country,
        }

    return abbreviations
