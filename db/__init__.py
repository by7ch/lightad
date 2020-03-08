import config

if config.USE_DB == "REDIS":
    from ._redis import *
else:
    from ._tinydb import *
