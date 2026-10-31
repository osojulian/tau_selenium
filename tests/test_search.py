import pytest
import selenium

from pages.result import DuckResult
from pages.search import DuckSearch


@pytest.mark.parametrize("phrase", [
    "panda",
    "tiger",
    "selenium"
])
def test_duck_search(browser, phrase):


    ## Instance of class Result, Search
    search_page = DuckSearch(browser)
    result_page = DuckResult(browser)

    #### Follow structure Given, When, then

    #Given the duck home page is displayed
    search_page.load()

    #When the user searches for the phrase
    search_page.search(phrase)

    ## Asserts for the results, compare
    #Then the search result title contains "Panda"
    assert phrase in result_page.title()


    # I have to find the locators for this values and code
    

    #And the search result query is "Panda"
    #assert phrase == result_page.values()

    #And the search result links pertain to "Panda"
    #titles = result_page.link()
    #matches = [t for t in titles if phrase.lower() in t.lower()]
    #assert len(matches) > 0


    # Raise if something happen and use in other cases
    # raise Exception("Incomplete Test")