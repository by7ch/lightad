import base64


def encode(c: str) -> str:
    return str(base64.b64encode(bytes(c)))


def decode(c: str) -> str:
    return str(base64.b64decode(bytes(c)))
