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


GET_TICK_TIME_MODE = "ALL"


def get_tick_time() -> list:
    return [

    ]


def initial_tick_time() -> int:
    return 0


def update_tick_time() -> int:
    return 1


def submit_flag(flag: str) -> bool:
    return True


def check_flag(flag: str) -> bool:
    return True
