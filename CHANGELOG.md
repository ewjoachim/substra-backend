# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- API: Added Pagination for lists of asset

## [0.2.0] - 2021-08-04
### Added
- Add docker config secret name for kaniko builder (#99).
- Add registry cleaning tasks.

### Changed
- Use a single compute pod for all the tasks of a compute plan (#17).
- Add two missing `__init__` files (#89).
- Update python dependencies.

## [0.1.12] - 2021-04-13
### Added
- Export models (#395).

### Fixed
- Binding to service.port instead of 8000.
- Datasample order for metrics.
- Auto-allocate docker-registry node port (#391).

### Changed
- Bump django from 2.2.19 to 2.2.20 in /backend.
- Update cryptography to its latest release.

## [0.1.11] - 2021-03-12
### Changed
- Update django and django-celery-results.

## [0.1.10] - 2021-03-09
### Changed
- docker-registry default service value to nodePort
- Update grpcio
- Change local peer hostname to prevent issue from grpc client
- Fix JWT token blacklist at logout
- Add django shared cache to prevent issue in throttling
- Less permissive CORS & AllowHosts

## [0.1.9] - 2021-02-09

## [0.1.8] - 2021-01-27

## [0.1.7] - 2021-01-26

## [0.1.6] - 2020-12-08

## [0.1.5] - 2020-12-01

## [0.1.4] - 2020-11-30

## [0.1.3] - 2020-10-02

## [0.1.2] - 2020-09-29

## [0.1.1] - 2020-08-12

## [0.1.0] - 2020-07-31

## [0.0.24] - 2020-07-21

## [0.0.23] - 2020-07-15

## [0.0.22] - 2020-07-10

## [0.0.21] - 2020-07-08

## [0.0.20] - 2020-07-07

## [0.0.19] - 2020-07-03

## [0.0.18] - 2020-06-03

## [0.0.17] - 2020-06-02

## [0.0.16] - 2020-05-29

## [0.0.15] - 2020-05-28

## [0.0.14] - 2020-05-18

## [0.0.13] - 2020-05-12

## [0.0.12] - 2020-04-14

## [0.0.11] - 2019-12-13

## [0.0.10] - 2019-12-06

## [0.0.9] - 2019-11-05

## [0.0.8] - 2019-05-27

## [0.0.7] - 2019-04-10

## [0.0.6] - 2019-04-03

## [0.0.5] - 2019-03-04

## [0.0.4] - 2019-03-04

## [0.0.3] - 2019-02-20

## [0.0.2] - 2019-02-15

## [0.0.1] - 2019-01-08

[Unreleased]: https://github.com/owkin/connect-backend/compare/0.2.0...HEAD
[0.2.0]: https://github.com/owkin/connect-backend/compare/0.1.12...0.2.0
[0.1.12]: https://github.com/owkin/connect-backend/compare/0.1.11...0.1.12
[0.1.11]: https://github.com/owkin/connect-backend/compare/0.1.10...0.1.11
[0.1.10]: https://github.com/owkin/connect-backend/compare/0.1.9...0.1.10
[0.1.9]: https://github.com/owkin/connect-backend/compare/0.1.8...0.1.9
[0.1.8]: https://github.com/owkin/connect-backend/compare/0.1.7...0.1.8
[0.1.7]: https://github.com/owkin/connect-backend/compare/0.1.6...0.1.7
[0.1.6]: https://github.com/owkin/connect-backend/compare/0.1.5...0.1.6
[0.1.5]: https://github.com/owkin/connect-backend/compare/0.1.4...0.1.5
[0.1.4]: https://github.com/owkin/connect-backend/compare/0.1.3...0.1.4
[0.1.3]: https://github.com/owkin/connect-backend/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/owkin/connect-backend/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/owkin/connect-backend/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/owkin/connect-backend/compare/0.0.24...0.1.0
[0.0.24]: https://github.com/owkin/connect-backend/compare/0.0.23...0.0.24
[0.0.23]: https://github.com/owkin/connect-backend/compare/0.0.22...0.0.23
[0.0.22]: https://github.com/owkin/connect-backend/compare/0.0.21...0.0.22
[0.0.21]: https://github.com/owkin/connect-backend/compare/0.0.20...0.0.21
[0.0.20]: https://github.com/owkin/connect-backend/compare/0.0.19...0.0.20
[0.0.19]: https://github.com/owkin/connect-backend/compare/0.0.18...0.0.19
[0.0.18]: https://github.com/owkin/connect-backend/compare/0.0.17...0.0.18
[0.0.17]: https://github.com/owkin/connect-backend/compare/0.0.16...0.0.17
[0.0.16]: https://github.com/owkin/connect-backend/compare/0.0.15...0.0.16
[0.0.15]: https://github.com/owkin/connect-backend/compare/0.0.14...0.0.15
[0.0.14]: https://github.com/owkin/connect-backend/compare/0.0.13...0.0.14
[0.0.13]: https://github.com/owkin/connect-backend/compare/0.0.12...0.0.13
[0.0.12]: https://github.com/owkin/connect-backend/compare/0.0.11...0.0.12
[0.0.11]: https://github.com/owkin/connect-backend/compare/0.0.10...0.0.11
[0.0.10]: https://github.com/owkin/connect-backend/compare/0.0.9...0.0.10
[0.0.9]: https://github.com/owkin/connect-backend/compare/0.0.8...0.0.9
[0.0.8]: https://github.com/owkin/connect-backend/compare/0.0.7...0.0.8
[0.0.7]: https://github.com/owkin/connect-backend/compare/0.0.6...0.0.7
[0.0.6]: https://github.com/owkin/connect-backend/compare/0.0.5...0.0.6
[0.0.5]: https://github.com/owkin/connect-backend/compare/0.0.4...0.0.5
[0.0.4]: https://github.com/owkin/connect-backend/compare/0.0.3...0.0.4
[0.0.3]: https://github.com/owkin/connect-backend/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/owkin/connect-backend/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/owkin/connect-backend/releases/tag/0.0.1