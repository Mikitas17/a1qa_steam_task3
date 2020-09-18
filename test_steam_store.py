import pytest
from my_parser import g_settings
from pages.main_page import MainPage
from browser_factory import BrowserFactory
from utils import file_checker
import time


def test_steam_app_download():
    driver = BrowserFactory.get_instance(g_settings.get_browser)
    main_page = MainPage(driver, g_settings.get_url())
    main_page.open()
    main_page.open_launcher_download()
    main_page.download_steam_installer()
    time.sleep(5)
    assert file_checker.is_file_downloaded("SteamSetup.exe")


@pytest.mark.discount_calculation
def test_highest_discount_check():
    driver = BrowserFactory.get_instance(g_settings.get_browser)
    main_page = MainPage(driver, g_settings.get_url())
    main_page.open()
    assert main_page.is_open()
    main_page.choose_genre(genre='Action')
    chosen_genre_page = ChosenGenreGamesPage(driver)
    chosen_genre_page.click_top_sellers_tab()
    game_from_top_seller_list = chosen_genre_page.click_on_item_with_discount_n_get_values()
    age_check_page = AgeCheckPage(driver)
    if age_check_page.is_open():
        age_check_page.select_year_n_submit('2000')
    game_page = GamePage(driver)
    game_from_game_page = game_page.get_data()
    assert game_from_top_seller_list.name == game_from_game_page.name
    assert game_from_top_seller_list.discount_pct == game_from_game_page.discount_pct
    assert game_from_top_seller_list.original_price == game_from_game_page.original_price
    assert game_from_top_seller_list.final_price == game_from_game_page.final_price


@pytest.mark.discount_calculation
def test_lowest_discount_check():
    driver = BrowserFactory.get_instance(g_settings.get_browser)
    main_page = MainPage(driver, g_settings.get_url())
    main_page.open()
    assert main_page.is_open()
    main_page.choose_genre(genre='Indie')
    chosen_genre_page = ChosenGenreGamesPage(driver)
    chosen_genre_page.click_top_sellers_tab()
    game_from_top_seller_list = chosen_genre_page.click_on_item_with_discount_n_get_values(
        high=False)
    age_check_page = AgeCheckPage(driver)
    if age_check_page.is_open():
        age_check_page.select_year_n_submit('2000')
    game_page = GamePage(driver)
    game_from_game_page = game_page.get_data()
    assert game_from_top_seller_list.name == game_from_game_page.name
    assert game_from_top_seller_list.discount_pct == game_from_game_page.discount_pct
    assert game_from_top_seller_list.original_price == game_from_game_page.original_price
    assert game_from_top_seller_list.final_price == game_from_game_page.final_price
