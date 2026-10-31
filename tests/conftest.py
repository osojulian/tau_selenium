import pytest
from selenium import webdriver
import json


@pytest.fixture
def config(scope = "session"):


    #Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Asserts values are acceptable
    assert config['browser'] in ["chrome", "edge", "Headless Chrome"]
    assert isinstance(config['implicit_wait'], int) and config['implicit_wait'] > 0


    return config

@pytest.fixture
def browser(config):
    #Initialize the web driver

    if config['browser'] == 'chrome':
        b = webdriver.Chrome()
    elif config['browser'] == 'edge':
        b = webdriver.edge()
    elif config['browser'] == 'Headless Chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        b = webdriver.Chrome(options=options)
    else:
        raise Exception(f'browser "{config['browser']}" is not supported')


    ## Implicitly wait
    b.implicitly_wait(config['implicit_wait'])


    # Yield
    yield b

    # Teardown
    b.quit()
