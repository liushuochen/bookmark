import const
import error
import cmd


def task_factory(subcommand, action, param):
    if subcommand == const.subcommand.help:
        instance = cmd.help_doc(param)

    elif subcommand == const.subcommand.version:
        instance = cmd.get_version(param)

    elif subcommand == const.subcommand.page:
        if action == const.action.add:
            instance = cmd.add_page(param)
        elif action == const.action.drop:
            instance = cmd.drop_page(param)
        elif action == const.action.edit:
            instance = cmd.edit_page(param)
        elif action == const.action.list:
            instance = cmd.list_page(param)
        elif action == const.action.describe:
            instance = cmd.get_page(param)
        elif action == const.action.open:
            instance = cmd.open_page(param)
        else:
            raise error.InvalidActionError(action)

    else:
        instance = cmd.default_scmd(subcommand, param)
    return instance
