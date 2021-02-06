import datetime
from logger.style import style


class Logger(object):
    def __init__(self, output=True, path=None):
        self.__output = output
        self.__path = path

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @staticmethod
    def combine(log, print_type, font, background):
        if print_type is None:
            return log

        if background is None:
            return "\033[%s;%sm%s\033[0m" % (print_type, font, log)
        else:
            return "\033[%s;%s;%sm%s\033[0m" % (print_type, font, background, log)

    def info(self, message, print_type=None, font=None, background=None):
        if ((font is not None) or (background is not None)) and \
                print_type is None:
            print_type = style.type.default
        color_message = self.combine(message, print_type, font, background)

        title = "[%s] [INFO]" % str(datetime.datetime.now())
        color_log = title + " " + color_message
        log = title + " " + message
        if self.output:
            print(color_log)

        if self.path is not None:
            with open(self.path, "a") as file:
                file.write(log)

    def error(self, message, print_type=None, font=None, background=None):
        if ((font is not None) or (background is not None)) and \
                print_type is None:
            print_type = style.type.default
        color_message = self.combine(message, print_type, font, background)

        title = "[%s] [ERROR]" % str(datetime.datetime.now())
        color_log = title + " " + color_message
        log = title + " " + message
        print(color_log)

        if self.path is not None:
            with open(self.path, "a") as file:
                file.write(log)

    def warn(self, message, print_type=None, font=None, background=None):
        if ((font is not None) or (background is not None)) and \
                print_type is None:
            print_type = style.type.default
        color_message = self.combine(message, print_type, font, background)

        title = "[%s] [WARNING]" % str(datetime.datetime.now())
        color_log = title + " " + color_message
        log = title + " " + message
        if self.output:
            print(color_log)

        if self.path is not None:
            with open(self.path, "a") as file:
                file.write(log)

    def debug(self, message, print_type=None, font=None, background=None):
        if ((font is not None) or (background is not None)) and \
                print_type is None:
            print_type = style.type.default
        color_message = self.combine(message, print_type, font, background)

        title = "[%s] [DEBUG]" % str(datetime.datetime.now())
        color_log = title + " " + color_message
        log = title + " " + message
        if self.output:
            print(color_log)

        if self.path is not None:
            with open(self.path, "a") as file:
                file.write(log)

    def console(self, message):
        print(message)
        if self.path is not None:
            with open(self.path, "a") as file:
                file.write(message)


# default logger
logger = Logger()
