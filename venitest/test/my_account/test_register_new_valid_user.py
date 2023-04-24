import pytest
from venitest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewValidUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        print("**************")
        print("This test verifies the registration with valid username and password")
        print("**************")
        my_account_signed_out = MyAccountSignedOut(self.driver)
        #go to my account
        my_account_signed_out.go_to_my_account()
        #fill in email and password
        my_account_signed_out.input_register_email("test@abv.bg")
        my_account_signed_out.input_password_registration("Test123456!")
        #click register
        my_account_signed_out.click_register_button()
        #verify registration

