from selenium.webdriver.common.by import By


class ResponsivePageLocators:
    AGE_SELECTOR = (By.XPATH, "//div[@class='agegate_birthday_selector']")
    DOB_DAY = (By.XPATH, "//select[@id='ageDay']")
    DOB_MONTH = (By.XPATH, "//select[@id='ageMonth']")
    DOB_YEAR = (By.XPATH, "//select[@id='ageYear']")
    VIEW_PAGE = (By.XPATH, "//a[@onclick='ViewProductPage()']")
