import pytest
from venitest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:
    username = 'efrergegef'
    password = 'rfse'
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        # go to my account
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        # type username and password
        my_account.input_login_username(self.username)
        my_account.input_login_password(self.password)
        # click login
        my_account.click_login_button()
        #verify error message
        my_account.wait_until_error_is_displayed("Error: The username {} is not registered on this site. If you are "
                                                 "unsure of your username, try your email address instead.".format(
            self.username))