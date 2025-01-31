from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["tax_database"]
documents_collection = db["documents"]
