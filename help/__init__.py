import util
import const
from template import replace


def print_doc(message="", action=const.action.help):
    if message != "":
        print(message)

    if action == const.action.add:
        content = add_help_doc()
    elif action == const.action.open:
        content = open_help_doc()
    elif action == const.action.drop:
        content = drop_help_doc()
    else:
        content = help_doc()

    print(content)
    exit(1)


def help_doc():
    content = replace(
        util.path_join(util.root_path(), "help/bookmark_help_doc.tpl"),
        write_template_file=False,
        title=get_title(),
    )
    return content


def drop_help_doc():
    content = replace(
        util.path_join(util.root_path(), "help/drop_help_doc.tpl"),
        write_template_file=False,
        title=get_title(),
    )
    return content


def add_help_doc():
    content = replace(
        util.path_join(util.root_path(), "help/add_help_doc.tpl"),
        write_template_file=False,
        title=get_title(),
    )
    return content


def open_help_doc():
    content = replace(
        util.path_join(util.root_path(), "help/open_help_doc.tpl"),
        write_template_file=False,
        title=get_title(),
    )
    return content


def get_title() -> str:
    if util.is_install():
        title = "bookmark"
    else:
        title = util.path_join(util.root_path(), "bookmark.sh")
    return title
