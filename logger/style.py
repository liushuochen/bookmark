class PrintType(object):
    def __init__(self):
        self.__default = "0"
        self.__highlight = "1"
        self.__underline = "4"
        self.__flash = "5"

    @property
    def default(self):
        return self.__default

    @property
    def highlight(self):
        return self.__highlight

    @property
    def underline(self):
        return self.__underline

    @property
    def flash(self):
        return self.__flash


class Color(object):
    def __init__(self):
        self._black = 30
        self._red = 31
        self._green = 32
        self._yellow = 33
        self._blue = 34
        self._purple = 35
        self._cyan = 36
        self._white = 37


class FontColor(Color):
    def __init__(self):
        Color.__init__(self)

    @property
    def black(self):
        return str(self._black)

    @property
    def red(self):
        return str(self._red)

    @property
    def green(self):
        return str(self._green)

    @property
    def yellow(self):
        return str(self._yellow)

    @property
    def blue(self):
        return str(self._blue)

    @property
    def purple(self):
        return str(self._purple)

    @property
    def cyan(self):
        return str(self._cyan)

    @property
    def white(self):
        return str(self._white)


class BackgroundColor(Color):
    def __init__(self):
        Color.__init__(self)

    @property
    def black(self):
        return str(self._black + 10)

    @property
    def red(self):
        return str(self._red + 10)

    @property
    def green(self):
        return str(self._green + 10)

    @property
    def yellow(self):
        return str(self._yellow + 10)

    @property
    def blue(self):
        return str(self._blue + 10)

    @property
    def purple(self):
        return str(self._purple + 10)

    @property
    def cyan(self):
        return str(self._cyan + 10)

    @property
    def white(self):
        return str(self._white + 10)


class Style(object):
    def __init__(self):
        self.type = PrintType()
        self.font = FontColor()
        self.background = BackgroundColor()

    def __repr__(self):
        return "log style"

    __str__ = __repr__


style = Style()
