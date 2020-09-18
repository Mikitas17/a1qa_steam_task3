from pages.base_page import BasePage
from my_parser import g_settings
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser, url):
        super(MainPage, self).__init__(browser)
        self.base_url = url

    def open(self):
        self.browser.get(self.base_url)

    def open_launcher_download(self):
        download_link = self.browser.find_element(
            *MainPageLocators.INSTALL_REDIRECT_BUTTON)
        download_link.click()

    def download_steam_installer(self):
        download_button = self.browser.find_element(
            *MainPageLocators.DOWNLOAD_BUTTON)
        download_button.click()

    def choose_genre(self, genre: str):
        lang = g_settings.get_language()
        genre_tab = Menu(*self._genre_menu, driver=self.driver)
        if genre == "Action":
            if lang == 'en':
                genre_tab.choose_item(*self._action_games_link)
            else:
                genre_tab.choose_item(*self._action_games_ru_link)
        elif genre == 'Indie':
            if lang == 'en':
                genre_tab.choose_item(*self._indie_games_link)
            else:
                genre_tab.choose_item(*self._indie_games_ru_link)