
import logging.config
from selenium.webdriver.common.keys import Keys
from src.base.page import Page
from selenium.webdriver.common.action_chains import ActionChains
logger = logging.getLogger(__name__)


class TestSalesForce(Page):

    login_button_on_home_page_id = 'login-button'
    username_field_id = 'username'
    password_field_id = 'password'
    login_button_on_account_page = 'Login'
    search_field_id = 'st-search-input'
    search_item_writing_tests = 'Writing Tests'
    search_result_writing_test_item = "//a[text()=' | Apex Developer Guide | Salesforce Developers']"
    writing_tests_header_item = "//span[@id='topic-title' and text()='Writing Tests']"
    apex_link_item = "//a[text()='Testing Apex']"
    apex_page_id = "//span[text()='Testing Apex']"
    apex_page_search_result = "//a[text()='Understanding Testing in Apex']"
    logout_button_id = 'user-info-logout'

    def test_login(self):
        self.driver.get('https://developer.salesforce.com/')
        self.login_button = self.driver.find_element_by_id(self.login_button_on_home_page_id)
        self.login_button.click()

        self.username_field = self.driver.find_element_by_id(self.username_field_id)
        self.password_field = self.driver.find_element_by_id(self.password_field_id)
        self.login = self.driver.find_element_by_id(self.login_button_on_account_page)
        self.username_field.send_keys("kamalkesar-w823@force.com")
        self.password_field.send_keys("Password1!")
        self.login.click()

        self.search_field = self.driver.find_element_by_id(self.search_field_id)
        assert self.search_field.is_displayed()
        self.search_field.send_keys(self.search_item_writing_tests)
        self.search_field.send_keys(Keys.ENTER)

        self.writing_tests = self.driver.find_element_by_xpath(self.search_result_writing_test_item)
        self.writing_tests.click()

        self.driver.implicitly_wait(20)
        self.writing_tests_header = self.driver.find_element_by_xpath(self.writing_tests_header_item)
        assert self.writing_tests_header.is_displayed()

        self.testing_apex_link = self.driver.find_element_by_xpath(self.apex_link_item)
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.testing_apex_link)
        self.testing_apex_link.send_keys(Keys.PAGE_DOWN)
        self.testing_apex_link.send_keys(Keys.ENTER)

        self.apex_page = self.driver.find_element_by_xpath(self.apex_page_id)
        assert self.apex_page.is_displayed()
        self.understanding_testing_in_apex_link_on_testing_apex_page = self.driver.find_element_by_xpath(self.apex_page_search_result)

        self.logout_button_dropdown = self.driver.find_element_by_id(self.login_button_on_home_page_id)
        self.logout_button_dropdown.click()
        self.logout_button = self.driver.find_element_by_id(self.logout_button_id)
        self.logout_button.click()




