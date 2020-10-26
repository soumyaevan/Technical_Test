import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from Config.config import TestData

@pytest.fixture(params=TestData.BROWSERS,scope='class')
def init_driver(request):
    if request.param == 'chrome':
        # web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    if request.param == 'firefox':
        # web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(TestData.IMPLICIT_WAIT)
    web_driver.maximize_window()
    yield
    web_driver.quit()