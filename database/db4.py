import sys
sys.path.append("/Users/razyesh/it-training-python-class/database")
import datetime
from db import DBConnection

MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_USERNAME = "razyesh"
MONGODB_PASSWORD = "1234"
MONGODB_DB = "moneymitra"

db = DBConnection()
with db.connect_mongo(host=MONGODB_HOST, 
                      port=MONGODB_PORT, 
                      user=MONGODB_USERNAME, 
                      password=MONGODB_PASSWORD, 
                      dbname="moneymitra") as cursor:
    filters = {"symbol": {"$eq": "NABIL"}}
    collection = cursor["technical_moving_average"]

    results = collection.find(filters)
    for row in results:
        print(row)

