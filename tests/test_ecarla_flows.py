import os
import time
import pytest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchModal, SearchResultsPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage

EMAIL = os.getenv("ECARLA_EMAIL")
PASSWORD = os.getenv("ECARLA_PASSWORD")

@pytest.mark.order(1)
def test_open_homepage(driver, base_url):
    home = HomePage(driver)
    home.open_home(base_url)
    assert "ecarla" in driver.current_url.lower()

@pytest.mark.order(2)
def test_login_success(driver, base_url):
    if not EMAIL or not PASSWORD:
        pytest.skip("ECARLA_EMAIL/ECARLA_PASSWORD not set")
    home = HomePage(driver)
    home.open_home(base_url)
    home.go_to_login()
    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)
    assert home.exists(By.CSS_SELECTOR, ".header-top__block--user a.header-top__link")

@pytest.mark.order(3)
def test_search_by_brand(driver, base_url):
    home = HomePage(driver)
    home.open_home(base_url)
    home.open_search_modal()
    search = SearchModal(driver)
    search.search("Rainbow")
    results = SearchResultsPage(driver)
    assert results.exists(By.CSS_SELECTOR, ".products-list .product-miniature")

@pytest.mark.order(4)
def test_search_by_name(driver, base_url):
    home = HomePage(driver)
    home.open_home(base_url)
    driver.get(base_url)
    home.open_search_modal()
    search = SearchModal(driver)
    search.search("kolczyki")
    results = SearchResultsPage(driver)
    assert results.exists(By.CSS_SELECTOR, ".products-list .product-miniature")

@pytest.mark.order(5)
def test_sort_by_price_ascending(driver, base_url):
    driver.get(f"{base_url}/255-bizuteria")
    category = CategoryPage(driver)
    category.sort_by_visible_text("Cena, rosnąco")
    assert category.exists(By.CSS_SELECTOR, "#js-product-list .product-miniature")

@pytest.mark.order(6)
def test_sort_by_price_descending(driver, base_url):
    driver.get(f"{base_url}/255-bizuteria")
    category = CategoryPage(driver)
    category.sort_by_visible_text("Cena, malejąco")
    assert category.exists(By.CSS_SELECTOR, "#js-product-list .product-miniature")

@pytest.mark.order(7)
def test_sort_by_name_A_Z(driver, base_url):
    driver.get(f"{base_url}/255-bizuteria")
    category = CategoryPage(driver)
    category.sort_by_visible_text("Nazwa, A do Z")
    assert category.exists(By.CSS_SELECTOR, "#js-product-list .product-miniature")

@pytest.mark.order(8)
def test_sort_by_name_Z_A(driver, base_url):
    driver.get(f"{base_url}/255-bizuteria")
    category = CategoryPage(driver)
    category.sort_by_visible_text("Nazwa, Z do A")
    assert category.exists(By.CSS_SELECTOR, "#js-product-list .product-miniature")

@pytest.mark.order(9)
def test_open_product_and_add_to_cart(driver, base_url):
    driver.get(f"{base_url}/search-result?search_query=kolczyki")
    results = SearchResultsPage(driver)
    results.open_first_product()
    product = ProductPage(driver)
    product.add_to_cart()
    cart_present = HomePage(driver).exists(By.CSS_SELECTOR, "#blockcart-modal, .cart-dropdown__content")
    assert cart_present 