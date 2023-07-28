import random
import string


def random_string(length) -> str:
    symbols = string.ascii_uppercase + "1234567890"
    return "".join(random.choice(symbols) for i in range(length))