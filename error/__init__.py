class BaseError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidActionError(BaseError):
    def __str__(self):
        return "Invalid action: %s" % self.message


class AddError(BaseError):
    def __str__(self):
        return "Action error: %s" % self.message


class PageNotFoundError(BaseError):
    def __str__(self):
        return "Page not found: %s" % self.message
