# uninstall bookmark
import os


def uninstall():
    command = "rm -rf /usr/local/bin/bookmark > /dev/null 2>&1"
    os.system(command)
    print("uninstall bookmark finished")


if __name__ == '__main__':
    uninstall()
