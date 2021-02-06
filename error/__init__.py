class BaseError(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        if not self.message.endswith("."):
            self.message = self.message + "."
        return self.message

    __str__ = __repr__


class InvalidSubcommandError(BaseError):
    def __init__(self, subcommand):
        BaseError.__init__(self, "Invalid subcommand `%s`" % subcommand)


class InvalidActionError(BaseError):
    def __init__(self, action):
        BaseError.__init__(self, "Invalid action `%s`" % action)


class InvalidParamError(BaseError):
    def __init__(self, param):
        BaseError.__init__(self, "Invalid param `%s`" % param)


class AddError(BaseError):
    pass


class PageNotFoundError(BaseError):
    def __init__(self, page):
        BaseError.__init__(self, "Page %s not found" % page)
