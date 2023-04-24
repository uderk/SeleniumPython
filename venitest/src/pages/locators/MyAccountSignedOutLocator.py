from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:
    #Login part of the page
    LOGIN_USERNAME = (By.ID, 'username')
    PASSWORD_LOGIN = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    #Registration part of the page
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="register"]')
