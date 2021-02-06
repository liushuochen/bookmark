import util
import datetime
from cmd.base import Base
from error import PageNotFoundError


class Edit(Base):
    def __init__(self, name, url, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.name = name
        self.url = url
        self.path = util.path_join(name + ".json")
