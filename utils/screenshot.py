import os
import time

class Screenshot:
    @staticmethod
    def take_screenshot(driver, test_name):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"./screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(file_name)
        return file_name
