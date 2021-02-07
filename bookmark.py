import sys
import error
import const
import traceback
from task_factory import task_factory
from logger import logger
from logger.style import style


def parse_args(args):
    sub_cmd = parse_subcommand(args[0])

    if len(args) > 1:
        action = parse_action(args[1])
    else:
        action = None

    if len(args) > 2:
        param = parse_param(args[2:])
    else:
        param = dict()
    return sub_cmd, action, param


def parse_subcommand(scmd):
    support_subcommand = {
        const.subcommand.help,
        const.subcommand.version,
        const.subcommand.page,
        const.subcommand.folder,
    }
    if scmd not in support_subcommand:
        raise error.InvalidSubcommandError(scmd)
    return scmd


def parse_action(action):
    support_operator = {
        const.action.add,
        const.action.drop,
        const.action.help,
        const.action.version,
        const.action.open
    }

    if action not in support_operator:
        raise error.InvalidActionError(action)
    return action


def parse_param(args):
    index = 0
    param = {
        "debug": True,
    }
    while index < len(args):
        if args[index] in {"--help", "-h"}:
            param["help"] = True
            break
        elif args[index] in {"--name", "-n"}:
            index += 1
            param["name"] = args[index]
        elif args[index] in {"--url", "-u"}:
            index += 1
            param["url"] = args[index]
        elif args[index] == "--path":
            index += 1
            param["path"] = args[index]
            logger.path = param["path"]
        elif args[index] == "--silence":
            param["debug"] = False
        else:
            # action value
            if "action_value" in param:
                raise error.InvalidParamError(args[index])
            else:
                param["action_value"] = args[index]

        index += 1
    return param


def execute():
    try:
        task_factory(*parse_args(sys.argv[1:])).execute()
    except Exception as e:
        if isinstance(e, error.BaseError):
            logger.error(str(e), print_type=style.type.flash, font=style.font.red)
        elif isinstance(e, IndexError):
            logger.error(
                "Invalid command request. Please read help doc first.",
                print_type=style.type.flash,
                font=style.font.red,
            )
        else:
            logger.error(
                "\n" + traceback.format_exc(),
                print_type=style.type.flash,
                font=style.font.red,
            )


if __name__ == '__main__':
    execute()
