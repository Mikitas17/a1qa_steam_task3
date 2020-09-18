import xml.etree.ElementTree as ET

user_data = ET.parse('config_files/user_data.xml')
root_user = user_data.getroot()

project_data = ET.parse('config_files/project_config.xml')
root_project = project_data.getroot()


class SettingsParserXml:

    def get_dob(self):
        day = root_user[0][0].text
        month = root_user[0][1].text
        year = root_user[0][2].text
        return day, month, year

    def get_browser(self):
        browser = root_user[0][3].text
        return browser

    def get_download_dir(self):
        directory = root_user[0][4].text
        return directory

    def get_language(self):
        language = root_user[0][5].text
        return language

    def get_url(self):
        url = root_project[0][0].text
        return url


g_settings = SettingsParserXml()
