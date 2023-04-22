import pytest
@pytest.mark.usefixtures("init_driver")
class TestDummy:

    def test_dummy_func(self):
        print("I am dummy test")
        self.driver.get("https://translate.google.com/")
