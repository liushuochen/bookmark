import util
import json
import datetime
import os
from cmd.base import Base
from error import AddError


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
            raise AddError("Page %s has already exist" % self.name)

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
            json_file.write(json.dumps(data))
        self.logger.info("add page %s successfully" % self.name)
