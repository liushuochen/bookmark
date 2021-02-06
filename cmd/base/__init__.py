import util
from logger import Logger
from error import PageNotFoundError


class Base(object):
    def __init__(self, output, log_file_path):
        self.logger = Logger(output=output, path=log_file_path)
        self.log_file_path = log_file_path
