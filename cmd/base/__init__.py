from logger import Logger


class Base(object):
    def __init__(self, debug, log_file_path):
        self.logger = Logger(debug=debug, path=log_file_path)
        self.log_file_path = log_file_path
