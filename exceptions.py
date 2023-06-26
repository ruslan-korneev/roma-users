class FileExtensionError(BaseException):
    """this exception should be raised only when you except different extension"""
    ...


class ValidationError(BaseException):
    """only for validations' errors"""
    ...
