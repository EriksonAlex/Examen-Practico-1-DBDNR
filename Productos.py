from connection import collection
import json
from bson import ObjectId

def read_products(id=None):
    if id is not None:
        oid2 = ObjectId(id)
        query = {"_id": oid2}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def create_products(json_employees):
    result = collection.insert_one(json_employees)
    print(result.inserted_id)


def update_products(id, json_employee_update):
    oid2 = ObjectId(id)
    query = {"_id": oid2}
    new_values = {"$set": json_employee_update}
    result = collection.update_one(query,new_values)
    print(result.modified_count)

def delete_products(id=None):
    if id is not None:
        oid2 = ObjectId(id)
        query = {"_id": oid2}
        document = collection.delete_one(query)
        print(document.deleted_count)
    else:
        print("Ingrese un ID")