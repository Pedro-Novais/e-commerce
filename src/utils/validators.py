import re

def valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    return re.match(email_regex, email)

def valid_password(password: str) -> bool:
    if len(password) < 7:
        return False

    password_regex = r'^(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>_+\-=\\/~`])[A-Za-z\d!@#$%^&*(),.?":{}|<>_+\-=\\/~`]{8,}$'

    return re.match(password_regex, password)
