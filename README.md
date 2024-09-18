# SekretSauce Test Automation Project

## Description

This project is a test automation solution designed for a website created for testing purposes. It was developed as part of a final project to demonstrate skills in test automation.

## Requirements

- **Python version**: 3.11.5
- **Libraries**:
  - selenium 4.20.0
  - pytest 7.4.2
  - pytest-html 3.2.1

## Configuration

1. Create a `.env` file in the root directory of the project based on the provided example. Use the following example, but make sure to adjust the paths according to your environment:

CHROME_DRIVER_PATH=C:/path/to/chromedriver 
CONFIG_PATH=C:/path/to/config.json


2. If the `.env` file is missing or the paths are incorrect, the application will not be able to load the necessary configuration files or browser driver properly.

## Installation

1. Install the required libraries using:

pip install -r requirements.txt


2. Make sure the `.env` file is correctly configured before running the tests.

3. Run the tests using:

pytest

