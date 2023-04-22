import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headleschrome', 'firefox', 'edge', 'ff']
    browser = os.environ.get('BROWSER', 'chrome')
    if not browser:
        raise Exception("The environment variable browser must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided {browser} is not of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()