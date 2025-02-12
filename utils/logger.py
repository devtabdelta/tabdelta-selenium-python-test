import logging

class Logger:
    @staticmethod
    def setup_logger():
        logging.basicConfig(
            filename="./reports/test_execution.log",
            format="%(asctime)s - %(levelness)s - %(message)s",
            level=logging.INFO
        )
        return logging.getLogger()
