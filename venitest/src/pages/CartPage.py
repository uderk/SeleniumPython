from venitest.src.helpers.config_helpers import get_base_url
from venitest.src.SeleniumExtended import SeleniumExtended

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    pass
