from constants import BASE_URL, DEFAULT_WAIT_TIME
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class QualityAssurancePage(BasePage):
    QA_JOBS_BUTTON = (By.XPATH, '//a[contains(text(), "See all QA jobs")]')
    LOCATION_DROPDOWN = (By.ID, 'select2-filter-by-location-container')
    POSITIONS_LIST = (By.XPATH, '//div[contains(concat(" ", normalize-space(@class), " "), '
                                '" position-list-item ")]')
    VIEW_ROLE_BUTTON = (By.XPATH, '//a[contains(text(), "View Role")]')
    APPLY_TOP_JOB_BUTTON = (By.XPATH, '//a[contains(text(), "Apply for this job")]')
    APPLY_JOB_BUTTON = (By.XPATH, '//a[@data-qa="show-page-apply"]')
    LOCATION_FILTER = (By.ID, 'select2-filter-by-department-container')

    DENEME_ELEMENT = (By.ID, 'deneme')
    POSITION_TITLES = (By.XPATH, '//p[@class[contains(., "position-title")]]')
    POSITION_DEPARTMENTS = (By.XPATH, '//span[@class[contains(., "position-department")]]')
    POSITION_LOCATIONS = (By.XPATH, '//div[@class[contains(., "position-location")]]')

    @staticmethod
    def location_option(location):
        return By.XPATH, f'//li[contains(@class, "select2-results__option") and text() = "{location}"]'

    def open(self):
        self.driver.get(BASE_URL + 'careers/quality-assurance')

    def open_all_qa_jobs(self):
        self.click_button(self.QA_JOBS_BUTTON)

    def wait_for_location_filter(self):
        location_filter_present = ec.text_to_be_present_in_element(self.LOCATION_FILTER, "Quality Assurance")
        WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(location_filter_present)

    def wait_for_item_count_updated(self):
        item_count_updated = ec.text_to_be_present_in_element(self.DENEME_ELEMENT, '3')
        WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(item_count_updated)

    def filter_by_location(self, location):
        self.click_button(self.LOCATION_DROPDOWN)
        location_option = self.driver.find_element(*self.location_option(location))
        location_option.click()
        self.driver.execute_script("window.scrollTo(0, 500);")

    def get_positions_list(self):
        return self.POSITIONS_LIST

    def get_position_titles(self):
        return self.driver.find_elements(*self.POSITION_TITLES)

    def get_position_departments(self):
        return self.driver.find_elements(*self.POSITION_DEPARTMENTS)

    def get_position_locations(self):
        return self.driver.find_elements(*self.POSITION_LOCATIONS)

    def open_position(self):
        view_role_button = self.driver.find_element(*self.VIEW_ROLE_BUTTON)
        hover = ActionChains(self.driver).move_to_element(view_role_button)
        hover.perform()
        view_role_button.click()

    def wait_for_position_page_opened(self):
        apply_for_job_button_present = ec.visibility_of_element_located(self.APPLY_TOP_JOB_BUTTON)
        WebDriverWait(self.driver, DEFAULT_WAIT_TIME).until(apply_for_job_button_present)

    def is_position_page_opened(self):
        apply_job_button = self.driver.find_element(*self.APPLY_JOB_BUTTON)
        return apply_job_button
