from Pages.CommonPage import CommonPage
from Pages.CareersPage import CareersPage
from Tests.Base import BaseTest
from Config.config import TestData

class Test_Careers(BaseTest):
    def test_verify_CareerPage_title(self):
        self.careerPage = CareersPage(self.driver)
        assert self.careerPage.get_title() == TestData.CAREER_PAGE_TITLE

    def test_top_bar_elements(self):
        self.careerPage = CareersPage(self.driver)
        self.commonPage = CommonPage(self.driver)
        self.commonPage.verify_top_bar()

    def test_bottom_bar_elements(self):
        self.careerPage = CareersPage(self.driver)
        self.commonPage = CommonPage(self.driver)
        self.commonPage.verify_bottom_bar()

    def test_Main_Descriptions(self):
        self.careerPage = CareersPage(self.driver)
        self.careerPage.validate_description_sections()

    def test_discover_links(self):
        self.careerPage = CareersPage(self.driver)
        self.careerPage.validate_Discover_links_And_Sections()

    def test_global_tribe(self):
        self.careerPage = CareersPage(self.driver)
        self.careerPage.validate_global_tribe()
