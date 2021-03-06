# install bookmark
# pip freeze > requirements.txt

import util
import os
from configparser import ConfigParser


class RequirementsInstallFailed(Exception):
    def __init__(self):
        self.message = "load requirements failed."

    def __repr__(self):
        return self.message

    __str__ = __repr__


def check(func):
    def wrapper(*args, **kwargs):
        if util.is_install():
            print("bookmark has already install.")
        else:
            func(*args, **kwargs)
        return
    return wrapper


def add_eol(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for index in range(len(result)):
            result[index] += "\n"
        return result
    return wrapper


class Install(object):
    def __init__(self):
        c = ConfigParser()
        c.read(util.path_join(util.root_path(), "config/bookmark.ini"))
        self.bin_py_path = c.get("install", "bin_python_path")
        self.python_cmd = c.get("install", "python_command")
        self.pip_cmd = c.get("install", "pip_command")

    @check
    def run(self):
        files_kwargs_list = [
            {
                "func": self.generate_shell_script,
                "filename": "bookmark.sh",
            },
            {
                "func": self.generate_bin_python_doc,
                "filename": "bookmark",
                "path": "/usr/local/bin/",
            },
        ]
        for kwargs in files_kwargs_list:
            self.create_file(**kwargs)

        try:
            self.install_dependency_module()
        except RequirementsInstallFailed as e:
            print(e)
        else:
            print("install bookmark finished")

    @staticmethod
    def create_file(func, filename, path="local", chmod="777"):
        content = "".join(func())
        with open(filename, "w") as file:
            file.write(content)

        command = "chmod %s %s" % (chmod, filename)
        os.system(command)
        if path != "local" and os.path.isdir(path):
            file_path = os.path.join(path, filename)
            command = "mv %s %s" % (filename, file_path)
            os.system(command)

    @staticmethod
    def shell_script_path():
        return util.path_join(util.root_path(), "bookmark.sh")

    @add_eol
    def generate_bin_python_doc(self):
        python_script_list = [
            "#!%s" % self.bin_py_path,
            "import sys",
            "import os",
            "",
            "",
            "if __name__ == '__main__':",
            "    args = \" \".join(sys.argv[1:])",
            "    path = \"%s\"" % self.shell_script_path(),
            "    command = \"%s %s\" % (path, args)",
            "    os.system(command)"
        ]
        return python_script_list

    @add_eol
    def generate_shell_script(self):
        shell_script_list = [
            "base_dir=$(cd $(dirname $0) && pwd)",
            "",
            "cd \"${base_dir}\"",
            "%s bookmark.py $@" % self.python_cmd,
        ]
        return shell_script_list

    @staticmethod
    def install_dependency_module():
        path = os.path.join(util.root_path(), "requirements.txt")
        command = "pip install -r %s > /dev/null 2>&1" % path
        if os.system(command) != 0:
            raise RequirementsInstallFailed()


if __name__ == '__main__':
    Install().run()
