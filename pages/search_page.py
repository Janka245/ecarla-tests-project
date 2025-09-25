from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SearchModal(BasePage):
    """Search modal interactions (input and submit)."""

    INPUT = (By.CSS_SELECTOR, ".ybc_searchbox input.search_query")
    SUBMIT = (By.CSS_SELECTOR, ".ybc_searchbox button[type='submit']")

    def search(self, query: str):
        """Type a query and submit the search form."""
        # Poczekaj aż modal będzie w pełni załadowany i input będzie widoczny
        self.wait.until(EC.visibility_of_element_located(self.INPUT))
        self.dismiss_overlays_if_present()
        self.type(*self.INPUT, text=query)
        # Poczekaj aż przycisk submit będzie klikalny
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        self.click(*self.SUBMIT)
        self.dismiss_overlays_if_present()

class SearchResultsPage(BasePage):
    """Search results list interactions (navigation, quick add)."""

    PRODUCT_TITLES = (By.CSS_SELECTOR, ".products-list .product-miniature__title a")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".product-miniature__actions button.add-to-cart")

    def open_first_product(self):
        """Open details of the first product in the results list."""
        self.dismiss_overlays_if_present()
        self.scroll_into_view(By.CSS_SELECTOR, ".products-list .product-miniature .product-miniature__title a")
        self.js_click(By.CSS_SELECTOR, ".products-list .product-miniature .product-miniature__title a")

    def add_first_to_cart(self):
        """Attempt quick add-to-cart from results; fallback to product page add if needed."""
        self.dismiss_overlays_if_present()
        if self.exists(*self.ADD_TO_CART_BUTTONS):
            self.scroll_into_view(*self.ADD_TO_CART_BUTTONS)
            self.js_click(*self.ADD_TO_CART_BUTTONS)
        else:
            # Fallback: open first product and add from product page
            self.open_first_product()
            from .product_page import ProductPage
            ProductPage(self.driver).add_to_cart()