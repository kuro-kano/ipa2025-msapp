"""Module to handle database operations for storing interface status."""

import os

from datetime import datetime, UTC
from pymongo import MongoClient


def save_interface_status(router_ip, interfaces):
    """Saves the interface status of a router to the MongoDB database."""
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["interface_status"]

    data = {
        "router_ip": router_ip,
        "timestamp": datetime.now(UTC),
        "interfaces": interfaces
    }
    collection.insert_one(data)
    client.close()
