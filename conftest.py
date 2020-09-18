# import pytest
# from browser_factory import BrowserFactory
# from my_parser import g_settings
#
#
# @pytest.fixture(autouse=False)
# def browser_main():
#     driver = BrowserFactory.get_instance(g_settings.get_browser)
#     driver.implicitly_wait(5)
#     driver.get(g_settings.get_url())
#     print("Open browser")
#     yield driver
#     print("Close browser")
#     driver.quit()
