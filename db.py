# import os
# import numpy as np
# from pymongo import MongoClient

# MONGODB_URI = "mongodb+srv://admin:admin123@cluster0.4ywwz.mongodb.net/"
# DB_NAME = "face_recognition_db"
# COLLECTION_NAME = "faces"

# def get_db_collection():
#     client = MongoClient(MONGODB_URI)
#     db = client[DB_NAME]
#     collection = db[COLLECTION_NAME]
#     return collection

# def load_face_db_mongo():
#     """
#     Load the face database from MongoDB.
#     Returns a dictionary in the form:
#       { "person_name": [embedding1, embedding2, ...] }
#     where each embedding is a NumPy array.
#     """
#     collection = get_db_collection()
#     face_db = {}
#     for doc in collection.find():
#         name = doc["name"]
#         embeddings = [np.array(enc) for enc in doc.get("embeddings", [])]
#         face_db[name] = embeddings
#     return face_db

# def upsert_face(name, new_encoding, max_samples=5):
#     """
#     Insert or update a face entry for a given name.
#     If the name exists and has fewer than max_samples, append the new encoding.
#     Otherwise, create a new document.
#     The encoding is stored as a list.
#     """
#     collection = get_db_collection()
#     doc = collection.find_one({"name": name})
#     new_enc_list = new_encoding.tolist()
#     if doc:
#         embeddings = doc.get("embeddings", [])
#         if len(embeddings) >= max_samples:
#             raise ValueError(f"Already registered maximum samples for '{name}'.")
#         embeddings.append(new_enc_list)
#         collection.update_one({"name": name}, {"$set": {"embeddings": embeddings}})
#     else:
#         collection.insert_one({"name": name, "embeddings": [new_enc_list]})


import os
import numpy as np
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB connection details from .env file
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def get_db_collection():
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]  # ✅ Directly return collection

def load_face_db_mongo():
    """
    Load the face database from MongoDB.
    Returns a dictionary in the form:
      { "person_name": [embedding1, embedding2, ...] }
    where each embedding is a NumPy array.
    """
    collection = get_db_collection()
    if collection is None:  # ✅ Fixed
        return {}

    face_db = {}
    for doc in collection.find():
        name = doc["name"]
        embeddings = [np.array(enc) for enc in doc.get("embeddings", [])]
        face_db[name] = embeddings
    return face_db

def upsert_face(name, new_encoding, max_samples=5):
    """
    Insert or update a face entry for a given name.
    If the name exists and has fewer than max_samples, append the new encoding.
    Otherwise, create a new document.
    """
    collection = get_db_collection()
    if collection is None:  # ✅ Fixed
        raise ValueError("Database collection is not available")

    new_enc_list = new_encoding.tolist()
    doc = collection.find_one({"name": name})

    if doc:
        embeddings = doc.get("embeddings", [])
        if len(embeddings) >= max_samples:
            raise ValueError(f"Already registered maximum samples for '{name}'.")
        embeddings.append(new_enc_list)
        collection.update_one({"name": name}, {"$set": {"embeddings": embeddings}})
    else:
        collection.insert_one({"name": name, "embeddings": [new_enc_list]})
