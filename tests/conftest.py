import pytest
import selenium
from selenium import webdriver

@pytest.fixture
def browser():
    #Setup
    b = webdriver.Chrome()

    b.implicitly_wait(10)

    # Yield
    yield b

    # Teardown
    b.quit()
