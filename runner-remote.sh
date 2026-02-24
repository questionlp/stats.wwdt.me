#!/bin/sh
# Shell script used to start up Flask for local development and testing with
# remote access
#
# Requires a virtual environment (venv) created as venv and all
# dependencies installed.

FLASK_APP=app FLASK_DEBUG=1 FLASK_RUN_PORT=8000 venv/bin/flask run --host=0.0.0.0
