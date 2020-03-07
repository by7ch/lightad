def insert_flag(flag: str) -> bool:
    """
    Insert a flag into db
    :param flag: flag found
    :return: whether successful
    """
    return True


def insert_payload(location: str) -> bool:
    """
    Insert a payload into db
    :param location: location of payload
    :return: whether successful
    """
    return True


def tick_scan_flag() -> list:
    """
    Check whether there are unsubmitted flags in db
    If there exists, pop all those flags
    """
    return []


def tick_scan_payload() -> (bool, list):
    """
    Pop new payload
    :return: whether new payload is added and new payload added
    """
    return True, ["./payloads/p.py"]
