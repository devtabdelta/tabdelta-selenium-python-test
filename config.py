import os

class Config:
    """Configuration settings for the Selenium framework"""

    # Base URL
    BASE_URL = "https://www.douglas.de/de"

    # Browser settings
    BROWSER = "chrome"  # Change to "firefox" if needed
    HEADLESS_MODE = False  # Set to True for headless execution

    IMPLICIT_WAIT = 10  # Seconds
    EXPLICIT_WAIT = 15  # Seconds

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_DATA_PATH = os.path.join(BASE_DIR, "test_data", "test_data.xlsx")  # Path to Excel test data

    ENABLE_ALLURE_REPORT = True  # Set to False if you don't want Allure reporting

    LOG_LEVEL = "INFO"  # Change to "DEBUG" for more logs

    ACCEPT_COOKIES = True  # Set to False if cookies should not be handled

