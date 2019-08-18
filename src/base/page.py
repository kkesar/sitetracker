
from selenium import webdriver
import logging.config


class Page:

    driver = None

    def setup_method(self):
        self.driver = webdriver.Chrome('../../resources/chromedriver')
        logger = logging.getLogger(__name__)
        print(logger.handlers)
        logger.debug('Starting up tests')

    def tear_down(self):
        self.driver.quit()
