import const
import error
from action import Add, Open, Drop


def task_factory(action, param):
    if action == const.action.add:
        name = param.get("name", None)
        url = param.get("url", None)
        if name is None or url is None:
            raise ValueError("Missing name and url.")
        instance = Add(name, url)

    elif action == const.action.open:
        name = param.get("name", None)
        url = param.get("url", None)
        if name is None and url is None:
            raise ValueError("Missing name or url")
        instance = Open(name, url)

    elif action == const.action.drop:
        name = param.get("name", None)
        if name is None:
            raise ValueError("Missing name")
        instance = Drop(name)

    else:
        raise error.InvalidActionError("Unsupported action %s." % action)
    return instance


def default():
    pass
