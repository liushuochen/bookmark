import util
import error
import json
import webbrowser
from cmd.page import PageAdd
from cmd.help import Help
from cmd.version import Version


def help_doc(param):
    return Help()


def get_version(param):
    return Version()


def add_page(param):
    name = param.get("action_value", None)
    if name is None:
        raise error.AddError("missing name request")

    url = param.get("url", None)
    if url is None:
        raise error.AddError("missing url request")

    debug = param.get("debug", False)
    file = param.get("path", None)
    return PageAdd(name, url, debug, file)


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
