from cmd.base import Base


class Default(Base):
    def __init__(self, subcommand, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.subcommand = subcommand

    def execute(self):
        self.logger.error("Unsupported command `%s`" % self.subcommand)
