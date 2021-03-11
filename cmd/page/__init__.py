import util
import json
import datetime
import os
import threading
import webbrowser
from prettytable import PrettyTable
from cmd.base import Base
from error import PageExistError, PageNotFoundError


class PageEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class PageBase(Base):
    def __init__(self, name, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.name = name

    def exist(self, name, create_storage_path=False):
        self.logger.info("check page %s exists..." % name)
        if create_storage_path:
            util.create_storage_dir()

        return name in util.pages()


class PageAdd(PageBase):
    def __init__(self, name, url, debug, log_file_path):
        PageBase.__init__(self, name, debug, log_file_path)
        self.url = url

    def execute(self):
        if self.exist(self.name, create_storage_path=True):
            raise PageExistError(self.name)
        self.add()

    def add(self):
        path = os.path.join(util.storage_path(), self.name + ".json")
        now = datetime.datetime.now()
        data = {
            "name": self.name,
            "url": self.url,
            "create_time": now,
            "update": {
                "times": 0,
                "time": now
            },
            "use": {
                "times": 0,
                "last_time": None
            }
        }

        with open(path, "w") as page_file:
            page_file.write(json.dumps(data, cls=PageEncoder, indent=4))
        self.logger.info("add page %s successfully" % self.name)


class PageDrop(PageBase):
    def __init__(self, name, debug, log_file_path):
        PageBase.__init__(self, name, debug, log_file_path)

    def execute(self):
        if not self.exist(self.name):
            raise PageNotFoundError(self.name)
        self.drop()

    def drop(self):
        path = util.path_join("pages", self.name + ".json")
        util.delete_file(path)
        self.logger.info("delete page %s successfully" % self.name)


class PageEdit(PageBase):
    def __init__(self, old_name, new_name, url, debug, log_file_path):
        PageBase.__init__(self, old_name, debug, log_file_path)
        self.old_name = old_name
        self.new_name = new_name
        self.url = url

    def execute(self):
        if not self.exist(self.old_name):
            raise PageNotFoundError(self.old_name)
        if self.new_name is not None and self.exist(self.new_name):
            raise PageExistError(self.new_name)
        self.update()

    def path(self):
        old_path = os.path.join(util.storage_path(), self.old_name + ".json")
        if self.new_name is None:
            new_path = None
        else:
            new_path = os.path.join(util.storage_path(), self.new_name + ".json")
        return old_path, new_path

    def update(self):
        old_path, new_path = self.path()
        now = datetime.datetime.now()
        with open(old_path, "r") as page_file:
            data = json.load(page_file)
        if self.new_name is not None:
            data["name"] = self.new_name
        if self.url is not None:
            data["url"] = self.url
        data["update"]["time"] = now
        data["update"]["times"] += 1

        with open(old_path, "w") as page_file:
            page_file.write(json.dumps(data, cls=PageEncoder, indent=4))

        if new_path is not None:
            os.renames(old_path, new_path)
        self.logger.info("edit page %s successfully" % self.new_name)


class PageList(Base):
    def __init__(self, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.pages = dict()

    def execute(self):
        self.get_pages_simple_message()
        self.show_pages()

    def show_pages(self):
        table = PrettyTable()
        table.field_names = ["NAME", "URL"]
        table.align["NAME"] = "l"
        table.align["URL"] = "l"
        for name in self.pages:
            table.add_row([name, self.pages[name]])
        table.border = False
        self.logger.console(table)

    def get_pages_simple_message(self):
        if not os.path.isdir(util.storage_path()):
            return

        name_list = os.listdir(util.storage_path())
        thread_list = []
        for name in name_list:
            if not util.is_json_file(name):
                continue

            thread = threading.Thread(
                target=self._get_simple_message,
                args=(name,),
            )
            thread.start()
            thread_list.append(thread)

        for thread in thread_list:
            thread.join()

    def _get_simple_message(self, page_name):
        path = util.path_join(util.storage_path(), page_name)
        with open(path, "r") as page_file:
            data = json.load(page_file)
        url = data["url"]
        self.pages[page_name.replace(".json", "")] = url


class PageDetail(PageBase):
    def __init__(self, name, log_file_path):
        PageBase.__init__(self, name, False, log_file_path)
        self.details = dict()

    def execute(self):
        if not self.exist(self.name):
            raise PageNotFoundError(self.name)
        self.get_details()
        self.show()

    def show(self):
        table = PrettyTable()
        table.field_names = ["ATTRIBUTE", "VALUE"]
        table.align["ATTRIBUTE"] = "l"
        table.align["VALUE"] = "l"
        rows = [
            ["name", self.details["name"]],
            ["url", self.details["url"]],
            ["create", self.details["create_time"]],
            ["last update", self.details["update"]["time"]],
            ["update times", self.details["update"]["times"]],
            ["use times", self.details["use"]["times"]],
            ["last use", self.details["use"]["last_time"]],
        ]
        table.add_rows(rows)
        table.border = False
        self.logger.console(table)

    def get_details(self):
        path = util.path_join(util.storage_path(), self.name+".json")
        with open(path, "r") as file:
            data = json.load(file)
        self.details = data


class PageOpen(PageBase):
    def __init__(self, name, debug, log_file_path):
        PageBase.__init__(self, name, debug, log_file_path)

    def execute(self):
        if not self.exist(self.name):
            raise PageNotFoundError(self.name)
        self.open()
        self.add_use_count()

    def add_use_count(self):
        path = util.path_join(util.storage_path(), self.name + ".json")
        with open(path, "r") as file:
            data = json.load(file)

        data["use"]["times"] += 1
        data["use"]["last_time"] = datetime.datetime.now()

        with open(path, "w") as page_file:
            page_file.write(json.dumps(data, cls=PageEncoder, indent=4))

    def open(self):
        path = util.path_join(util.storage_path(), self.name+".json")
        with open(path, "r") as file:
            data = json.load(file)
        webbrowser.open(data["url"])
        self.logger.info("open page %s finished." % self.name)
