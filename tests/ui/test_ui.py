import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адрІесу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()


@pytest.mark.ui
def test_open_and_close_cart_modal():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Open site (or product page if required)
    driver.get("https://rozetka.com.ua/")

    # 2. Click cart button by testid
    cart_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='header-cart-btn']"))
    )
    cart_button.click()
    # time.sleep(3)  # observation / pause

    # 3. Assert overlay
    modal = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='modal-content']")
        )
    )
    assert modal.is_displayed()

    # 4. Close modal by close button
    close_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='modal-close-btn']"))
    )
    close_btn.click()

    # 5. Assert modal disappears
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='modal-content']")
        )
    )

    driver.close()


@pytest.mark.ui
def test_open_cart_from_product_page():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    # відкриваємо сторінку продукту
    driver.get("https://rozetka.com.ua/ua/459901394/p459901394/")
    # Клік на кнопку корзини
    buy_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "buy-button")))
    buy_btn.click()

    driver.quit()


@pytest.mark.ui
def test_parcel_input_default_state():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # відкриваємо сторінку https://tracking.novaposhta.ua/
    driver.get("https://tracking.novaposhta.ua/")

    # Перевіряємо плейсхолдер наявність тексту "Номер посилки"
    parcel_input = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Номер посилки']")
        )
    )
    assert parcel_input.get_attribute("placeholder") == "Номер посилки"

    # Перевіряємо чи пусте значення за замовчуванням
    assert parcel_input.get_attribute("value") == ""

    # Закриваємо браузер
    driver.close()
