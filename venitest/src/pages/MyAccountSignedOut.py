from venitest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from venitest.src.SeleniumExtended import SeleniumExtended
from venitest.src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        my_account_url = get_base_url() + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.PASSWORD_LOGIN, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL,exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_password_registration(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BUTTON)