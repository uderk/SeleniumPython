from venitest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from venitest.src.SeleniumExtended import SeleniumExtended
from venitest.src.helpers.config_helpers import get_base_url


class MyAccountSignedIn(MyAccountSignedInLocators):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        my_account_url = get_base_url() + self.endpoint
        self.driver.get(my_account_url)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LOGOUT_BUTTON_LEFT)

