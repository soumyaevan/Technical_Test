from selenium.webdriver.common.by import By
import pytest_check as check
from Pages.BasePage import BasePage
from Config.config import TestData

class CareersPage(BasePage):

    """Elements if careers page"""
    SECTION_WHO_WE_ARE = (By.XPATH,"//h2[text()='Who we are']")
    SECTION_WHAT_WE_DO = (By.XPATH,"//h2[text()='What we do']")
    SECTION_HOW_WE_DO_IT = (By.XPATH, "//h2[text()='How we do it']")
    SECTION_DISCOVER_WHERE_WE_BELONG = (By.XPATH, "//h2[text()='Discover Where You Belong']")
    LINK_TECHNOLOGY = (By.XPATH, "//li[@data-tab='Technology-1']")
    SECTION_TECHNOLOGY = (By.XPATH, "//div[@id='Technology-1']")
    LINK_PRODUCT = (By.XPATH, "//li[@data-tab='Product-2']")
    SECTION_PRODUCT = (By.XPATH, "//div[@id='Product-2']")
    LINK_RATE_MANAGEMENT = (By.XPATH, "//li[@data-tab='RateManagement-3']")
    SECTION_RATE_MANAGEMENT = (By.XPATH, "//div[@id='RateManagement-3']")
    LINK_MARKETING = (By.XPATH, "//li[@data-tab='Marketing-4']")
    SECTION_MARKETING = (By.XPATH, "//div[@id='Marketing-4']")
    LINK_CUSTOMER_SUCCESS = (By.XPATH, "//li[@data-tab='CustomerSuccess-5']")
    SECTION_CUSTOMER_SUCCESS = (By.XPATH, "//div[@id='CustomerSuccess-5']")
    LINK_FINANCE = (By.XPATH, "//li[@data-tab='FinanceandPeopleOps-6']")
    SECTION_FINANCE = (By.XPATH, "//div[@id='FinanceandPeopleOps-6']")
    LINK_LEGAL = (By.XPATH, "//li[@data-tab='Legal-7']")
    SECTION_LEGAL = (By.XPATH, "//div[@id='Legal-7']")
    LINK_SALES = (By.XPATH, "//li[@data-tab='Sales-8']")
    SECTION_SALES = (By.XPATH, "//div[@id='Sales-8']")
    LINK_GLOBAL_TRIBE_OSLO = (By.XPATH, "//div[@id='slick-slide20']/div/div/div/a[2]")
    LINK_GLOBAL_TRIBE_NEW_YORK = (By.XPATH, "//div[@id='slick-slide21']/div/div/div/a[2]")
    LINK_GLOBAL_TRIBE_HAMBURG = (By.XPATH, "//div[@id='slick-slide22']/div/div/div/a[2]")

    """Constructor of CarrersPage class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.CAREER_PAGE_URL)

    """Getting the title of the page"""
    def get_careers_page_title(self):
        return self.get_title()


    """Validate if Who we are, What we do and How we do it section is present """
    def validate_description_sections(self):
        check.is_true(self.verify_element_displayed(self.SECTION_WHO_WE_ARE))
        check.is_true(self.verify_element_displayed(self.SECTION_WHAT_WE_DO))
        check.is_true(self.verify_element_displayed(self.SECTION_HOW_WE_DO_IT))
        check.is_true(self.verify_element_displayed(self.SECTION_DISCOVER_WHERE_WE_BELONG))

    """Validate the 'Discover Where You Belong' section"""
    """Verifying each link in this section opens the corresponding division"""
    def validate_Discover_links_And_Sections(self):
        self.click_element(self.LINK_TECHNOLOGY)
        check.is_true(self.verify_element_displayed(self.SECTION_TECHNOLOGY))

        self.click_element(self.LINK_PRODUCT)
        check.is_true(self.verify_element_displayed(self.SECTION_PRODUCT))

        self.click_element(self.LINK_RATE_MANAGEMENT)
        check.is_true(self.verify_element_displayed(self.SECTION_RATE_MANAGEMENT))

        self.click_element(self.LINK_MARKETING)
        check.is_true(self.verify_element_displayed(self.SECTION_MARKETING))

        self.click_element(self.LINK_CUSTOMER_SUCCESS)
        check.is_true(self.verify_element_displayed(self.SECTION_CUSTOMER_SUCCESS))

        self.click_element(self.LINK_FINANCE)
        check.is_true(self.verify_element_displayed(self.SECTION_FINANCE))

        self.click_element(self.LINK_LEGAL)
        check.is_true(self.verify_element_displayed(self.SECTION_LEGAL))

        self.click_element(self.LINK_SALES)
        check.is_true(self.verify_element_displayed(self.SECTION_SALES))

    """Verifying that each 'Visit' link will open corresponding country's career page"""
    def validate_global_tribe(self):
        self.click_element(self.LINK_GLOBAL_TRIBE_OSLO)
        check.equal(self.get_title(),"Oslo Careers")
        self.driver.execute_script("window.history.go(-1)")

        self.click_element(self.LINK_GLOBAL_TRIBE_NEW_YORK)
        check.equal(self.get_title(), "New York City Careers")
        self.driver.execute_script("window.history.go(-1)")

        self.click_element(self.LINK_GLOBAL_TRIBE_HAMBURG)
        check.equal(self.get_title(), "Hamburg Careers")
        self.driver.execute_script("window.history.go(-1)")