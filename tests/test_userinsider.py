import allure
from pages.home_page import HomePage
from pages.qa_page import QualityAssurancePage


@allure.title("Open Home Page")
def test_open_home_page(driver):
    # step 1
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.is_page_opened()

    # step 2
    home_page.select_careers()
    assert home_page.careers_page_opened()
    home_page.check_career_blocks()


@allure.title("Filter QA Jobs and Check Positions")
def test_filter_qa_jobs(driver):
    with allure.step("Filter by Location"):
        # step 3
        qa_page = QualityAssurancePage(driver)
        qa_page.open()
        qa_page.accept_cookies_click()
        qa_page.open_all_qa_jobs()
        qa_page.wait_for_location_filter()
        qa_page.filter_by_location('Istanbul, Turkey')
        qa_page.wait_for_item_count_updated()
        positions = qa_page.get_positions_list()
        assert len(positions) > 0

    # step 4
    with allure.step("Check Position Details"):
        position_titles = qa_page.get_position_titles()
        position_departments = qa_page.get_position_departments()
        position_locations = qa_page.get_position_locations()

        for i in range(0, len(position_titles)):
            assert 'Quality Assurance' in position_titles[i].text or 'QA' in position_titles[i].text
            assert 'Quality Assurance' in position_departments[i].text
            assert 'Istanbul, Turkey' in position_locations[i].text

    # step 5
    with allure.step("Open a Position"):
        qa_page.open_position()
        qa_page.driver.switch_to.window(qa_page.driver.window_handles[1])
        qa_page.wait_for_position_page_opened()
        assert qa_page.is_position_page_opened()
