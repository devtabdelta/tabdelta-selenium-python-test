import pytest
from selenium import webdriver
from utils.config import Config
from utils.logger import Logger


@pytest.fixture(scope="class")
def setup():
    logger = Logger.setup_logger()
    logger.info("Initializing WebDriver...")

    if Config.BROWSER == "chrome":
        driver = webdriver.Chrome(Config.DRIVER_PATH)
    elif Config.BROWSER == "firefox":
        driver = webdriver.Firefox(Config.DRIVER_PATH)
    else:
        raise Exception("Unsupported Browser!")

    driver.maximize_window()
    driver.get(Config.BASE_URL)

    yield driver  # Return driver instance

    logger.info("Closing WebDriver...")
    driver.quit()
