import os


def isfile(path):
    return os.path.isfile(path)


def is_install() -> bool:
    return "bookmark" in set(os.listdir("/usr/bin"))


def root_path() -> str:
    util_path = os.path.realpath(__file__)
    util_path_list = util_path.split("/")
    return "/".join(util_path_list[:-1])


def path_join(*args):
    return os.path.join(*args)


def get_version() -> str:
    with open(path_join(root_path(), "bm.version"), "r") as file:
        version = file.read().strip()
    return version


def storage_path() -> str:
    return path_join(root_path(), "pages")


def file_exist(path) -> bool:
    return os.path.exists(path)


def is_dir(path) -> bool:
    return os.path.isdir(path)


def is_file(path) -> bool:
    return os.path.isfile(path)


def system(command) -> int:
    return os.system(command)


def create_storage_dir(path):
    os.mkdir(path)


def pages() -> set:
    file_list = os.listdir(storage_path())
    page_set = set()
    for file in file_list:
        if not is_json_file(file):
            continue

        name_list = file.split(".")
        name_list.pop(-1)
        page_set.add(".".join(name_list))

    return page_set


def is_json_file(filename: str) -> bool:
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
