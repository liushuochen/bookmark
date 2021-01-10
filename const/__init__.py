def single(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


@single
class Action(object):
    def __init__(self):
        self.__add = "add"
        self.__drop = "drop"
        self.__help = "help"
        self.__version = "version"
        self.__open = "open"

    @property
    def add(self):
        return self.__add

    @property
    def drop(self):
        return self.__drop

    @property
    def help(self):
        return self.__help

    @property
    def version(self):
        return self.__version

    @property
    def open(self):
        return self.__open


action = Action()
