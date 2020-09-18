from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from my_errors import DriverNotChosenError
from my_parser import g_settings


class BrowserFactory:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BrowserFactory, cls).__new__(cls)
        return cls.instance

    def get_instance(self):
        if g_settings.get_browser() == "firefox":
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install()
            )
        elif g_settings.get_browser() == "chrome":
            exec_path = ChromeDriverManager().install()
            options = webdriver.ChromeOptions()
            preferences = {
                "download.default_directory": g_settings.get_download_dir(),
                "safebrowsing.enabled": "false"
            }
            options.add_experimental_option("prefs", preferences)
            driver = webdriver.Chrome(exec_path, options=options)
        else:
            raise DriverNotChosenError
        driver.implicitly_wait(5)
        return driver
