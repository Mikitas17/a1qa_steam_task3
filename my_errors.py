class DriverNotChosenError(Exception):

    def __init__(self, message="You need to choose correctly one driver when "
                               "creating an instance. For example: "
                               "first_instance = BrowserFactory("
                               "browser='firefox')"):
        self.message = message
        super().__init__(self.message)


class ElementNotPresent(Exception):
    def __init__(self, message="There is no such an element on the page"):
        self.message = message
        super().__init__(self.message)
