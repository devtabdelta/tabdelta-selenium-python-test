import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import Config


@pytest.fixture(scope="function")
def setup():
    """Setup and teardown for Selenium WebDriver using ChromeDriver Manager"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(service=service, options=options)  # Launch Chrome
    driver.implicitly_wait(Config.IMPLICIT_WAIT)  # Set implicit wait
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver  # Provide the driver instance to tests
    driver.quit()  # Close browser after test execution
