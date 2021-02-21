import error
import cmd.page
from cmd.help import Help
from cmd.version import Version
from cmd.default import Default


def default_scmd(subcommand, param):
    debug = param.get("debug", False)
    file = param.get("path", None)
    return Default(subcommand, debug, file)


def help_doc(param):
    return Help()


def get_version(param):
    return Version()


def add_page(param):
    name = param.get("action_value", None)
    if name is None:
        raise error.MissingActionError(name)

    url = param.get("url", None)
    if url is None:
        raise error.MissingActionError(url)

    debug = param.get("debug", False)
    file = param.get("path", None)
    return cmd.page.PageAdd(name, url, debug, file)


def drop_page(param):
    name = param.get("action_value", None)
    if name is None:
        raise error.MissingActionError(name)

    debug = param.get("debug", False)
    file = param.get("path", None)
    return cmd.page.PageDrop(name, debug, file)


def edit_page(param):
    name = param.get("action_value", None)
    if name is None:
        raise error.MissingActionError(name)

    new_name = param.get("name", None)
    new_url = param.get("url", None)
    debug = param.get("debug", False)
    file = param.get("path", None)
    return cmd.page.PageEdit(name, new_name, new_url, debug, file)


def list_page(param):
    debug = param.get("debug", False)
    file = param.get("path", None)
    return cmd.page.PageList(debug, file)


def get_page(param):
    name = param.get("action_value", None)
    if name is None:
        raise error.MissingActionError(name)

    file = param.get("path", None)
    return cmd.page.PageDetail(name, file)


def open_page(param):
    name = param.get("action_value", None)
    if name is None:
        raise error.MissingActionError(name)

    debug = param.get("debug", False)
    file = param.get("path", None)
    return cmd.page.PageOpen(name, debug, file)
