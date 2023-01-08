# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2023 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""pytest conftest.py File"""

import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
