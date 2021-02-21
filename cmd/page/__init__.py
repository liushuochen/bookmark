import util
import json
import datetime
import os
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
            "update_time": now,
            "update_times": 0,
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
        data["update_time"] = now
        data["update_times"] += 1

        with open(old_path, "w") as page_file:
            page_file.write(json.dumps(data, cls=PageEncoder, indent=4))

        if new_path is not None:
            os.renames(old_path, new_path)
        self.logger.info("edit page %s successfully" % self.new_name)
