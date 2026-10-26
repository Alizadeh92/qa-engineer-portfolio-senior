"""Sanitised page-object excerpt adapted from my practice-test workflow."""

import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .web_element_wrapper import WebElement


class PracticePage:
    """Page object for practice-test configuration."""

    # Configure this variable for an authorised test environment.
    BASE_URL = os.environ.get("PRACTICE_CONFIGURATION_URL", "")

    def __init__(self, driver, subject_code, topics):
        self.driver = driver
        self.subject_code = subject_code
        self.topics = topics

        self.url = self._build_url()
        self.question_source_dropdown = WebElement(
            driver,
            locator='select[value="All"]',
            locator_type="css",
        )
        self.question_source_option = WebElement(
            driver,
            locator="div.question-source-option",
            locator_type="css",
        )
        self.question_count = WebElement(
            driver,
            locator="div.question-count",
            locator_type="css",
        )

    def _build_url(self):
        if not self.BASE_URL:
            raise RuntimeError(
                "Set PRACTICE_CONFIGURATION_URL for your authorised test environment"
            )
        return (
            f"{self.BASE_URL}?topics={self.topics}"
            f"&view=filters&subject={self.subject_code}"
        )

    def open(self):
        self.driver.get(self.url)

    def wait_until_question_count_is_visible(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, self.question_count.locator)
            )
        )
