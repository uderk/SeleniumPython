from selenium.webdriver.common.by import By

class HeaderLocators:

    CART_RIGHT_HEADER = (By.XPATH, "//li/a[contains(text(),'Cart')]")
    CART_ITEM_COUNT = (By.XPATH, "//span[contains(text(),'item')]")