# Changes

## 5.1.0 (In Progress)

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
- Change `app.url_map.strict_slashes` from `False` to `True`

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
