import util
from cmd.base import Base


class Help(Base):
    def __init__(self):
        Base.__init__(self, None, None)
        self.path = util.path_join("cmd/help/bookmark_help_doc.txt")

    def execute(self):
        with open(self.path, "r") as doc:
            content = doc.read()
        self.logger.console(content)
