from constants import BASE_URL
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, '//a[contains(text(), "Company")]')
    CAREERS_OPTION = (By.XPATH, '//a[contains(text(), "Careers")]')
    TEAMS_BLOCK = (By.ID, 'career-find-our-calling')
    LOCATIONS_BLOCK = (By.ID, 'career-our-location')
    LIFE_BLOCK = (By.XPATH, '//section[@data-id="a8e7b90"]')

    def open(self):
        self.driver.get(BASE_URL)

    def is_page_opened(self):
        return 'Insider' in self.driver.title

    def select_careers(self):
        self.click_button(self.COMPANY_MENU)
        self.click_button(self.CAREERS_OPTION)

    def careers_page_opened(self):
        return 'Careers' in self.driver.title

    def check_career_blocks(self):
        teams_block = self.driver.find_element(*self.TEAMS_BLOCK)
        assert 'Find your calling' in teams_block.text

        locations_block = self.driver.find_element(*self.LOCATIONS_BLOCK)
        assert 'Our Locations' in locations_block.text

        life_block = self.driver.find_element(*self.LIFE_BLOCK)
        assert 'Life at Insider' in life_block.text
