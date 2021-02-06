import util
from cmd.base import Base


class Drop(Base):
    def __init__(self, name, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.name = name

    def execute(self):
        self.check(self.name)
        self.drop()

    def drop(self):
        path = util.path_join(util.storage_path(), self.name + ".json")
        util.delete_file(path)
