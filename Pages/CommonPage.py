from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

"""This class contains the elements of top and bottom bar of the xenetta website and their corrseponding actions"""
"""These elements are common in both the test pages"""
class CommonPage(BasePage):

    """Elements from top bar"""
    OUR_CUSTOMER = (By.XPATH, "//li/a[@href='https://www.xeneta.com/customers']")
    PLATFORM = (By.XPATH, "//li/a[@href='https://www.xeneta.com/products']")
    RESOURCES_TOP = (By.XPATH, "//li/a[@href='https://www.xeneta.com/resources'][@aria-haspopup='true']")
    COMPANY = (By.XPATH, "//li/a[@href='https://www.xeneta.com/our-company']")
    SIGN_IN = (By.XPATH, "//li/a[@href='https://app.xeneta.com/']")
    GET_DEMO = (By.XPATH, "//li/a[@href='#parent-popup']")
    XENETTA_LOGO_TOP = (By.XPATH, "//div/a[@href='https://www.xeneta.com/']")

    """Elements from bottom bar"""
    SHIPPER_BCO = (By.XPATH, "//li/a[@href='https://www.xeneta.com/shippers-bco-analysts']")
    FREIGHT_FORWARDERS = (By.XPATH, "//li/a[@href='https://www.xeneta.com/freight-forwarders']")
    CARRIERS = (By.XPATH, "//li/a[@href='https://www.xeneta.com/carriers']")
    CUSTOMER_COMMUNITY = (By.XPATH, "//li/a[@href='http://community.xeneta.com/']")
    XENETA_PLATFORM = (By.XPATH, "//li/a[@href='https://www.xeneta.com/the-xeneta-platform']")
    RESOURCES_BOTTOM = (By.XPATH, "//li[@class='hs-menu-item hs-menu-depth-1']/a[@href='https://www.xeneta.com/resources']")
    CAREERS = (By.XPATH, "//li/a[@href='https://www.xeneta.com/careers']")
    NEWS = (By.XPATH, "//li/a[@href='https://www.xeneta.com/news']")
    CONTACT_US = (By.XPATH, "//li/a[@href='https://www.xeneta.com/contact']")
    PRESS_ROOM = (By.XPATH, "//li/a[@href='https://www.xeneta.com/press']")
    LINKED_IN = (By.XPATH, "//li/a[@href='https://www.linkedin.com/company/xeneta-as/']")
    TWITTER = (By.XPATH, "//li/a[@href='https://twitter.com/Xeneta_AS']")
    YOUTUBE = (By.XPATH, "//li/a[@href='https://www.youtube.com/channel/UCTqzaUYvGM6dOHgQBttUIiA']")
    SPOTIFY = (By.XPATH, "//li/a[@href='https://open.spotify.com/show/133DN4II1o7x6AuntYYl3F']")
    XENETTA_LOGO_BOTTOM = (By.XPATH, "//span/a[@href='https://www.xeneta.com/']")

    """constructor of the common page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def verify_top_bar(self):
        assert self.verify_element_displayed(self.OUR_CUSTOMER)
        assert self.verify_element_displayed(self.PLATFORM)
        assert self.verify_element_displayed(self.RESOURCES_TOP)
        assert self.verify_element_displayed(self.COMPANY)
        assert self.verify_element_displayed(self.SIGN_IN)
        assert self.verify_element_displayed(self.GET_DEMO)
        assert self.verify_element_displayed(self.XENETTA_LOGO_TOP)

    def verify_bottom_bar(self):
        assert self.verify_element_displayed(self.SHIPPER_BCO)
        assert self.verify_element_displayed(self.FREIGHT_FORWARDERS)
        assert self.verify_element_displayed(self.CARRIERS)
        assert self.verify_element_displayed(self.CUSTOMER_COMMUNITY)
        assert self.verify_element_displayed(self.XENETA_PLATFORM)
        assert self.verify_element_displayed(self.RESOURCES_BOTTOM)
        assert self.verify_element_displayed(self.CAREERS)
        assert self.verify_element_displayed(self.NEWS)
        assert self.verify_element_displayed(self.CONTACT_US)
        assert self.verify_element_displayed(self.PRESS_ROOM)
        assert self.verify_element_displayed(self.LINKED_IN)
        assert self.verify_element_displayed(self.TWITTER)
        assert self.verify_element_displayed(self.YOUTUBE)
        assert self.verify_element_displayed(self.SPOTIFY)
        assert self.verify_element_displayed(self.XENETTA_LOGO_BOTTOM)




