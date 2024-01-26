from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies_click(self):
        accept_all_button = self.driver.find_element(By.ID, 'wt-cli-accept-all-btn')
        accept_all_button.click()

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()
