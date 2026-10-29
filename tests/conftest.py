import pytest
from selenium import webdriver
import json


@pytest.fixture
def config(scope = "session"):


    #Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Asserts values are acceptable


@pytest.fixture
def browser():
    #Setup
    b = webdriver.Chrome()

    b.implicitly_wait(10)

    # Yield
    yield b

    # Teardown
    b.quit()
