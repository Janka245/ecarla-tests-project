from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    """Home page elements and actions (header region)."""

    SEARCH_TOGGLER = (By.CSS_SELECTOR, "a.search-toggler.header-top__link")
    LOGIN_LINK = (By.CSS_SELECTOR, ".header-top__block--user a.header-top__link")

    def open_home(self, base_url: str):
        """Navigate to the site root."""
        self.open(base_url)

    def open_search_modal(self):
        """Open the search modal from the header."""
        self.click(*self.SEARCH_TOGGLER)

    def go_to_login(self):
        """Navigate to the login page via the header user icon."""
        self.click(*self.LOGIN_LINK) 