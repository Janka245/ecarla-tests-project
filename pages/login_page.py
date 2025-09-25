from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Login page form interactions."""

    EMAIL_INPUT = (By.CSS_SELECTOR, "#login-form input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#login-form input[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login-form button[data-link-action='sign-in']")

    def login(self, email: str, password: str):
        """Fill credentials and submit the login form."""
        self.type(*self.EMAIL_INPUT, text=email)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.SUBMIT_BUTTON) 