import pytest
from venitest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from venitest.src.helpers.generic_helpers import generate_random_password
from venitest.src.helpers.generic_helpers import generate_random_email
from venitest.src.pages.MyAccountSignedIn import MyAccountSignedIn
@pytest.mark.usefixtures("init_driver")
class TestRegisterNewValidUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        #constants
        email = generate_random_email()
        password = generate_random_password(12)
        print("**************")
        print("This test verifies the registration with valid username and password")
        print("**************")
        my_account_signed_out = MyAccountSignedOut(self.driver)
        my_account_signed_in = MyAccountSignedIn(self.driver)
        #go to my account
        my_account_signed_out.go_to_my_account()
        #fill in email and password
        my_account_signed_out.input_register_email(email)
        my_account_signed_out.input_password_registration(password)
        #click register
        my_account_signed_out.click_register_button()
        #verify registration
        my_account_signed_in.verify_user_is_signed_in()
