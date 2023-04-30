from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_NAME = (By.XPATH, "//tr/td[@class='product-name']")
    COUPON_CODE = (By.ID, "coupon_code")
    APPLY_COUPON = (By.NAME, "apply_coupon")
    APPLIED_COUPON_MESSAGE_SUCCESS = (By.XPATH, "//div[@class = 'woocommerce-message']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//div[@class = 'wc-proceed-to-checkout']")