import time

from venitest.src.helpers.config_helpers import get_base_url
from venitest.src.SeleniumExtended import SeleniumExtended
from venitest.src.pages.locators.CheckOutPageLocators import CheckOutPageLocators
from venitest.src.helpers.generic_helpers import generate_random_email


class CheckOutPage(CheckOutPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # constant fields
    first_name = "veni"
    last_name = "zdravkov"
    street = "test street"
    town = "Sofia"
    country = "Bulgaria"
    postcode = "9000"
    phone = "08705858402"
    email = generate_random_email()

    # state = "Sofia"

    # actions
    def enter_first_name(self):
        self.sl.wait_and_input_text(self.FIRST_NAME, self.first_name)

    def enter_last_name(self):
        self.sl.wait_and_input_text(self.LAST_NAME, self.last_name)

    def enter_street(self):
        self.sl.wait_and_input_text(self.STREET, self.street)

    def enter_town(self):
        self.sl.wait_and_input_text(self.CITY, self.town)

    def enter_postcode(self):
        self.sl.wait_and_input_text(self.POSTCODE, self.postcode)

    def enter_phone(self):
        self.sl.wait_and_input_text(self.PHONE, self.phone)

    def enter_email(self):
        self.sl.wait_and_input_text(self.EMAIL, self.email)

    def select_country(self):
        self.sl.select_from_dynamic_dropdown(self.COUNTRY, self.COUNTRY_DROPDOWN_INPUT, self.country)

    def click_place_order_and_verify(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)
        # place order takes unusual amount of time
        time.sleep(15)
        self.sl.wait_until_element_is_visible(self.ORDER_RECEIVED)

    def get_order_number(self):
        self.sl.wait_and_get_text(self.ORDER_NUMBER)
