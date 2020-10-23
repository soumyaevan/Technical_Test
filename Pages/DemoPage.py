from selenium.webdriver.common.by import By
import pytest_check as check
from Pages.BasePage import BasePage
from Config.config import TestData
class DemoPage(BasePage):

    """Elements in the body section"""
    # IMG_1_1_DEMO = (By.XPATH, "//p/span[2]/a[@href='#form-popup-1']/../../../../../div/a/div")
    LINK_SCHEDULE_NOW = (By.XPATH, "//p/span[2]/a[@href='#form-popup-1']")
    # IMG_WATCH_VIDEOS = (By.XPATH, "//p[contains(text(),'analyze your spend')]/../../a/div")
    LINK_WATCH_NOW = (By.XPATH, "//p[contains(text(),'analyze your spend')]/span/a")
    # IMG_GROUP_LIVE_DEMO = (By.XPATH, "//p/span[2]/a[@href='#form-popup-3']/../../../../a/div")
    LINK_SIGN_UP_HERE = (By.XPATH, "//p/span[2]/a[@href='#form-popup-3']")
    FORM_1_1_DEMO = (By.XPATH, "//div[@id='form-popup-1']")
    FORM_1_1_DEMO_CLOSE_BTN = (By.XPATH, "//a[@href='#close-modal']")
    FORM_WATCH_LIVE_DEMO = (By.XPATH, "//div[@id='form-popup-2']")
    FORM_GROUP_LIVE_DEMO = (By.XPATH, "//div[@id='form-popup-3']")

    """Constructor of CarrersPage class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.DEMO_PAGE_URL)

    """Getting the title of the page"""
    def get_demo_page_title(self):
        return self.get_title()

    """Validating 1 to 1 demo section"""
    def validate_1to1_demo(self):
        # assert self.verify_element_displayed(self.IMG_1_1_DEMO)
        check.is_true(self.verify_element_displayed(self.LINK_SCHEDULE_NOW))
        self.click_element(self.LINK_SCHEDULE_NOW)
        check.is_true(self.verify_element_displayed(self.FORM_1_1_DEMO))
        self.click_element(self.FORM_1_1_DEMO_CLOSE_BTN)

    """Validating watch videos section"""
    def validate_watch_videos(self):
        # assert self.verify_element_displayed(self.IMG_WATCH_VIDEOS)
        check.is_true(self.verify_element_displayed(self.LINK_WATCH_NOW))
        self.click_element(self.LINK_WATCH_NOW)
        check.is_true(self.verify_element_displayed(self.FORM_WATCH_LIVE_DEMO))
        self.click_element(self.FORM_1_1_DEMO_CLOSE_BTN)

    """Validating Group Live Demo section"""
    def vallidate_group_live_demo(self):
        check.is_true(self.verify_element_displayed(self.LINK_SIGN_UP_HERE))
        self.click_element(self.LINK_SIGN_UP_HERE)
        check.is_true(self.verify_element_displayed(self.FORM_GROUP_LIVE_DEMO))
        self.click_element(self.FORM_1_1_DEMO_CLOSE_BTN)