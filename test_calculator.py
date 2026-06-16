Exercise 2: Automated Python Unit Testing
Objective

Run tests automatically.

Project
calculator.py
test_calculator.py
Workflow
name: Run Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: 3.11

      - run: pip install pytest

      - run: pytest
Learn
Test automation
Fail-fast development
Real-world Purpose

Prevent broken code from entering repositories.
