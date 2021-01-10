import util


def replace(path, **kwargs):
    if suffix(filename(path)) != "tpl":
        path += ".tpl"

    if not util.isfile(path):
        return

    # `write_template_file` default is True
    if "write_template_file" in kwargs:
        write_template_file = kwargs["write_template_file"]
        del kwargs["write_template_file"]
    else:
        write_template_file = True

    content_list = open(path, "r").readlines()
    for index in range(len(content_list)):
        if "{{-" in content_list[index]:
            for key in kwargs:
                target = "{{- %s -}}" % key
                if target in content_list[index]:
                    content_list[index] = content_list[index].replace(
                        target,
                        kwargs[key]
                    )

    content = "".join(content_list)
    if write_template_file:
        path = path.replace(".tpl", "")
        with open(path, "w") as file:
            file.write(content)

    return content


def filename(path: str) -> str:
    path_list = path.split("/")
    return path_list[-1]


def suffix(filename: str):
    filename = filename.strip(".")
    if filename.count(".") <= 0:
        return None

    filename_list = filename.split(".")
    return filename_list[-1]
