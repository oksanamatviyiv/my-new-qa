from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage


class CartPage(BasePage):
    URL = "https://rozetka.com.ua/ua/cart/"
    BUY_BTN = (By.CLASS_NAME, "buy-button")
    CART_URL_PART = "/cart"

    # відкриваємо сторінку
    def open(self):
        self.driver.get(self.URL)
        return self

    # Очікуємо, що сторінка завантажиться
    def wait_opened(self):
        self.wait.until(EC.url_contains(self.CART_URL_PART))
        return self

    # Клік на кнопку купити
    def click_buy(self):
        self.wait.until(EC.element_to_be_clickable(self.BUY_BTN)).click()
        return self

    # Перевірка, що сторінка відкрита
    def is_opened(self):
        return self.CART_URL_PART in self.driver.current_url
