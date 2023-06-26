import json

from const import USER_FILE_STORAGE
from exceptions import FileExtensionError


def get_data_from_file(filename: str = USER_FILE_STORAGE) -> dict:
    if not filename.endswith(".json"):
        raise FileExtensionError
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def save_data_to_file(data: dict, filename: str = USER_FILE_STORAGE) -> None:
    if not filename.endswith(".json"):
        raise FileExtensionError

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
