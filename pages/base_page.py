from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        """Wait for an element to be clickable and then click."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Wait for an element to be visible and enter text."""
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        """Retrieve the text of an element."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        """Check if an element is visible on the page."""
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
