from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DEFAULT_TIMEOUT = 15

class BasePage:
    """Base class for Page Objects providing common Selenium helpers."""

    def __init__(self, driver):
        """Store driver and initialize default WebDriverWait."""
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url: str):
        """Navigate to the given URL and dismiss potential overlays."""
        self.driver.get(url)
        self.dismiss_overlays_if_present()

    def click(self, by: By, selector: str):
        """Wait until element is clickable and perform a native click."""
        self.wait.until(EC.element_to_be_clickable((by, selector))).click()

    def type(self, by: By, selector: str, text: str, clear: bool = True):
        """Type text into a visible element, optionally clearing first."""
        el = self.wait.until(EC.visibility_of_element_located((by, selector)))
        if clear:
            el.clear()
        el.send_keys(text)

    def text_of(self, by: By, selector: str) -> str:
        """Return visible text of an element."""
        return self.wait.until(EC.visibility_of_element_located((by, selector))).text

    def exists(self, by: By, selector: str) -> bool:
        """Check if an element is present in the DOM (not necessarily visible)."""
        try:
            self.wait.until(EC.presence_of_element_located((by, selector)))
            return True
        except Exception:
            return False

    def select_option_by_text(self, by: By, selector: str, text: str):
        """Select option from a <select> by visible text."""
        from selenium.webdriver.support.ui import Select
        el = self.wait.until(EC.element_to_be_clickable((by, selector)))
        Select(el).select_by_visible_text(text)

    def js_click(self, by: By, selector: str):
        """Scroll into view and click an element using JavaScript, useful when native click is intercepted."""
        el = self.wait.until(EC.presence_of_element_located((by, selector)))
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        except Exception:
            pass
        self.driver.execute_script("arguments[0].click();", el)

    def dismiss_overlays_if_present(self):
        """Try to close cookie consent and newsletter popups if present."""
        # Cookiebot close button
        try:
            close_btn = self.driver.find_elements(By.CSS_SELECTOR, "#CybotCookiebotDialog .CybotCookiebotBannerCloseButton")
            if close_btn:
                self.driver.execute_script("arguments[0].click();", close_btn[0])
        except Exception:
            pass
        # Newsletter popup close image button
        try:
            news_close = self.driver.find_elements(By.CSS_SELECTOR, "#popupContainer img[title='close form']")
            if news_close:
                self.driver.execute_script("arguments[0].click();", news_close[0])
        except Exception:
            pass

    def scroll_into_view(self, by: By, selector: str):
        """Scroll the element into view (center alignment)."""
        try:
            el = self.wait.until(EC.presence_of_element_located((by, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        except Exception:
            pass 