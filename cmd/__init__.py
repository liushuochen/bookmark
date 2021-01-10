import util
import error
import json
import webbrowser


class ActionBase(object):
    def __init__(self):
        self.__tasks = []
    
    @property
    def task_list(self):
        return self.__tasks
    
    def registry(self, task, index=-1):
        if index == -1:
            self.task_list.append(task)
        else:
            self.task_list.insert(index, task)
    
    def execute(self):
        for subtask in self.task_list:
            subtask()
    

class Add(ActionBase):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url

        self.registry(self.check)
        self.registry(self.add)

    def check(self):
        if not util.is_dir(util.storage_path()):
            util.create_storage_dir(util.storage_path())

        if self.name in util.pages():
            raise error.AddError("Page %s has already exist" % self.name)

    def add(self):
        path = util.path_join(util.storage_path(), self.name + ".json")
        data = {
            "name": self.name,
            "url": self.url,
        }

        with open(path, "w") as json_file:
            json_file.write(json.dumps(data))


class Drop(ActionBase):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.path = util.path_join(util.storage_path(), name + ".json")

        self.registry(self.check)
        self.registry(self.drop)

    def check(self):
        if not util.file_exist(self.path):
            raise error.PageNotFoundError("page %s not found." % self.name)

    def drop(self):
        util.delete_file(self.path)


class Open(ActionBase):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url

        self.registry(self.check)
        self.registry(self.open)

    def check(self):
        if self.name is not None and self.name not in util.pages():
            raise error.PageNotFoundError("%s do not exist." % self.name)

    def open(self):
        if self.name is not None:
            path = util.path_join(util.storage_path(), self.name + ".json")
            with open(path, "r") as json_file:
                data = json.load(json_file)
            webbrowser.open(data["url"])
        else:
            webbrowser.open(self.url)
