from pages.base_page import BasePage
from locators.responsive_page_locators import ResponsivePageLocators
from my_parser import g_settings
from elements.drop_down_menu import drop_down


class ResponsivePage(BasePage):

    def drop_down_fill_date(self):
        drop_down(g_settings.get_browser, g_settings.get_dob()[0],
                  *ResponsivePageLocators.DOB_DAY)
        drop_down(g_settings.get_browser, g_settings.get_dob()[1],
                  *ResponsivePageLocators.DOB_MONTH)
        drop_down(g_settings.get_browser, g_settings.get_dob()[2],
                  *ResponsivePageLocators.DOB_YEAR)

    def to_product_page(self):
        to_page = g_settings.get_browser.find_element(
            *ResponsivePageLocators.VIEW_PAGE)
        to_page.click()
