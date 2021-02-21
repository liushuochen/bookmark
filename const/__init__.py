def single(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


@single
class Subcommand(object):
    def __init__(self):
        self.__help = "help"
        self.__version = "version"
        self.__page = "page"
        self.__folder = "folder"

    @property
    def help(self):
        return self.__help

    @property
    def version(self):
        return self.__version

    @property
    def page(self):
        return self.__page

    @property
    def folder(self):
        return self.__folder


@single
class Action(object):
    def __init__(self):
        self.__add = "add"
        self.__drop = "drop"
        self.__help = "help"
        self.__version = "version"
        self.__open = "open"
        self.__edit = "edit"
        self.__list = "list"
        self.__describe = "describe"

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

    @property
    def edit(self):
        return self.__edit

    @property
    def list(self):
        return self.__list

    @property
    def describe(self):
        return self.__describe


action = Action()
subcommand = Subcommand()
