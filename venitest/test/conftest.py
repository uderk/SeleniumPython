import pytest
from selenium import webdriver

import os
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


@pytest.fixture(scope="class")
def init_driver(request):

    #global driver
    supported_browsers = ['chrome', 'ch', 'headleschrome', 'firefox', 'headlesfirefox', 'edge', 'ff']

    browser = os.environ.get('BROWSER', None)
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
    elif browser in "headleschrome":
        chrome_options = ChOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in "headlesfirefox":
        chrome_options = FFOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Firefox(options=chrome_options)

    request.cls.driver = driver
    yield
    driver.maximize_window()
    driver.quit()