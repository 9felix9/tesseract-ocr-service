"""System health related tooling."""
# TODO IF PYMONGO OR GEARMAN COOKIECUTTER CHECK
from pymongo import MongoClient
from python3_gearman.connection import GearmanConnection


def is_mongodb_reachable(mongo_server_settings: list) -> bool:
    # pilfered from https://stackoverflow.com/a/30539401
    mongo_client = MongoClient(*mongo_server_settings, serverSelectionTimeoutMS=1)
    try:
        mongo_client.server_info()
    except Exception:
        return False

    return True


def is_gearman_server_reachable(gearman_server_settings: list) -> bool:
    connection = GearmanConnection(
        gearman_server_settings[0], int(gearman_server_settings[1])
    )
    try:
        connection.connect()
        connection.close()
    except Exception:
        return False

    return True