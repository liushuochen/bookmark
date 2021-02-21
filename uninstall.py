# uninstall bookmark
import os


def uninstall():
    command = "rm -rf /usr/local/bin/bookmark > /dev/null 2>&1"
    os.system(command)


if __name__ == '__main__':
    uninstall()
