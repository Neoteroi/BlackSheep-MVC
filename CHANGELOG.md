# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2025-03-23

- Upgrade to `BlackSheep` `2.1.0`.
- Modify the project template to support the new `Router` prefix feature, and
  the `APP_ROUTE_PREFIX` env variable to control the route prefix globally.
- Use the `get_diagnostic_app` from `BlackSheep`, as it is now included in the
  library.
- Use the `get_trailing_slash_middleware` function, to ensure all HTML
  documents are served at a path ending with a trailing '/'. This is necessary
  to ensure relative links in HTML documents work consistently.
- Add possibility to change the background color of the top section using an
  env variable `BG_COLOR`. This is to better support testing multiple
  installation using path based routing.
- Add example `Dockerfile` and instructions to use.

## 2025-03-17

- Add a fallback in case of Application startup error (`get_diagnostic_app`).
- Unpin `pydantic` version.
- Set the `APP_SHOW_ERROR_DETAILS` env variable in `dev.py`.

## 2023-11-26

- Update the template for BlackSheep v2
- Remove support for Pydantic v1, add support for `pydantic-settings`,
  and upgrade `Pydantic` pinned version
- Fix comments with proper templates format (`.jinja`).

## 2023-06-29 :gem:

- New project template
