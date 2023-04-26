import pytest
from venitest.src.pages.HomePage import HomePage
from venitest.src.pages.Header import Header

@pytest.mark.usefixtures('init_driver')
class TestE2ECheckOutGuestUser:

    # go to home page
    @pytest.mark.tcid14
    def test_end_ent_to_end_checkout_guest_user(self):
        print("**************")
        print("This tests verifies the checkout process for guest user")
        print("**************")
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        home_page.go_to_home_page()
        # add 1 item to chart
        home_page.add_first_item_to_chart()
        # go to chart
        header.click_on_chart_on_right_header()
        # apply free coupon

        # select free shipping

        # click on checkout

        # fill in form

        # click on place order

        # verify order is received

        # verify order is recorded in DB (via SQL)
