# Changes

## 5.10.3

### Development Changes

- Upgrade black from 23.12.1 to 24.3.0

## 5.10.2

### Component Changes

- Upgrade wwdtm from 2.8.0 to 2.8.1, which includes fixing an issue of panelists not being sorted by their decimal scores properly

## 5.10.1

### Application Changes

- Add support for GitHub sponsorship link in the side pop-out nav, dropdown nav menu and in the footer by way of the `settings.github_sponsor_url` config key
- Change the how render and version information is rendered on screens with a width less than 1200px to align left rather than right

## 5.10.0

### Application Changes

- Add support for new show URL field from the Wait Wait Stats Database, which is used in place of the `/s/` redirect link if there is a value stored for a particular show
- Add support for Patreon link in the side pop-out nav, dropdown nav menu and in the footer by way of the `settings.patreon_url` config key

### Component Changes

- Upgrade wwdtm from 2.7.0 to 2.8.0

## 5.9.0

### Application Changes

- Add type hints for a majority of the return types for routes and utility modules
- Replace use of `typing.Optional` and `typing.Union` with the with the conventions documented in PEP-484 and PEP-604
- Change handling of `time_zone` configuration value to prevent use of `pytz.timezone()` in function arguments

### Component Changes

- Upgrade wwdtm from 2.6.1 to 2.7.0, which includes:
  - Upgrade numpy from 1.26.0 to 1.26.3
- Upgrade Markdown from 3.5.1 to 3.5.2

### Development Changes

- Switch to Ruff for code linting and formatting (with the help of Black)
- Upgrade pytest from 7.4.3 to 7.4.4
- Upgrade black from 23.11.0 to 23.12.1

### Documentation Changes

- Update the copyright block at the top of each file to remove `coding` line and to include the appropriate SPDX license identifier

## 5.8.1

### Component Changes

- Upgrade wwdtm from 2.6.0 to 2.6.1

## 5.8.0

### Application Changes

- Add support for rendering multiple Bluff the Listener segment results for a given show

### Component Changes

- Upgrade wwdtm from 2.5.0 to 2.6.0, which requires Wait Wait Stats Database version 4.4 or higher
- Upgrade Markdown from 3.4.3 to 3.5.1

## 5.7.2

### Application Changes

- Fix CSS for list and list item rendering within the show notes

## 5.7.1

### Application Changes

- Remove unneeded slash in an empty tag for the Materialize CSS include

## 5.7.0

**Starting with version 5.7.0, support for all versions of Python prior to 3.10 have been deprecated.**

### Application Changes

- Replace `dateutil.parser.parse` with `datetime.datetime.strptime`

### Component Changes

- Upgrade wwdtm from 2.4.0 to 2.5.0, which drops supports for Python versions prior to 3.10 and includes:
  - Upgrade MySQL Connector/Python from 8.0.33 to 8.2.0
  - Upgrade numpy from 1.24.4 to 1.26.0

### Development Changes

- Upgrade black from 23.10.1 to 23.11.0
- Remove `py38` and `py39` from `tool.black` in `pyproject.toml`

## 5.6.0

### Component Changes

- Upgrade Flask from 2.3.2 to 3.0.0
- Upgrade gunicorn from 20.1.0 to 21.2.0

### Development Changes

- Upgrade pycodestyle from 2.11.0 to 2.11.1
- Upgrade pytest from 7.4.0 to 7.4.3
- Upgrade black from 23.7.0 to 23.10.1

## 5.5.1

### Component Changes

- Upgrade wwdtm from 2.3.0 to 2.4.0

## 5.5.0

### Application Changes

- Add support for displaying panelist Lightning Fill-in-the-Blank starting score and correct answers stored in the corresponding new table columns. This is handled via version 2.3.0 of the `wwdtm` library and depends on setting the `use_decimal_scores` setting in the `config.json` application configuration file.

### Component Changes

- Upgrade wwdtm from 2.2.0 to 2.3.0

## 5.4.0

### Application Changes

- Add support for displaying panelist decimal scores stored in a new table column in the Wait Wait Stats Database instead of the standard integer scores. This is handled via version 2.2.0 of the `wwdtm` library and a new `use_decimal_scores` setting in the `config.json` application configuration file. By default, the value will be set to `false` and must be changed to `true`, and the appropriate changes have been deployed to the Wait Wait Stats Database.
- Increase the number of digits displayed after the decimal point for certain panelist statistics from 4 to 5

### Component Changes

- Upgrade wwdtm from 2.1.0 to 2.2.0, which also includes:
  - Upgrade NumPy from 1.23.2 to 1.24.3

### Development Changes

- Upgrade black from 23.3.0 to 23.7.0
- Upgrade flake8 from 6.0.0 to 6.1.0
- Upgrade pycodestyle from 2.10.0 to 2.11.0
- Upgrade pytest from 7.3.1 to 7.4.0

## 5.3.1

### Application Changes

- Revamping of the formatting and styles when printing pages from the site to reduce wasted whitespace and other tweaks, including:
  - Adding site title at the top of the document
  - Update the guest, host, location, panelist, scorekeeper and show info blocks to mimic a two-column layout
  - Change the `main` block to not cause the footer to be pushed to a new page
  - Render the collection lists in a more compact manner
  - Correct a few `color` values for a few types of links

## 5.3.0

### Application Changes

- Add `settings.sort_by_venue` configuration setting that is used to determine whether to sort the locations by venue name or by state and city for the `/locations`. Defaults to `false`, which matches the previous behavior.

### Component Changes

- Upgrade Flask from 2.2.3 to 2.3.2
- Upgrade wwdtm from 2.0.9 to 2.1.0

## 5.2.4

### Component Changes

- Upgrade wwdtm from 2.0.8 to 2.0.9, which also includes the following changes:
  - Upgrade MySQL Connector/Python from 8.0.31 to 8.0.33
  - Upgrade NumPy from 1.23.4 to 1.24.2
  - Upgrade python-slugify from 6.1.2 to 8.0.1
  - Upgrade pytz from 2022.6 to 2023.3
- Upgrade Markdown from 3.4.1 to 3.4.3
- Removed python-dateutil as an explicit requirement as it is being pulled in by the wwdtm package

### Development Changes

- Move pytest configuration from `pytest.ini` into `pyproject.toml`
- Upgrade flake8 from 5.0.4 to 6.0.0
- Upgrade pycodestyle from 2.9.1 to 2.10.0
- Upgrade pytest from 7.2.0 to 7.3.1
- Upgrade black from 22.10.0 to 23.3.0

## 5.2.3

### Component Changes

- Upgrade Materialize from 1.2.1 to 1.2.2

## 5.2.2

### Component Changes

- Upgrade Flask from 2.2.2 to 2.2.3
- Upgrade Werkzeug from 2.2.2 to 2.2.3 to fix a security vulnerability

## 5.2.1

### Other Changes

- Updating copyright year for code files under `tests`

## 5.2.0

### Component Changes

- Upgrade Materialize from 1.1.0 to 1.2.1

### Other Changes

- Updating copyright year for all code files and add copyright block to `static/css/style.css` and `static/js/init.js`

## 5.1.5

### Application Changes

- Continue refactoring how application and database connection settings are loaded and setting default values

### Component Changes

- Upgrade wwdtm from 2.0.7 to 2.0.8, which also includes the following changes:
  - Upgrade MySQL Connector/Python from 8.0.30 to 8.0.31
  - Upgrade NumPy from 1.23.2 to 1.23.4
  - Upgrade python-slugify from 5.0.2 to 6.1.2
  - Upgrade pytz from 2022.2.1 to 2022.6
- Upgrade Flask from 2.2.0 to 2.2.2
- Upgrade Werkzeug from 2.2.1 to 2.2.2

### Development Changes

- Upgrade flake8 from 4.0.1 to 5.0.4
- Upgrade pycodestyle from 2.8.0 to 2.9.1
- Upgrade pytest from 7.1.2 to 7.2.0
- Upgrade black from 22.6.0 to 22.10.0

## 5.1.4

### Application Changes

- Update the URL in footer to use HTTPS instead of HTTP
- Use `dict.get(key, default_value)` in `app/__init__.py` to get/set configuration values in order to avoid application startup errors if configuration keys are not set.
  - Default value for `time_zone` is `UTC`
  - Default values for any URL is an empty string
- Adding `mastodon_url` and `mastodon_user` configuration keys in the `settings` section of the config file.
- If the `mastodon_url` and `mastodon_user` keys contain a value, insert a link with `rel="me"` attribute for profile link validation.

## 5.1.3

### Bugfix

- Fix an issue where the `time_zone` configuration value was being assigned to `settings_config` twice, instead of being assigned to both `settings_config` and `database_config`

## 5.1.2

### Component Changes

- Upgrade wwdtm from 2.0.5 to 2.0.7, which also includes the following changes:
  - Upgrade MySQL Connector/Python from 8.0.28 to 8.0.30
  - Upgrade NumPy from 1.22.3 to 1.23.2
  - Upgrade pytz from 2022.1 to 2022.2.1

## 5.1.1

### Component Changes

- Upgrade Flask to 2.2.0

## 5.1.0

### Component Changes

- Upgrade Werkzeug from 2.1.2 to 2.2.1
- Upgrade Markdown from 3.3.6 to 3.4.1

### Application Changes

- Relocate templates from under `app/templates` to the newly created
  `templates` directory within each section (e.g.: `app/shows/templates/shows`)
  - The templates directory structure will match the new Blueprints structure
    used in [reports.wwdt.me_v2](https://github.com/questionlp/reports.wwdt.me_v2)
- Update guests, hosts, locations, panelists, scorekeepers and shows routes
  and redirects so that canonical routes now have a trailing slash and requests
  made without a trailing slash will get redirected

### Development Changes

- Upgrade pytest from 6.2.5 to 7.1.2
- Add type hinting to pytest scripts
- Upgrade Black from 22.1.0 to 22.6.0
- Change Black `target-version` to remove `py36` and `py37`, and add `py310`

## 5.0.4

### Component Changes

- Upgrade Materialize from 1.1.0-alpha to 1.1.0
- Upgrade Flask from 2.1.1 to 2.1.3
- Set Werkzeug version to 2.1.2
  - Version 2.2.0 includes a breaking change regarding route parsing and handling

## 5.0.3

### Component Changes

- Upgrade wwdtm from 2.0.2 to 2.0.5
- Upgrade Flask from 2.0.2 to 2.1.1
- Upgrade pytz from 2021.3 to 2022.1

## 5.0.2

### Application Changes

- Change "API Docs" links on the site to read "API"

## 5.0.1

### Application Changes

- Update the Site History page to include version 5.0
- Update the link to the GitHub repository

## 5.0.0

### Component Changes

- Replace (lib)wwdtm 1.2.x with wwdtm 2.0.2
- Upgrade Flask from 2.0.1 to 2.0.2
- Upgrade Materialize from 1.0.0 to 1.1.0-alpha

### Application Changes

- Complete restructuring of the Flask application to use Blueprints
  design pattern
- Convert the application from using uWSGI to serve the application to
  Gunicorn to match the changes made with the Wait Wait Stats API

### Development Changes

- Adding tests by way of `pytest`
