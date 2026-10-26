"""Sanitised excerpt adapted from a reusable Selenium helper in my project."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    """Small wrapper that centralises locator handling and common UI actions."""

    LOCATOR_TYPES = {
        "id": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "class": By.CLASS_NAME,
        "link_text": By.LINK_TEXT,
    }

    def __init__(self, driver, locator, locator_type="css", timeout=10):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type
        self.timeout = timeout

    def _locator(self):
        try:
            by = self.LOCATOR_TYPES[self.locator_type]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported locator type: {self.locator_type}"
            ) from exc
        return by, self.locator

    def get_element(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self._locator())
        )

    def find_element(self):
        return self.driver.find_element(*self._locator())

    def find_elements(self):
        return self.driver.find_elements(*self._locator())

    def click(self):
        self.get_element().click()

    def get_text(self):
        return self.get_element().text

    def send_keys(self, text):
        self.get_element().send_keys(text)

    def is_displayed(self):
        try:
            return self.get_element().is_displayed()
        except Exception:
            return False

    def exists(self):
        try:
            self.find_element()
            return True
        except NoSuchElementException:
            return False

    def has_element_count(self, expected_count):
        return len(self.find_elements()) == expected_count
