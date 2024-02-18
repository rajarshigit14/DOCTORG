import os
from dotenv import load_dotenv
from datetime import date,timedelta
from pymongo.mongo_client import MongoClient
from allocation import doctors_list
from datetime import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
uri = SECRET_KEY 

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.database

# Created or Switched to collection names
collection = db.funky
db1=client.base
collection1=db1.punky

query=collection.find({"Department":"Allergist","Priority":"junior"})

a=list(query)
preferred_choice="anurag"
if preferred_choice=="Preferred date":
   
    date_object=datetime.strptime('2023-09-23','%Y-%m-%d').date()

    query=collection.find({"Department":"Allergist","Priority":"junior"})
    a=list(query)
    p=collection1.find_one({'date':str('2023-09-23')})
    result,time_arr=doctors_list(a,'2023-09-23',p['Times'])
else:
    

    today = date.today()
    day=today + timedelta(days=0)


    p=collection1.find_one({'date':str(day)})

    result,time_arr=doctors_list(a,day,p['Times'])
    if result=='-1':
        for i in range(1,15):
            day=today + timedelta(days=i)
            
            p=collection1.find_one({'date':str(day)})
            result,time_arr=doctors_list(a,day,p['Times'])
            if result != '-1':
                break

    #update database with time_arr-(anurag's job)
    #p['Times']=time_arr
    d={'date':str(day)}
    t={'$set':{'Times':time_arr}}
    collection1.update_one(d,t)
    print(result)
