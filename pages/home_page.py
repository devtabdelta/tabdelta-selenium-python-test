from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    #COOKIE_ACCEPT_BTN = (By.XPATH, "//button[contains(text(),'Accept')]")
    PERFUME_MENU = (By.XPATH, "//a[normalize-space()='PARFUM']")

    def accept_cookies(self):
        """Handles clicking the 'Accept Cookies' button inside Shadow DOM"""

        try:
            # Locate the shadow host (the element that contains shadow root)
            shadow_host = self.driver.find_element(By.CSS_SELECTOR,
                                                   "#usercentrics-root")

            # Get shadow root using JavaScript
            shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)

            # Find the 'Accept Cookies' button inside shadow DOM
            accept_button = shadow_root.find_element(By.CSS_SELECTOR, ".sc-dcJsrY.eIFzaz")

            # Wait for the button to be clickable and click
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(accept_button))
            accept_button.click()
            print("✅ Accept Cookies button clicked successfully!")

        except Exception as e:
            print(f"⚠️ Unable to click Accept Cookies button: {e}")

    def __init__(self, driver):
        super().__init__(driver)


    def navigate_to_perfume(self):
        """Navigates to the perfume menu."""
        self.click_element(self.PERFUME_MENU)
