from pprint import pprint

from saving_data import set_data
from utils import get_data_from_file, save_data_to_file


def print_users():
    data = get_data_from_file()
    pprint(data, indent=2)


def create_user():
    data = get_data_from_file()
    data = set_data(data)

    if not data:
        return

    save_data_to_file(data)


COMMANDS = {
    "list": print_users,
    "create": create_user,
}
