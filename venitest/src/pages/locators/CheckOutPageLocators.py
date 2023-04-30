from selenium.webdriver.common.by import By


class CheckOutPageLocators:
    # mandatory_fields
    FIRST_NAME = (By.ID, "billing_first_name")
    LAST_NAME = (By.ID, "billing_last_name")
    COUNTRY = (By.ID, "select2-billing_country-container")
    STREET = (By.ID, "billing_address_1")
    CITY = (By.ID, "billing_city")
    POSTCODE = (By.ID, "billing_postcode")
    PHONE = (By.ID, "billing_phone")
    EMAIL = (By.ID, "billing_email")
    PLACE_ORDER_BUTTON = (By.ID, "place_order")
    COUNTRY_DROPDOWN_INPUT = (By.XPATH, "//input[@class = 'select2-search__field']")
    ORDER_RECEIVED = (By.XPATH, "//h1[contains(text(),'Order received')]")
