import pytest
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    # for linux
    gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    print(gecko)
    # options.add_argument('-headless')
    driver = webdriver.Firefox(options=options, executable_path=gecko)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def wait_for_element():
    def f(driver, time_out, search_method, search_param):
        try:
            element_present = EC.presence_of_element_located((search_method, search_param))
            WebDriverWait(driver, time_out).until(element_present)
        except TimeoutException:
            pytest.fail("Timed out waiting for page to load")
        pass
    return f
