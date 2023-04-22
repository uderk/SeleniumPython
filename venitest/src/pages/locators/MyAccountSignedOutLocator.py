from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:
    LOGIN_USERNAME = (By.ID, 'username')
    PASSWORD_LOGIN = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')
