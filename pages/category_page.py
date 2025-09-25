from selenium.webdriver.common.by import By
from .base_page import BasePage

class CategoryPage(BasePage):
    """Category page interactions: sorting and sidebar filters."""

    # Sort select with availability and name/price options
    SORT_SELECT = (By.CSS_SELECTOR, "div.sort_container select.custom-select")
    # Brand filter group
    BRAND_GROUP_TITLE = (By.CSS_SELECTOR, "#PM_ASCriterionsGroupTitle_1_5 .PM_ASCriterionsGroupName")
    BRAND_FIRST_LINK = (By.CSS_SELECTOR, "#PM_ASCriterionGroupCheckbox_1_5 li:first-child label a.PM_ASLabelLink")

    def sort_by_visible_text(self, text: str):
        """Choose a sort option by visible text."""
        self.dismiss_overlays_if_present()
        self.select_option_by_text(*self.SORT_SELECT, text=text)

    def filter_by_first_brand(self):
        """Expand brand group if needed and apply the first brand filter."""
        self.dismiss_overlays_if_present()
        # Expand the brand group if collapsible
        try:
            self.scroll_into_view(*self.BRAND_GROUP_TITLE)
            self.js_click(*self.BRAND_GROUP_TITLE)
        except Exception:
            pass
        # Click first brand link
        try:
            self.scroll_into_view(*self.BRAND_FIRST_LINK)
            self.js_click(*self.BRAND_FIRST_LINK)
            return
        except Exception:
            pass
        # Fallback: click any brand link
        try:
            self.js_click(By.CSS_SELECTOR, "#PM_ASCriterionGroupCheckbox_1_5 a.PM_ASLabelLink")
        except Exception:
            pass 