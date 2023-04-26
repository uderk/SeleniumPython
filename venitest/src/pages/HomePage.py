from venitest.src.helpers.config_helpers import get_base_url
from venitest.src.SeleniumExtended import SeleniumExtended
from venitest.src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def add_first_item_to_chart(self):

        self.sl.wait_and_click(self.ADD_TO_CHART_FIRST_ITEM_BUTTON)

