# Playwright Python End-to-end tests

## About

The purpose of this repo is to create a structured playground for automating end-to-end tests for the page https://www.accuweather.com.

## Project structure

Project implements Page Object Pattern architecture.

* **tests:** definition of test suites and scenarios

* **conftest.py:** allows you to define fixtures, plugins, and hooks that can be shared across multiple test files in a
  subdirectories.
* **pages:** main project library combines pages construction and behaviour in `page_objects`, pages locator
  definition and generation in `locators` and common elements like navbars or textinputs in `elements`.
* **pytest.ini** is a configuration file for Pytest that allows you to set options and modify the behavior of Pytest for
  a specific project.

## Installation

[Python](https://www.python.org/downloads/)

### Installation

#### Installing

* python -m pip install --upgrade pip
* pip install -r requirements.txt
* python -m playwright install --with-deps


## Run test
### Run test locally
### Run test with Jenkins

