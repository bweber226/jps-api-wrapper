# JPS (Jamf Pro Server) API Wrapper

[![GitLab](https://img.shields.io/gitlab/license/cvtc/appleatcvtc/jps-api-wrapper?style=flat-square)]()
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/jps-api-wrapper)](https://img.shields.io/pypi/dm/jps-api-wrapper?style=flat-square)

The JPS (Jamf Pro Server) API Wrapper encapsulates all available endpoints in the Classic and Pro versions of the Jamf API to make them easier and faster to use in Python.

I plan on keeping this up to date with current releases of JPS. Check the changelog for additional endpoints or changes on new JPS releases.

## Table of Contents

- [JPS (Jamf Pro Server) API Wrapper](#jps-jamf-pro-server-api-wrapper)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Install](#install)
  - [Usage](#usage)
  - [Method Documentation](#method-documentation)
  - [Other Notes](#other-notes)
  - [Contributing](#contributing)
  - [License](#license)

## Background

This project is a successor to [OrganicJamf](https://gitlab.com/cvtc/appleatcvtc/organicjamf) which was an API wrapper project that gained functionality as our organization needed it. As I added more and more to it I decided to rip the band-aid off and just finish out the wrapper so that it included all endpoints. This involved a rewrite to make it less time consuming to add endpoints as I plan on maintaining this for future releases of JPS. This was built as a time saving measure for automation projects dealing with JPS.

## Install

To install JPS API Wrapper run the following:

```
pip install jps-api-wrapper
```

## Usage

Using with statements with the Classic and Pro modules will cause the authentication token to invalidate upon exiting. Do any requests before exiting to use the same session authentication.

```
from jps_api_wrapper.classic import Classic
from jps_api_wrapper.pro import Pro
from os import environ

JPS_URL = "https://example.jamfcloud.com"
USERNAME = environ["JPS_USERNAME"]
PASSWORD = environ["JPS_PASSWORD"]

with Classic(JPS_URL, USERNAME, PASSWORD) as classic:
    print(classic.get_computers())
    print(classic.get_computer(1001))

with Pro(JPS_URL, USERNAME, PASSWORD) as pro:
    print(pro.get_mobile_devices())
```

If not using with statements it is recommended to invalidate the token before closing the program. You can do this manually by doing the following.

```
from jps_api_wrapper.classic import Classic
from jps_api_wrapper.pro import Pro
from os import environ

JPS_URL = "https://example.jamfcloud.com"
USERNAME = environ["JPS_USERNAME"]
PASSWORD = environ["JPS_PASSWORD"]

print(classic.get_building(name="Example"))
classic.session.auth.invalidate()
```

Any methods that require the data param will have a link to Jamf's documentation in the docstring and the method documentation for the syntax of the data that the request expects.

For some examples of jps-api-wrapper usage in real projects feel free to check out my other projects in our [GitLab](https://gitlab.com/cvtc/appleatcvtc).

## Method Documentation

View the [ReadTheDocs](https://jps-api-wrapper.readthedocs.io/en/stable/)

The method documentation is meant to match [Jamf's API Reference](https://developer.jamf.com/jamf-pro/reference/classic-api) for easy navigation of functionality.

## Other Notes

- The Jamf Pro API is still under development unlike the Jamf Classic API, Jamf will typically deprecate endpoints before removing them but endpoints can be removed without warning due to security or other concerns. If you are using the Pro module please be aware of this.
- When a new version of the same endpoint is added to the Pro module it will be appended with a v* (ex Pro.get_patch_policy_dashboard_v2) until the previous version is deleted. Then the new version will retake the original name and the v2 version will be deprecated. I will try to give as much warning as possible on this but the Jamf Pro API is continuously being updated.
- data parameters come before identification in methods because it's more commonly a required field since more than one type of identification is typical (mostly in the Classic module)
- With deprecated assets like peripherals and managed preferences the get, update, and delete endpoints will be added but not creation since you shouldn't be making these anymore but you may still want to have access to disable or delete them since they're not in the GUI anymore
- Get methods that end in a plural return all values or filtered selection of all values that return in the same data format as the all request. The only exception to this is if the singular and plural word for the end of the endpoint name is the same (like software) then the all request is appended with _all to differentiate it
- The method names reflect the get, create, update, delete privilege requirements because they're more readable and easier to understand than post and put for people that aren't familiar with working with HTTP requests. Some methods are labeled to more accurately reflect the actual purpose rather than the HTTP method (i.e. Post requests that delete multiple records)
- Pro delete methods enforce type of the id and ids parameters because ids will split the list into the individual ids for processing. If this happens to a string, say "123", it will split that instead into ["1", "2", "3"] which would result in resource objects 1, 2, and 3 being deleted instead of the desired 123 resource object
- Pro methods predicated with replace are put methods that replace all existing data with the new data supplied. They are distinguished from other methods predicated by update so that someone does not mistakenly replace all data when they just meant to update

## Contributing

This repository contains a Pipfile for easy management of virtual environments
with Pipenv. Run it, but don't create a lockfile, to install the development
dependencies:

```
pipenv install --skip-lock --dev
```

To run the tests and get coverage information, run:

```
pipenv run pytest --cov=src --cov-report=xml --cov-report=term-missing
```

Files are formatted with Black prior to committing. Black is installed in your Pipenv virtual environment. Run it like this before you commit:

```
pipenv run black .
```

PRs accepted. The main repo is my [organization's GitLab repo](https://gitlab.com/cvtc/appleatcvtc/jps-api-wrapper) so make any pull requests there as the GitHub repo is mirrored from there.

## License

[MIT © Bryan Weber.](./LICENSE)