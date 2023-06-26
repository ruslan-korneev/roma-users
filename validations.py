from exceptions import ValidationError


def validate_email(email: str) -> str:
    base_message = f"not valid email: {email}"
    if email.count("@") == 1:
        raise ValidationError("email should have one '@' symbol")

    host = email.split("@")[1]
    errors = []
    if "." not in host:
        errors.append("host should have at least one '.'")
    if host.startswith("."):
        errors.append("host should not start with '.'")
    if host.endswith("."):
        errors.append("host should not end with '.'")

    if errors:
        raise ValidationError(f"{base_message}: {errors}")

    return email


def validate_phone(phone: str) -> str:
    if not phone.startswith("+7"):
        raise ValidationError(
            f"phone {phone} should starts with +7"
        )

    if len(phone) != 12:
        raise ValidationError(
            f"length phone {phone} should equal to 12"
        )

    return phone
