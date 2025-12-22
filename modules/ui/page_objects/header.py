from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Header:
    CART_BTN = (By.CSS_SELECTOR, "[data-testid='header-cart-btn']")
    MODAL = (By.CSS_SELECTOR, "[data-testid='modal-content']")
    MODAL_CLOSE = (By.CSS_SELECTOR, "[data-testid='modal-close-btn']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_cart_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_BTN)).click()

    def cart_modal_is_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.MODAL))

    def close_cart_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.MODAL_CLOSE)).click()
        self.wait.until(EC.invisibility_of_element_located(self.MODAL))
