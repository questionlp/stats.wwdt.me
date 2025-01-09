# Copyright (c) 2018-2025 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Errors Module and Blueprint Views."""
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_not_found(client: FlaskClient) -> None:
    """Testing errors.not_found."""
    response: TestResponse = client.get("/host/peter-seagull")
    assert response.status_code == 404
    assert b"Not Found" in response.data
