import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 20

    def wait_and_input_text(self, locator, input_text, timeout=None):
        # pass
        timeout = timeout if timeout else self.default_timeout
        #
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(20)
        # element = self.driver.find_element(By.ID, 'username')
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(input_text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

