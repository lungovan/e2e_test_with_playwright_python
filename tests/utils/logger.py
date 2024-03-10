import logging
from tests.utils.date_helper import get_current_time_str


class TestLogger:
    def __init__(self, test_name):
        self.logger = logging.getLogger(test_name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(f'test_artifacts/test_logs/{test_name}_{get_current_time_str()}.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)