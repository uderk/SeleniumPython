from venitest.src.helpers.config_helpers import get_base_url
from venitest.src.SeleniumExtended import SeleniumExtended
from venitest.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    applied_coupon_success_message = "Coupon code applied successfully."

    def get_all_product_names_in_cart(self):
        products = self.sl.wait_until_elements_are_visible(self.PRODUCT_NAME)
        products_names = [p.text for p in products]
        return products_names

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_CODE, coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON)

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

    def check_if_coupon_is_applied(self):
        self.sl.wait_until_element_contains_text(self.APPLIED_COUPON_MESSAGE_SUCCESS,
                                                 self.applied_coupon_success_message)

    def proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BUTTON)
