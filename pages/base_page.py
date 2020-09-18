from my_errors import ElementNotPresent


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, locate_by, selector):
        try:
            self.browser.find_element(locate_by, selector)
        except ElementNotPresent:
            return False
        return True
