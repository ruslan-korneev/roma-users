import os
import json

from const import USER_FILE_STORAGE
from commands import COMMANDS


def main():
    if not os.path.exists(USER_FILE_STORAGE):
        with open(USER_FILE_STORAGE, "w") as file:
            json.dump({}, file)

    while True:
        our_commands = ", ".join(COMMANDS.keys())
        command = input(f"Введите команду {our_commands}: ")
        COMMANDS.get(command, lambda: print("Command not found"))()


if __name__ == "__main__":
    # print("main() запустилось")
    main()
else:
    print("из этого файла что-то импортировали")
