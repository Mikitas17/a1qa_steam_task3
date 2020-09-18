from selenium.webdriver.support.ui import Select


def drop_down(driver, user_data, *elem_path):
    drop_down_day = driver.find_element(*elem_path)
    drop_down_day.click()
    drop_down_day = Select(driver.find_element(*elem_path))
    drop_down_day.select_by_visible_text(user_data)
