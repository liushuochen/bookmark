import sys
import error
import const
import util
import traceback
from cmd.help import print_doc
from task_factory import task_factory


def parse_args(args):
    action = parse_action(args[0])
    if action == const.action.help:
        print_doc(action=action)
    if action == const.action.version:
        print(util.get_version())
        exit(0)

    if len(args) > 1:
        param = parse_param(args[1:])
    else:
        param = dict()

    if param.get("help", False):
        print_doc(action=action)
    return action, param


def parse_action(action):
    support_operator = {
        const.action.add,
        const.action.drop,
        const.action.help,
        const.action.version,
        const.action.open
    }

    if action not in support_operator:
        raise error.InvalidActionError("%s do not exist." % action)
    return action


def parse_param(args):
    index = 0
    param = dict()
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
        else:
            # nothing to do.
            pass

        index += 1
    return param


def execute():
    try:
        task_factory(*parse_args(sys.argv[1:])).execute()
    except Exception as e:
        if isinstance(e, error.BaseError):
            print(str(e))
        elif isinstance(e, IndexError):
            print("Invalid command request. Please read help doc first.")
        else:
            print(traceback.format_exc())


if __name__ == '__main__':
    execute()
