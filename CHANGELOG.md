# Changes

## 5.1.0

### Component Changes

- Upgrade Materialize from 1.1.0-alpha to 1.1.0

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

- Complete restructuring of the Flask application to use Blueprints design
  pattern
- Convert the application from using uWSGI to serve the application to
  Gunicorn to match the changes made with the Wait Wait Stats API

### Development Changes

- Adding tests by way of `pytest`
