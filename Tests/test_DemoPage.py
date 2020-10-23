from Pages.CommonPage import CommonPage
from Pages.DemoPage import DemoPage
from Tests.Base import BaseTest
from Config.config import TestData

class Test_Demo(BaseTest):
    def test_verify_DemoPage_title(self):
        self.demoPage = DemoPage(self.driver)
        assert self.demoPage.get_title() == TestData.DEMO_PAGE_TITLE

    def test_top_bar_elements(self):
        self.demoPage = DemoPage(self.driver)
        self.commonPage = CommonPage(self.driver)
        self.commonPage.verify_top_bar()

    def test_bottom_bar_elements(self):
        self.demoPage = DemoPage(self.driver)
        self.commonPage = CommonPage(self.driver)
        self.commonPage.verify_bottom_bar()

    def test_body_links(self):
        self.demoPage = DemoPage(self.driver)
        self.demoPage.validate_1to1_demo()
        self.demoPage.validate_watch_videos()
        self.demoPage.vallidate_group_live_demo()
