#!/usr/bin/env python3

"""
this module writes a script that
provides some stats about Nginx
"""

from pymongo import MongoClient

def get_nginx_stats():
    """
    Connects to the MongoDB database
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    get_nginx_stats()