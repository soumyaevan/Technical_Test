import pytest
from selenium import webdriver
from Config.config import TestData

@pytest.fixture(params=TestData.BROWSERS,scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(TestData.IMPLICIT_WAIT)
    web_driver.maximize_window()
    yield
    web_driver.quit()