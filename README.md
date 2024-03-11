# Playwright Python End-to-end tests

## About

* The purpose of this repo is to create a structured playground for automating end-to-end tests for the page https://www.accuweather.com.

## Tech stack:
* Python
* Playwright
* Pytest

## Project structure

Project implements Page Object Pattern architecture.

* **pages:** main project library combines pages construction and behaviour in `page_objects`, pages locator
  definition and generation in `locators` and common elements like navbars or textinputs in `elements`.
  
* **specs:** definition of test suites and scenarios

* **utils:** definition of helper classes

* **conftest.py:** allows you to define fixtures, plugins, and hooks that can be shared across multiple test files in a
  subdirectories.


* **pytest.ini** is a configuration file for Pytest that allows you to set options and modify the behavior of Pytest for
  a specific project.
  
## Run test
### Run test locally

##### Download the repo to your local machine
##### Install Python

* The project requires [Python 3.11 or later ](https://www.python.org/downloads/)

##### Install Dependencies

* python -m pip install --upgrade pip
* pip install -r requirements.txt
* python -m playwright install --with-deps

##### Run test by command: pytest --html=test_artifacts/report/report.html


### Run test with GitHub Action
* The project is configured to run every hour on GitHub Action with below workflows file.

```
name: Playwright Tests
on:
  schedule:
    - cron: '0 * * * *'
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Ensure browsers are installed
      run: python -m playwright install --with-deps

    - name: Run your tests
      run: pytest --html=test_artifacts/report/report.html

    - name: Archive logs
      uses: actions/upload-artifact@v4
      with:
        name: test_artifacts
        path: |
          test_artifacts/test_logs/
          test_artifacts/report/
          test_artifacts/screenshots/
```











