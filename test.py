import os
from dotenv import load_dotenv
from datetime import date,timedelta
from pymongo.mongo_client import MongoClient
from allocation import doctors_list
from datetime import datetime
import calendar
from allocation_sameday import sameday_doctors_list
'''def findDay(dates):
    born = datetime.datetime.strptime(dates, '%d %m %Y').weekday()
    return (calendar.day_name[born])'''

def Backend(priority_list,datee):
    global preferred_choice
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

    query=collection.find({"Department":priority_list[1],"Priority":priority_list[0]})
    print(type(query))
    a=list(query)
    print(type(a))
    if datee!="-1":
        preferred_choice=datee
        date_object=datetime.strptime('2023-09-23','%Y-%m-%d').date()

        a=list(query)
        p=collection1.find_one({'date':preferred_choice})
        result,time_arr=doctors_list(a,preferred_choice,p['Times'])
        
        print(result)
    else:   

        today = date.today()
        day=today + timedelta(days=0)
        
        preferred_choice=day
        #print(day,"~~~~~")
        p=collection1.find_one({'date':str(day)})
        #print(p['Times'])
        result,time_arr=sameday_doctors_list(a,day,p['Times'])
        
        if result=='-1':
            
            for i in range(1,15):
                day=today + timedelta(days=i)
                preferred_choice=day
                p=collection1.find_one({'date':str(day)})
                #print(p['Times']['9638745120'])
                result,time_arr=doctors_list(a,day,p['Times'])
                if result != '-1':
                    break
    #print(time_arr)    
    d={'date':str(preferred_choice)}
    t={'$set':{'Times':time_arr}}
    collection1.update_one(d,t)
    return result

