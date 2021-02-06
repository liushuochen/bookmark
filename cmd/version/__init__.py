import util
from cmd.base import Base


class Version(Base):
    def __init__(self):
        Base.__init__(self, None, None)
        self.path = util.path_join("cmd/version/bm.version")

    def execute(self):
        with open(self.path, "r") as file:
            version = file.read().strip()
        self.logger.console(version)
