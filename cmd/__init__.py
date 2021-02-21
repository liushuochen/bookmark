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

    debug = param.get("debug", False)
    file = param.get("path", None)
    return cmd.page.PageDetail(name, file)



# class Open(ActionBase):
#     def __init__(self, name, url):
#         super().__init__()
#         self.name = name
#         self.url = url
#
#         self.registry(self.check)
#         self.registry(self.open)
#
#     def check(self):
#         if self.name is not None and self.name not in util.pages():
#             raise error.PageNotFoundError("%s do not exist." % self.name)
#
#     def open(self):
#         if self.name is not None:
#             path = util.path_join(self.name + ".json")
#             with open(path, "r") as json_file:
#                 data = json.load(json_file)
#             webbrowser.open(data["url"])
#         else:
#             webbrowser.open(self.url)
