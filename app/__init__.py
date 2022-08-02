# -*- coding: utf-8 -*-
# vim: set noai syntax=python ts=4 sw=4:
#
# Copyright (c) 2018-2022 Linh Pham
# stats.wwdt.me is released under the terms of the Apache License 2.0
"""Core Application for Wait Wait Stats Page"""
from flask import Flask
from wwdtm import VERSION as WWDTM_VERSION

from app import config, dicts, utility
from app.errors import handlers
from app.guests.routes import blueprint as guests_bp
from app.hosts.routes import blueprint as hosts_bp
from app.locations.routes import blueprint as locations_bp
from app.main.routes import blueprint as main_bp
from app.main.redirects import blueprint as redirects_bp
from app.panelists.routes import blueprint as panelists_bp
from app.scorekeepers.routes import blueprint as scorekeepers_bp
from app.sitemaps.routes import blueprint as sitemaps_bp
from app.shows.routes import blueprint as shows_bp
from app.version import APP_VERSION


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Override base Jinja options
    app.jinja_options = Flask.jinja_options.copy()
    app.jinja_options.update({"trim_blocks": True, "lstrip_blocks": True})
    app.create_jinja_environment()

    # Register error handlers
    app.register_error_handler(404, handlers.not_found)
    app.register_error_handler(500, handlers.handle_exception)

    # Load configuration file
    _config = config.load_config()
    app.config["database"] = _config["database"]
    app.config["app_settings"] = _config["settings"]

    # Set up Jinja globals
    app.jinja_env.globals["app_version"] = APP_VERSION
    app.jinja_env.globals["wwdtm_version"] = WWDTM_VERSION
    app.jinja_env.globals["date_string_to_date"] = utility.date_string_to_date
    app.jinja_env.globals["current_year"] = utility.current_year
    app.jinja_env.globals["rank_map"] = dicts.PANELIST_RANKS
    app.jinja_env.globals["rendered_at"] = utility.generate_date_time_stamp

    app.jinja_env.globals["time_zone"] = app.config["app_settings"]["app_time_zone"]
    app.jinja_env.globals["ga_property_code"] = app.config["app_settings"][
        "ga_property_code"
    ]
    app.jinja_env.globals["api_url"] = app.config["app_settings"]["api_url"]
    app.jinja_env.globals["blog_url"] = app.config["app_settings"]["blog_url"]
    app.jinja_env.globals["graphs_url"] = app.config["app_settings"]["graphs_url"]
    app.jinja_env.globals["reports_url"] = app.config["app_settings"]["reports_url"]
    app.jinja_env.globals["site_url"] = app.config["app_settings"]["site_url"]

    # Register Jinja template filters
    app.jinja_env.filters["pretty_jsonify"] = utility.pretty_jsonify
    app.jinja_env.filters["markdown"] = utility.md_to_html

    # Register application blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(redirects_bp)
    app.register_blueprint(sitemaps_bp)
    app.register_blueprint(guests_bp, url_prefix="/guests")
    app.register_blueprint(hosts_bp, url_prefix="/hosts")
    app.register_blueprint(locations_bp, url_prefix="/locations")
    app.register_blueprint(panelists_bp, url_prefix="/panelists")
    app.register_blueprint(scorekeepers_bp, url_prefix="/scorekeepers")
    app.register_blueprint(shows_bp, url_prefix="/shows")

    return app
