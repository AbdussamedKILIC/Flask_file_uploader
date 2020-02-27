import pymongo
from datetime import datetime
from bson.objectid import ObjectId
import hashlib

# MongoDB Connection
client = pymongo.MongoClient('localhost', 27017)

# Select Database name
db = client['test']

# Select Collection name from database
collection = db['test']


# Add new user to db
# take name:string ,email:string ,password:string
# hash input password then add user to database
# Return json message
def addUser(name, email, password):
    user = collection.find_one({"email": email})
    if user == None:
        user = {"name": name, "email": email,
                "password": hashlib.sha256(password.encode('utf-8')).hexdigest(), "photos": []}
        collection.insert_one(user)
        return {"message": "Created"}
    else:
        return {"message": "Already Exist"}


# Get user from db
# take email:string ,password:string
# hash input password then query db
# Return user data
# Erorr return json message
def getUser(email, password):
    user = collection.find_one(
        {"email": email, "password": hashlib.sha256(password.encode('utf-8')).hexdigest()})
    if user == None:
        return {"message": "Not Exist"}
    else:
        return user


# add new picture to user data
# take email:string ,password:string , filename:string
# hash input password then update user data
# Return json message
# Erorr return json message
def addphoto(email, password, photoName):
    result = collection.update_one(
        {"email": email, "password": hashlib.sha256(password.encode('utf-8')).hexdigest()}, {
            "$push": {'photos': {"filename": photoName, "date": datetime.utcnow()}}}
    ).matched_count
    if result == 1:
        return {"message": "Added"}
    else:
        return {"message": "Error"}
