AVAILABLE_PARAMS_FOR_PAYLOADS = [
    "host",
    "port",
    "flag_id",
]

USE = [
    "REDIS",
    "TINYDB"
][0]

REDIS_HOST = ""
REDIS_PW = ""
REDIS_DB = ""

TINYDB_LOCATION = "./tiny.json"


def get_params(service: str) -> list:
    return [
        {
            "host": "1",
            "port": "3306",
            "flag_id": "1234"
        }
    ]


def submit_flag(flag: str) -> bool:
    return True

