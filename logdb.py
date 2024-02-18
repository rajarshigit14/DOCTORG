import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
uri = SECRET_KEY 

client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.logbase
# Created or Switched to collection names
collection = db.tunky

patient = {"Name": "Anurag Dutta",
           "Age": 20,
           "Mobile_No": 9674002645,
           "Email_Id": "imanurag18@gmail.com",
           "History": [ ['SCB','2023-10-28','Allergist, MD 8 years'], ['SS','2023-11-10','Neurologist, DM 6 years']]
        }

collection.insert_one(patient)