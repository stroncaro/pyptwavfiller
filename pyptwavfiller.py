from enum import StrEnum
import os
from sys import argv

HELP_TEXT = """
pyptwavfiller - Empty wav filler for mocking project structures

Usage: pyptwavfiller.py COMMAND [ARGUMENT]
    COMMANDS:
        CREATE  - creates an index.txt file with the folder structure
        MOUNT   - takes an index.txt file and recreates the folder structure
                  replacing all wavs with empty wavs
"""


class Command(StrEnum):
    CREATE = "CREATE"
    MOUNT = "MOUNT"


def print_help() -> None:
    print(HELP_TEXT)


def create_index() -> None:
    path = os.path.dirname(os.path.realpath(__file__))
    crawl_dirs(path)

    raise NotImplementedError()


def crawl_dirs(path: str):
    for entry in os.scandir(path):
        print(entry)
        if entry.is_dir(follow_symlinks=False):
            crawl_dirs(entry.path)


def mount_index(index) -> None:
    raise NotImplementedError()


if __name__ == "__main__":
    argc = len(argv)

    if argc == 1 or argc > 3:
        print_help()
        exit(0)

    command = argv[1]
    if not command in Command:
        raise TypeError(
            f"Unknown command: '{command}'. Run pyptwavfiller.py without arguments for help"
        )

    match command:
        case Command.CREATE:
            create_index()
        case Command.MOUNT:
            mount_index()
        case _:
            print_help()
