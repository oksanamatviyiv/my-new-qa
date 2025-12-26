from selenium.webdriver.chrome.webdriver import WebDriver
from modules.ui.page_objects.track_page import TrackPage
from modules.ui.page_objects.cart_page import CartPage
from modules.ui.page_objects.header import Header
from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object(driver: WebDriver):
    # створення об'єкту сторінки
    sign_in_page = SignInPage(driver)

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui
def test_open_and_close_cart_modal(driver: WebDriver):
    # відкриваємо сторінку
    driver.get("https://rozetka.com.ua/")
    header = Header(driver)

    # Відкриваємо модальне вікно кошика
    header.open_cart_modal()

    # Перевіряємо, що модальне вікно кошика відображається
    assert header.cart_modal_is_visible()

    # Закриваємо модальне вікно кошика
    header.close_cart_modal()


@pytest.mark.ui
def test_open_cart_from_product_page(driver: WebDriver):
    driver.get("https://rozetka.com.ua/ua/459901394/p459901394/")
    cart = CartPage(driver)
    # Відкриваємо корзину
    cart.open().wait_opened()
    assert cart.is_opened()


@pytest.mark.ui
def test_parcel_input_default_state(driver: WebDriver):
    parcel_input = TrackPage(driver).open()
    # Перевіряємо текст плейсхолдера
    assert parcel_input.placeholder_text() == "Номер посилки"
    # Перевіряємо чи пусте значення за замовчуванням
    assert parcel_input.value_text() == ""
