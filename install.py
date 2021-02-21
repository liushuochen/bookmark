# install bookmark
import util
import os
from configparser import ConfigParser


def check(func):
    def wrapper(*args, **kwargs):
        if util.is_install():
            print("bookmark has already install.")
        else:
            func(*args, **kwargs)
        return
    return wrapper


def shell_script_path():
    return util.path_join(util.root_path(), "bookmark.sh")


def generate_bin_python_doc():
    conf = ConfigParser()
    conf.read(util.path_join(util.root_path(), "config/bookmark.ini"))
    bin_py_path = conf.get("install", "bin_python_path")
    python_script_list = [
        "#!%s" % bin_py_path,
        "import sys",
        "import os",
        "",
        "",
        "if __name__ == '__main__':",
        "    args = \" \".join(sys.argv[1:])",
        "    path = \"%s\"" % shell_script_path(),
        "    command = \"%s %s\" % (path, args)",
        "    os.system(command)"
    ]
    return python_script_list


@check
def install():
    python_script_list = generate_bin_python_doc()
    for index in range(len(python_script_list)):
        python_script_list[index] += "\n"
    with open("bookmark", "w") as py_file:
        py_file.write("".join(python_script_list))

    os.system("chmod 777 bookmark")
    os.system("mv bookmark /usr/local/bin/bookmark")
    print("install bookmark finished")


if __name__ == '__main__':
    install()
