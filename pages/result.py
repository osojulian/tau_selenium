## Create class and methods for each page

class DuckResult:


    #LOCATORS
    ## TODO: Locator for result link and search input

    def __init__(self, browser):

        self.browser = browser

    def title(self):
        return self.browser.title

    def values(self):
        return ""

    def link(self):
        return []