# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [Unreleased]

### Added
- Tools & infrastructure reflection page added to documentation website (`tools_infrastructure.qmd`) and linked in the navbar ([#86](https://github.com/UBC-MDS/ez-df-data-validator/issues/86)).
- Example output added to the tutorial for clearer function usage.
- Docstrings added to core unit tests to improve documentation clarity ([#78](https://github.com/UBC-MDS/ez-df-data-validator/issues/78)).
- Additional CHANGELOG entries to improve release tracking ([#99](https://github.com/UBC-MDS/ez-df-data-validator/issues/99)).

### Changed
- Documentation structure and layout improved.
- README badges updated to use dynamic versioning.
- `publish.yml` and `pyproject.toml` updated to support dynamic versioning and TestPyPI publishing.
- Build workflow updated to generate documentation preview deployments ([#94](https://github.com/UBC-MDS/ez-df-data-validator/issues/94)).

### Fixed
- Fixed missing output for example code in the README ([#83](https://github.com/UBC-MDS/ez-df-data-validator/issues/83), [#92](https://github.com/UBC-MDS/ez-df-data-validator/pull/92)).
- Fixed documentation landing page layout.
- Removed unnecessary generated files from the repository ([#85](https://github.com/UBC-MDS/ez-df-data-validator/issues/85)).

### CI / Infrastructure
- GitHub Actions workflows updated to:
  - run `pytest` with coverage
  - run `ruff` lint checks
  - build Quartodoc reference
  - render Quarto documentation
  - deploy documentation previews
  - publish package to TestPyPI via automated pipeline
- Development → main branch sync completed following staging workflow.



## [0.0.3] - 2026-01-24

### Added
- More test handle missing ([#62](https://github.com/UBC-MDS/ez-df-data-validator/issues/62))
- Add missing_summary function and unit tests ([#43](https://github.com/UBC-MDS/ez-df-data-validator/issues/43))
- Add ruff to toml ([#59](https://github.com/UBC-MDS/ez-df-data-validator/issues/59))
- Add CI workflow and improve missing_summary docs and tests ([#52](https://github.com/UBC-MDS/ez-df-data-validator/issues/52))
- build.yml ([#66](https://github.com/UBC-MDS/ez-df-data-validator/issues/66))
- Change package name ([#67](https://github.com/UBC-MDS/ez-df-data-validator/issues/67))
- Update README for Milestone 3 (docs, CI, usage, tests) ([#70](https://github.com/UBC-MDS/ez-df-data-validator/issues/70))
- Publish pipeline to TestPYPI ([#71](https://github.com/UBC-MDS/ez-df-data-validator/issues/71))

## [0.0.2] - 2026-01-17

### Added
- Add missing_summary function implementation and unit tests by @wst0712 in #43
- Fix docstring in handle_missing() ([#42](https://github.com/UBC-MDS/ez-df-data-validator/issues/42))
- Implement schema_standardizer function ([#40](https://github.com/UBC-MDS/ez-df-data-validator/issues/40))
- Fix and standardize docstrings across functions ([#39](https://github.com/UBC-MDS/ez-df-data-validator/issues/39))
- Add implementation and unit tests for handle_missing() (LLM-assisted design - decisions) ([#38](https://github.com/UBC-MDS/ez-df-data-validator/issues/38))
- Add function code for find_duplicates ([#36](https://github.com/UBC-MDS/ez-df-data-validator/issues/36))
- Add unit tests for find_duplicates ([#35](https://github.com/UBC-MDS/ez-df-data-validator/issues/35))
- Refine function definitions based on LLM feedback ([#34](https://github.com/UBC-MDS/ez-df-data-validator/issues/34))

## [0.0.1] - 2026-01-10

### Added
- Initial repo setup ([#7](https://github.com/UBC-MDS/ez-df-data-validator/issues/7))
- edit readme ([#9](https://github.com/UBC-MDS/ez-df-data-validator/issues/9))
- create function spec for find_duplicates ([#10](https://github.com/UBC-MDS/ez-df-data-validator/issues/10))
- Add SchemaStandardizer for initial dataframe hygiene ([#11](https://github.com/UBC-MDS/ez-df-data-validator/issues/11))
- Handle missing ([#14](https://github.com/UBC-MDS/ez-df-data-validator/issues/14))
- Add missing_summary function specification ([#12](https://github.com/UBC-MDS/ez-df-data-validator/issues/12))
- Update README with missing_summary function details ([#15](https://github.com/UBC-MDS/ez-df-data-validator/issues/15))
- Format readme ([#16](https://github.com/UBC-MDS/ez-df-data-validator/issues/16))