import time

import pytest
from venitest.src.pages.HomePage import HomePage
from venitest.src.pages.Header import Header
from venitest.src.pages.CartPage import CartPage
from  venitest.src.pages.CheckOutPage import CheckOutPage

@pytest.mark.usefixtures('init_driver')
class TestE2ECheckOutGuestUser:

    # go to home page
    @pytest.mark.tcid14
    def test_end_ent_to_end_checkout_guest_user(self):
        print("**************")
        print("This tests verifies the checkout process for guest user")
        print("**************")
        #constants
        coupon_code = 100
        # page objects
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckOutPage(self.driver)

        home_page.go_to_home_page()
        # add 1 item to chart
        home_page.add_first_item_to_chart()
        # check if cart is updated
        header.wait_until_cart_item_count(1)
        # go to chart
        header.click_on_chart_on_right_header()
        product_names = cart_page.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"
    # apply free coupon
        cart_page.apply_coupon(coupon_code)
    # select free shipping
        cart_page.check_if_coupon_is_applied()
        cart_page.proceed_to_checkout()
    # fill in form
        checkout_page.enter_first_name()
        checkout_page.enter_last_name()
        checkout_page.select_country()
        checkout_page.enter_street()
        checkout_page.enter_town()
        # time.sleep(2)
        # checkout_page.enter_state()
        # time.sleep(2)
        checkout_page.enter_postcode()
        checkout_page.enter_phone()
        checkout_page.enter_email()
    # click on place order
        checkout_page.click_place_order_and_verify()
    # verify order is received

    # verify order is recorded in DB (via SQL)
