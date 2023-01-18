# JPS API Wrapper

[![license](LINK TO GITHUB AFTER THIS IS UP)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

The JPS (Jamf Pro Server) API Wrapper encapsulates all available endpoints in the Classic and Pro versions of the Jamf API to make them easier and faster to use.

## Table of Contents

- [JPS API Wrapper](#jps-api-wrapper)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Install](#install)
  - [Usage](#usage)
  - [Method Documentation](#method-documentation)
  - [Other Notes](#other-notes)
  - [Contributing](#contributing)
  - [License](#license)

## Background

This project is a successor to [OrganicJamf](https://gitlab.com/cvtc/appleatcvtc/organicjamf) which was an API wrapper project that gained functionality as our organization needed it. As I added more and more to it I decided to rip the bandaid off and just finish out the wrapper so that it included all endpoints. This involved a rewrite to make it less time consuming to add endpoints as I plan on maintaining this for future releases of JPS. This was built as a time saving measure for automation projects dealing with JPS.

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
    print(classic.get_computer())

with Pro(JPS_URL, USERNAME, PASSWORD) as pro:
    print(pro.get_mobile_devices())
```

Any methods that require the data param will have a link to Jamf's documentation in the docstring for the syntax of the data that the request expects.

Note: The `license` badge image link at the top of this file should be updated with the correct `:user` and `:repo`.

## Method Documentation

View the [ReadTheDocs](INSERT LINK LATER)

## Other Notes

- data parameters come before identification in methods because it's more commonly a required field since more than one type of identification is typical (mostly in the Classic module)
- With deprecated assets like peripherals and managed preferences the get, update, and delete endpoints will be added but not creation since you shouldn't be making these anymore but you may still want to have access to disable or delete them since they're not in the GUI anymore
- Get methods that end in a plural return all values or filtered selection of all values that return in the same data format as the all request. The only exception to this is if the singular and plural word for the end of the endpoint name is the same (like software) then the all request is appended with _all to differentiate it
- The method names reflect the get, create, update, delete privilege requirements because they're more readable and easier to understand than post and put for people that aren't familiar with working with HTTP requests. Some methods are labeled to more accurately reflect the actual purpose rather than the HTTP method (i.e. Post requests that delete multiple records)
- Pro delete methodes enforce type of the id and ids parameters because ids will be split the list into the ids for processing. If this happens to a string, say "123" it will split that instead into ["1", "2", "3"] which would result in resource objects 1, 2, and 3 being deleted instead of the desired 123 resource object
- Pro methods predicated with replace are put methods that replace all existing data with the new data supplied. They are distringuished from other methods predicated by update so that someone does not mistakingly replace all data when they just meant to update

## Contributing

PRs accepted.

## License

[MIT © Bryan Weber.](./LICENSE)