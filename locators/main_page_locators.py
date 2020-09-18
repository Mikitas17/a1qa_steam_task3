from selenium.webdriver.common.by import By


class MainPageLocators:
    INSTALL_REDIRECT_BUTTON = (By.XPATH, "//a[contains(@class, "
                                         "'header_installsteam_btn_content')]")
    DOWNLOAD_BUTTON = (By.XPATH, "//a[contains(@class, "
                                 "'about_install_steam_link')]")
    BROWSE_MENU_BUTTON = (By.XPATH, "//div[@id='genre_tab']")
    ACTION_PAGE_REDIRECT_FROM_POP_UP = (By.XPATH, "//div[@class='popup_menu"
                                                  "']/a[contains(@href, "
                                                  "'Action')]")
    TEST_LIST = (By.CSS_SELECTOR, "#TopSellersTable .discount_pct")
