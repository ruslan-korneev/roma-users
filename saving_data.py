from validations import (
    validate_phone,
    validate_email,
    ValidationError
)


def set_name(data: dict) -> str:
    while True:
        name = input("Введите имя пользователя:")
        if name not in data:
            data[name] = {}
            return name
        else:
            print("Пользователь с таким именем уже создан!")


def set_age(data: dict, name: str) -> None:
    while True:
        age = int(input("Введите возраст:"))
        if 18 < age < 100:
            data[name]["age"] = age
            return
        else:
            print("Возраст >18,<100")


def set_phone(data: dict, name: str) -> None:
    phone = input("Введите телефон:")
    validate_phone(phone)
    data[name]["phone"] = phone


def set_email(data: dict, name: str) -> None:
    email = input("Введите почту:")
    validate_email(email)
    data[name]["email"] = email


def set_data(data: dict) -> dict | None:
    try:
        # name = set_name(data)
        # set_age(data, name)
        name = "temp"
        data[name] = {}
        set_phone(data, name)
        set_email(data, name)
    except ValidationError as exc:
        print(exc.args)
        return

    return data
