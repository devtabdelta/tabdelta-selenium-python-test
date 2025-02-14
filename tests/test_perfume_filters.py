import pytest
from pages.home_page import HomePage
from pages.perfume_page import PerfumePage
from utils.excel_reader import ExcelReader
from utils.screenshot import Screenshot
from utils.logger import Logger

logger = Logger.setup_logger()

@pytest.mark.parametrize("make, for_who, verantwortung", ExcelReader.get_test_data("./test_data/test_data.xlsx", "Filters"))
def test_filter_perfume(setup, make, for_who, verantwortung):
    """
    Test applying different perfume filters using data-driven testing.
    """
    driver = setup
    home = HomePage(driver)
    perfume = PerfumePage(driver)

    try:
        logger.info("Test Started: Navigating to Perfume Page")


        home.accept_cookies()
        home.navigate_to_perfume()
        logger.info("Navigated to Perfume Menu Successfully")
        print(make)
        make_filters = make.split(",")
        logger.info(make_filters)
        perfume.select_make_filters(make_filters)


        if for_who == "Yes":
            perfume.apply_for_who_filter()
            logger.info("Applied 'Für Wen' filter")

        if verantwortung == "Yes":
            perfume.apply_responsibility_filter()
            logger.info("Applied 'Verantwortung' filter")



    except Exception as e:
        logger.error(f"Test Failed: {e}")
        Screenshot.take_screenshot(driver, "test_filter_perfume")
        assert False, f"Test Failed due to error: {e}"

    logger.info("Test Completed Successfully")
