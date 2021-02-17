import util
import json
import datetime
import os
from cmd.base import Base
from error import AddError, PageNotFoundError


class PageAdd(Base):
    def __init__(self, name, url, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.name = name
        self.url = url

    def execute(self):
        task_list = [
            self.check_exist,
            self.add,
        ]
        for task in task_list:
            task()

    def check_exist(self):
        self.logger.info("check page %s exists..." % self.name)
        if not os.path.isdir(util.storage_path()):
            util.create_storage_dir(util.storage_path())

        if self.name in util.pages():
            raise AddError("page %s has already exist" % self.name)

    def add(self):
        path = os.path.join(util.storage_path(), self.name + ".json")
        now = str(datetime.datetime.now())
        data = {
            "name": self.name,
            "url": self.url,
            "create_time": now,
            "update_time": now,
            "update_times": 0,
        }

        with open(path, "w") as json_file:
            json_file.write(json.dumps(data, indent=4))
        self.logger.info("add page %s successfully" % self.name)


class PageDrop(Base):
    def __init__(self, name, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.name = name

    def execute(self):
        self.check()
        self.drop()

    def check(self):
        self.logger.info("check page %s exists..." % self.name)
        if not os.path.isdir(util.storage_path()) or self.name not in util.pages():
            raise PageNotFoundError(self.name)

    def drop(self):
        path = util.path_join("pages", self.name + ".json")
        util.delete_file(path)
        self.logger.info("delete page %s successfully" % self.name)


class PageEdit(Base):
    def __init__(self, name, url, debug, log_file_path):
        Base.__init__(self, debug, log_file_path)
        self.name = name
        self.url = url
