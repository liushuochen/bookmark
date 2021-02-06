import const
import error
import cmd


def task_factory(subcommand, action, param):
    if subcommand == const.subcommand.help:
        instance = cmd.help_doc(param)
    elif subcommand == const.subcommand.page:
        if action == const.action.add:
            instance = cmd.add_page(param)
        else:
            raise error.InvalidActionError(action)
    else:
        raise error.InvalidSubcommandError("Unsupported action %s." % action)
    return instance


def default():
    pass
