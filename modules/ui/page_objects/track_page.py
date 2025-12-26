from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage


class TrackPage(BasePage):
    URL = "https://tracking.novaposhta.ua/"
    PARCEL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Номер посилки']")

    # відкриваємо сторінку
    def open(self):
        self.driver.get(self.URL)
        return self

    # Елемент поля вводу номера посилки
    def parcel_input(self):
        return self.wait.until(EC.presence_of_element_located(self.PARCEL_INPUT))

    # Текст плейсхолдера
    def placeholder_text(self):
        return self.parcel_input().get_attribute("placeholder")

    # Значення в полі вводу
    def value_text(self):
        return self.parcel_input().get_attribute("value")
