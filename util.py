import os


def is_install():
    return "bookmark" in set(os.listdir("/usr/bin"))


def root_path():
    util_path = os.path.realpath(__file__)
    util_path_list = util_path.split("/")
    return "/".join(util_path_list[:-1])


def path_join(*args):
    arg_list = list(args)
    arg_list.insert(0, root_path())
    return os.path.join(*arg_list)


def storage_path():
    return path_join("pages")


def file_exist(path):
    return os.path.exists(path)


def system(command):
    return os.system(command)


def create_storage_dir(path):
    os.mkdir(path)


def pages():
    file_list = os.listdir(storage_path())
    page_set = set()
    for file in file_list:
        if not is_json_file(file):
            continue

        name_list = file.split(".")
        name_list.pop(-1)
        page_set.add(".".join(name_list))

    return page_set


def is_json_file(filename):
    filename = filename.strip(".")
    if "." not in filename:
        return False

    filename_list = filename.split(".")
    return filename_list[-1] == "json"


def delete_file(path):
    if not os.path.isfile(path):
        return

    command = "rm -rf %s" % path
    return os.system(command) == 0
