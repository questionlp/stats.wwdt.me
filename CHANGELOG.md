# Changes

## 6.10.0

### Application Changes

- Cleaned up the "Appearances: Regular Shows" and "Appearances: All Shows" labels in the Not My Job Guest, Host, Location, Panelist and Scorekeeper details pages
  - The entire label now has a Bootstrap tooltip that displays a note when hovering over the full label text
  - Removed the dotted line under "Regular Shows" and "All Shows"
  - Removed the opening and closing parentheses around "Regular Shows" and "All Shows"
  - Added an info icon at the end of the label to indicate that there is additional information available
- Changed the Coordinates block in the Location details page
  - Removed the dotted line under the location's coordinates
  - Added an info icon after the coordinates to indicate that there is additional information available (DMS coordinates)
  - Added a left border to the span containing the "Location Map" link
  - Switched the location of the map icon from before to after the "Location Map" text for consistency with the other info icons
- Moved towards standardizing on a font weight of 600 for all headers, subheaders and bottom navigation links
  - Prior to this update, both 500 and 600 font weights were used
  - This matches the [recommended font weights](https://carbondesignsystem.com/elements/typography/overview/#weights) defined in the [Carbon Design System](https://carbondesignsystem.com/)
- Changed the sans-serif, serif and monospace font stacks based on the [font stack](https://carbondesignsystem.com/elements/typography/overview/#typeface:-ibm-plex) defined in the Carbon Design System
  - sans-serif: `"IBM Plex Sans", "Helvetica Neue", system-ui, -apple-system, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji"`
  - serif: `"IBM Plex Serif", "Georgia", Times, serif, "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji"`
  - monospace: `"IBM Plex Mono", "Menlo", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", Courier, "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", monospace`
- Added a little spacing between the panelist total score and the starting score and questions answered correctly amount, if available
- Updated the visually hidden text for panelist scores to provide better context for screen readers and parsers
- Changed the panelist rank in the Panelist details page from being text enclosed in square brackets to be a badge

### Component Changes

- Upgrade wwdtm-theme from 2.1.1 to 2.2.4

## 6.9.0

### Application Changes

- Added new badges to Not My Job Guest, Host, Panelist and Scorekeeper details pages that notes if they have been on the show as another role (for example: a panelist who has also been a scorekeeper) with a link to the corresponding details page
  - The new badges do not have a special background color, but have a border to differentiate those badges from other badges
  - How that is determined by the [Wait Wait Stats Library](https://docs.wwdt.me/) is if the slug string matches the slug string for another role
  - The slug string for the same person for each of their roles should match, but it is not 100% guaranteed based on how their data was originally captured

### Component Changes

- Upgrade wwdtm from 2.19.0 to 2.20.0
  - Includes upgrading NumPy from 2.1.2 to 2.2.6
- Upgrade wwdtm-theme from 2.1.0 to 2.1.1

### Development Changes

- Upgrade Ruff from 0.11.9 to 0.12.8
- Upgrade pytest from 8.3.5 to 8.4.1
- Upgrade pytest-cov from 6.1.1 to 6.2.1

## 6.8.0

### Application Changes

- Added a retro-inspired "middle" mode theme that was added to version 2.1.0 of [wwdtm-theme](https://github.com/questionlp/wwdtm-theme)
  - The idea to create the theme was sparked by a Veronica Explains [post on Mastodon](https://linuxmom.net/@vkc/114944265497880449) made wanting to see light/middle/dark mode website designs
  - The new color theme is built around the limited color palettes and serif fonts that were commonly used to render web pages in the mid to late-1990s, specifically Netscape 2 and 3 on classic Macintosh and Windows 3.x.
  - The limited set of colors were the basic named colors from [HTML 3.2](https://www.w3.org/TR/2018/SPSD-html32-20180315/) and the 216-color "[web-safe](https://en.wikipedia.org/wiki/Web_colors#Web-safe_colors)" palette.
  - The page background color, `#c0c0c0`, comes from the page and window background color used by Netscape Navigator 2 and 3 on classic Macintosh computers and on Windows 3.x
  - Page elements, including the navbar, footer, off-canvas side navigation changed to use similar colors available from the "web-safe" color palette
  - The new theme uses "IBM Plex Serif" as the primary font family, instead of "IBM Plex Sans". Fallback font families are set to "Times", "Times New Roman" and the "serif" generic.
- Added "Retro" option in the color theme selection dropdown in the navbar and off-canvas side navigation
- Changed Bootstrap tooltips to use a custom `ww-tooltip` class for the "Retro" color theme

### Component Changes

- Added IBM Plex Serif web font files
- Upgrade wwdtm-theme from 2.0.28 to 2.1.0

## 6.7.7

### Application Changes

- Add visually hidden "Start" and "Correct" text before the corresponding panelist scoring information in both show and panelist details to provide additional context for screen readers and parsers
- Changed the disclaimer in the footer to be inside a collapsible container with an info icon at the end of the copyright and contact line acting as a button to toggle the collapsible
  - This change was done to make the footer more minimal in its default state

### Component Changes

- Upgrade wwdtm-theme from 2.0.26 to 2.0.28
  - Increase line height for host and scorekeeper names from the default 1.5 to 1.625
  - Increase panelist and guest lists from 1.75 to 2

## 6.7.6

### Application Changes

- Discreetly display the node rendering and serving the page as a tooltip in the footer

## 6.7.5

### Component Changes

- Upgrade wwdtm-theme from 2.0.24 to 2.0.26
  - Increased line height for the `.footer.links` across the board

## 6.7.4

### Component Changes

- Upgrade wwdtm-theme from 2.0.23 to 2.0.24
  - Increased line height for the `.footer.links` on smaller screens from 2 to 2.6

## 6.7.3

### Component Changes

- Upgrade wwdtm-theme from 2.0.20 to 2.0.23
  - Increases line height for the `.footer.links` on smaller screens to make it easier to tap or click specific links when the text is wrapped

## 6.7.2

### Application Changes

- Swap position of the "Support NPR" link in the footer to match the ordering used on the [Wait Wait Reports Site](https://reports.wwdt.me/) and the upcoming version of the [Wait Wait Graphs Site](https://graphs.wwdt.me/)

## 6.7.1

### Application Changes

- Updated handling of Not My Job Guest score exception in both Shows and Guests details pages so that the `<span>` for the score exception only appears when there is a score exception. Previously, an empty `<span>` was needlessly rendered for all guest score entries
- - Add `support_npr_url` to the `app_settings` section in the `config.json` file
- Display link to "Support NPR" in the pop-out side navigation and in the footer with the value from `support_npr_url`, if not blank or `None`

## 6.7.0

### Application Changes

- Fix the breadcrumb link for "Shows" for the individual show page so that it properly points to the Shows index page
- Adding `<link rel="canonical">` header to all pages under the Shows section
- Adding a new info page titled "Understanding Wait Wait Stats Page Data" that provides information on badges, panelist ranking, scoring exceptions and other terminology used in the Wait Wait Stats Page
- Add `exclude_description` and `exclude_notes` flags to the individual show details template in order to exclude the sections when the template is used outside of the Show section
- Add `exclude_guest_appearances`, `exclude_host_appearances`, `exclude_panelist_appearances` and `exclude_scorekeeper_appearances` flag to the respective details templates and `exclude_location_recordings` flag to the location details template in order to exclude the section when the template is used outside of each section
- Add `examples` configuration object within `app_settings` in the `config.json` file with `guest`, `host`, `location`, `panelist`, and `show` keys used to configure which example data to be used in the "Understanding Wait Wait Stats Page Data" page. Not all are used in the info page, but are available if needed. The following are the default values:
  - **guest:** `stephen-colbert`
  - **host:** `josh-gondelman`
  - **location:** `arlene-schnitzer-concert-hall-portland-or`
  - **panelist:** `hari-kondabolu`
  - **scorekeeper:** `bill-kurtis`
  - **show:** `2017-08-26`
- Change "Return to Year List" link on Shows: All page to be right-aligned instead of left-aligned
- Replace underscores with hyphens in HTML template file names

### Component Updates

- Upgrade wwdtm-theme from 2.0.5 to 2.0.20
  - Upgrade Bootstrap from 5.3.6 to 5.3.7
  - Includes an update to make the footer link list items display as `inline-block` instead of `inline` to prevent line breaks within list items
  - Add `.static-section` to allow for more semantic granularity versus `.static-page`
  - Change `$h5-font-size` from `$font-size-base` to `$font-size-base * 1.125`
  - Add styling for new table of contents block

## 6.6.5

### Application Changes

- Update the Markdown to HTML filter to modify generated external links to open in a new window/tab and add the `bi-box-arrow-up-right` icon at the end of the link text
- Update list of AI scraper user agents
- Change the `block_ai_scrapers` logic so that if the configuration key is set to `true`, the action is set to `Disallow: /`. If the configuration key is set to `false`, the action is set to `Crawl-delay: 10`

## 6.6.4

### Application Changes

- Fixed a bug in the `/shows/random/<int:year>` route where the database connection close command was not moved to the correct location
- Change `/shows/random` and `/shows/random/<int:year>` to use the new `wwdtm.show.Show.retrieve_random_date_object()` and `wwdtm.show.Show.retrieve_random_date_object_by_year()` methods

### Component Changes

- Upgrade wwdtm from 2.18.2 to 2.19.0

## 6.6.3

### Application Changes

- Change the `/shows/random` route to redirect using `shows.year_month_day` rather than `shows.date_string`
  - Example: Instead of the route returning `/shows/2018-10-27`, the route will return `/shows/2018/10/27`
  - The route will use the `shows.date_string` route as a fallback option
  - If no random date should be pulled from the database, redirect to the Shows index page

## 6.6.2

### Component Changes

- Upgrade Flask from 3.1.0 to 3.1.1

## 6.6.1

### Application Changes

- Set NPR badge links and external links (including Wait Wait Graphs, Wait Wait Reports and Wait Wait Stats API) to open in a new window/tab
- Use `bi-box-arrow-up-right` icon to denote external links
- Add `bluesky_url` and `bluesky_user` configuration to display Bluesky account information
- Add contact information to the About page

### Component Changes

- Upgrade wwdtm from 2.18.1 to 2.18.2
- Upgrade wwdtm-theme from 2.0.0 to 2.0.5
  - Upgrade Bootstrap from 5.3.5 to 5.3.6
  - Upgrade Bootstrap Icons from 1.11.3 to 1.13.1

### Development Changes

- Upgrade ruff from 0.9.6 to 0.11.9
- Upgrade pytest from 8.3.3 to 8.3.5
- Upgrade pytest-cov from 5.0.0 to 6.1.1

## 6.6.0

Due to the significant changes around the new application theming, the usual Application, Component and Development changes section are being merged into a single Changes section.

### Changes

- Complete re-work of the application theme structure and how theme assets are deployed
  - `scss` submodule has been replaced by `wwdtm-theme`
  - `wwdtm-theme` now handles the compiling of the Sass files to CSS into `dist/css` and copies the Bootstrap scripts into `dist/js`
- Trimming down the included `package.json` to only require `@ibm/plex-mono` and `@ibm/plex-sans`
- NPM scripts have been simplified to copy the required CSS and JS files from `wwdtm-theme` and the required IBM Plex web font files into the appropriate paths under `app/static`
- Add Best Of Shows, Repeat Best Of Shows and Repeat Shows by Year views for Shows
- Upgrade wwdtm from 2.17.2 to 2.18.1

## 6.5.6

### Application Changes

- Fixed issue where the location map was not rendering due to changes made in version 6.5.5

## 6.5.5

### Application Changes

- Relocate the Bootstrap and application code initialization from towards the end of the document to the head to prevent background flashing on page loads when in dark mode
- Corrected Umami Analytics include for error page template
- Update Bootstrap icon classes to include `.bi`

### Component Changes

- Set Jinja2 version to `~=3.1.6`

## 6.5.4

### Application Changes

- Fix: Change hover color for the Repeat show badge for `prefers-color-scheme: dark` to make the link text readable against the light badge background color

## 6.5.3

### Application Changes

- Update list of AI bots from <https://github.com/ai-robots-txt/ai.robots.txt> in the default `robots.txt`

### Development Changes

- Upgrade ruff from 0.9.3 to 0.9.6

## 6.5.2

### Component Changes

- Upgrade wwdtm from 2.17.1 to 2.17.2

## 6.5.1

### Component Changes

- Upgrade wwdtm from 2.17.0 to 2.17.1

## 6.5.0

### Application Changes

- Migrate random guest, host, location, panelist, scorekeeper and show routes to use the new corresponding methods in the `wwdtm` library.
- Add the ability to get a random show for a given year
- Add additional exception handling for show routes that have URL parts expecting integer values
- Clean up database connections within `try/except/finally` blocks

### Component Changes

- Upgrade wwdtm from 2.15.0 to 2.17.0

## 6.4.1

### Application Changes

- Fix an issue where "Home/Remote Studios" location was not appearing in the Locations page due to an issue that was found in the `wwdtm` library.

### Component Changes

- Upgrade wwdtm from 2.14.0 to 2.15.0

### Development Changes

- Upgrade ruff from 0.9.2 to 0.9.3
- Remove black from required development packages as part of migrating entirely to Ruff

## 6.4.0

### Application Changes

- Implementing [HTTP 418](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418)

## 6.3.1

### Application Changes

- Change the ordering of database ID and pronoun badges for hosts and panelists to match the correct ordering used for scorekeepers

### Development Changes

- Upgrade ruff from 0.7.4 to 0.9.2

## 6.3.0

### Application Changes

- Add fuzzy matching for panelist slugs in the `panelists.details` route. The fuzzy matching slugifies the input `panelist_slug` value and compares it against the list of all panelist slugs.

  If the slugified value matches a valid panelist slug and the slugified value does not match the original `panelist_slug` value, then redirect the user to the correct path for the panelist. If there isn't a match, then redirect the user to `panelists.index`.

  The extra check between the slugified `panelist_slug` value against the request's `panelist_slug` is to prevent the chance of an infinite redirect loop from happening.

  For example, if the user requests `/panelists/Luke%20Burbank` will match the slugified value of `Luke%20Burbank` to `luke-burbank` and redirects the user to `/panelists/luke-burbank`. However, if the user requests `/panelists/Luke%20Burbonk`, there won't be a match and redirects the user to `/panelists`.
- Similar updates to the corresponding guests, hosts and scorekeepers routes have also been made.
- Add testing for the new slug fuzzy matching redirects for guests, hosts, panelists and scorekeepers.

### Component Updates

- Upgrade Flask from 3.0.3 to 3.1.0
- Upgrade Markdown from 3.5.2 to 3.7.0

### Development Changes

- Added test for `errors.not_found`

## 6.2.5

### Application Changes

- Fix issues with incorrect parameter names in redirects for `shows.year_month` and `shows.year_month_day` which cause errors
- Update copyright dates from 2024 to 2025

## 6.2.4-post.1

### Component Changes

- Upgrade nanoid from 3.3.7 to 3.3.8 to fix a security vulnerability for a package required to compile, minify and copy generated CSS files

## 6.2.4

### Application Changes

- Update `wwdtm-theme` to set font weight for header and footer navigation links to `500`
- Tweak responsive font sizing for `root` in `wwdtm-theme` with a range of 14.5px and 16.75px

## 6.2.3

### Application Changes

- Re-add responsive font sizing for `:root` in `wwdtm-theme` with a range of 14px and 16.5px

## 6.2.2

### Application Changes

- Remove responsive font sizing for `:root` in `wwdtm-theme`

### Development Changes

- Upgrade ruff from 0.7.0 to 0.7.4

## 6.2.1

### Application Changes

- Rename "Best Of Repeats" to "Repeat Best Ofs" pages and routes
- Add a redirect for `/shows/best-of-repeats` to point to `/shows/repeat-best-ofs`

### Component Changes

- Upgrade wwdtm from 2.13.0 to 2.14.0

### Development Changes

- Add missing tests for Best Of, Repeat Best Of and Repeat Shows pages

## 6.2.0

### Application Changes

- Adding Best Of, Best Of Repeat and Repeat Shows pages
- Initial support for Python 3.13

### Component Changes

- Upgrade wwdtm from 2.12.1.post0 to 2.13.0

### Development Changes

- Upgrade black from 24.8.0 to 24.10.0
- Upgrade ruff from 0.6.9 to 0.7.0
- Increase minimum pytest version from 8.0 to 8.3 in `pyproject.toml`
- Add `py313` to `tool.black.target-version`

## 6.1.0

### Application Changes

- Replace all references of `named_tuple=` in database cursors to `dictionary=` due to cursors using `NamedTuple` being marked for deprecation in future versions of MySQL Connector/Python

### Component Changes

- Upgrade wwdtm from 2.11.0 to 2.12.1.post0

### Development Changes

- Upgrade black from 24.4.2 to 24.8.0
- Upgrade pytest from 8.1.2 to 8.3.3
- Upgrade ruff from 0.6.7 to 0.6.9
- Add initial pytest coverage reporting using `pytest-cov`, which can be generated by running: `pytest --cov=app tests/`

## 6.0.2

### Application Changes

- Fix ordering of locations due to a bug found in `wwdtm` version 2.10.1
- Change ordering of locations for `/locations/all` to respect the value of `settings.sort_by_venue` in `config.json`
- Fix issue where "N/A" is not shown when a location does not have any recordings

### Component Changes

- Upgrade wwdtm from 2.10.1 to 2.11.0

### Development Changes

- Upgrade ruff from 0.5.1 to 0.6.7

## 6.0.1-post0

### Application Changes

- This non-release does not include any application changes. The version number presented by the application will still be [6.0.1](https://github.com/questionlp/stats.wwdt.me/releases/tag/v6.0.1).

### Development Changes

- Removal of the `serve` NPM package as it is not used and one of its dependencies requires a package that has a [high severity vulnerability](https://github.com/advisories/GHSA-9wv6-86v2-598j).

## 6.0.1

### Application Changes

- Fix an error caused by checking the wrong variable for `panelists.routes.details()`
- Update generated Bootstrap CSS with latest changes

### Development Changes

- Set `max-locals` to 20 for Pylint

## 6.0.0-post0

### Application Changes

- This non-release does not include any application changes. The version number presented by the application will still be [6.0.0](https://github.com/questionlp/stats.wwdt.me/releases/tag/v6.0.0).

### Development Changes

- Contents of the `scss` directory has now been migrated to a new Git repository, [wwdtm-themes](https://github.com/questionlp/wwdtm-themes) and `scss` is now a Git submodule reference.

## 6.0.0

### Application Changes

- Frontend code refactor due to switching from Materialize to Bootstrap
  - Replacing Materialize frontend toolkit with Bootstrap
  - Replacing Materialize Icons with Bootstrap Icons
  - Refactor the frontend structure to use Bootstrap frontend components and conventions
  - Include the required IBM Plex web fonts with the application to remove use of Google Fonts
- User interface changes
  - Change the behavior of the main navigation to combine navigation links into a single list that are listed in the top navbar on `xl` screen size or in an off-canvas side nav on smaller screens
  - Improve legibility and readability in font size changes and increased color contrast when using the dark mode color theme
  - Include a color theme toggle in the main navigation to allow the reader to switch the theme on-the-fly
  - Remove the rightwards arrow included after links in the main section of the page
  - Change wording of Appearances and Recordings in respective details pages and provide additional information via Bootstrap tooltip
  - Add Bootstrap tooltip to Not My Job guest scoring exception marker
  - Render show description and notes text as Markdown
  - De-emphasize the DB ID badge by changing the background color to blend in, instead of contrasting, with the background
  - Remove "Home" from all navigational breadcrumbs
  - Remove zero-padded dates from navigational breadcrumbs
- Fix warnings and errors reported by pylint
- Fix an issue where `use_decimal_scores` was not being passed through to the recent shows view
- Add an experimental `block_ai_scrapers` config key that will block known AI scraping and crawling bots (default: false)

### Component Changes

- Upgrade gunicorn from 22.0.0 to 23.0.0
- Replace Materialize CSS 1.2.2 with Bootstrap 5.3.3
  - Existing Materialize CSS and JS files will be preserved to prevent cached versions of the application from breaking
  - Materialize-related files will be removed in a future minor release

## 5.13.4

### Application Changes

- Update references to GitHub repository to point to [stats.wwdt.me](https://github.com/questionlp/stats.wwdt.me) instead of `stats.wwdt.me_v5`.

## 5.13.3

### Application Changes

- Move web analytics tags out of `base.html` into `head.html`

## 5.13.2

### Application Changes

- Add Umami `script` tag to errors base template

## 5.13.1

### Application Changes

- Correct Umami `script` tag properties

## 5.13.0

### Application Changes

- Add support for Umami web analytics via `settings.umami_analytics` config object with the following keys:

| Config Key | Description |
| ---------- | ----------- |
| `_enabled` | Set value to `true` to enable adding Umami `script` tag (default: `false`) |
| `url` | URL of the Umami analytics script |
| `data_website_id` | Umami Site ID |
| `data_auto_track` | Set value to `false` to disable auto event tracking (default: `true`) |
| `data_host_url` | Override the location where Umami data is sent to |
| `data_domains` | Comma-delimited list of domains where the Umami script should be active |

### Component Changes

- Upgrade wwdtm 2.10.0 to 2.10.1

### Development Changes

- Upgrade ruff from 0.3.6 to 0.5.1
- Upgrade black from 24.3.0 to 24.4.2
- Upgrade pytest from 8.1.1 to 8.1.2

## 5.12.1

### Application Changes

- Change the footer font color to remove alpha transparency to improve readability

## 5.12.0

### Application Changes

- Add support for host, panelist and scorekeeper preferred pronouns via a label (aka tag) next to the corresponding ID label in their details page

## 5.11.3

### Component Changes

- Upgrade wwdtm from 2.9.1 to 2.10.0, which requires Wait Wait Stats Database version 4.7 or higher

## 5.11.2

### Application Changes

- Add a link next to the location coordinates that scrolls down to the location map in single location details view

## 5.11.1

### Application Changes

- Change the z-index for the map control area to `500` to prevent the controls from appearing over slide-out navigation or pop-up menus
- Update styles for Leaflet to inherit font-family used for the rest of the application (IBM Plex Sans)

## 5.11.0

### Application Changes

- This version requires version 4.6.1 of the Wait Wait Stats Database, which includes a new `ww_postal_abbreviations` table that is required
- Adding a new section to the location details page that displays a map using Leaflet.js, OpenStreetMap and location longitude/latitude coordinates
- Add a new config key `settings.display_location_map` with a default of `false` as a feature flag for the above new feature
- Move the city and state from the `h2` heading to a new "Located In" field
- Display full state, province or territory name rather than two-letter abbreviation in locations list or in show details page
- Display decimal latitude/latitude coordinates in location details page with DMS coordinates in a tooltip
- Add PNG, SVG and Apple touch icon versions of the application's favicon

### Component Changes

- Adding Leaflet.js 1.9.4
- Upgrade wwdtm from 2.8.2 to 2.9.1

## 5.10.4

### Component Changes

- Upgrade wwdtm from 2.8.1 to 2.8.2
- Upgrade flask from 3.0.0 to 3.0.3
- Upgrade gunicorn from 21.2.0 to 22.0.0

### Development Changes

- Upgrade ruff from 0.1.13 to 0.3.6
- Upgrade pytest from 7.4.4 to 8.1.1

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
