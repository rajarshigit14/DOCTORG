import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

def sameday_doctors_list(doctors,appointment_date,Times):
    #Checking if any allocation is done or not
    start=0
    end=0
    Flag=0
    x=''
    info=[]
    #checking all the doctors for appropriate date and doctor
    for doc in doctors:
        avali_days=doc['days']
        #removing the days on which the doctor does do any visits
        l=[]
        for day in avali_days:
            if avali_days[day] == '':
                l.append(day)

        for i in l:
            del avali_days[i]

        #all avaliable days in a list for the current doctor
        day_list=list(avali_days.keys())

        add_date_sting=str(appointment_date)
        add_date_sting=add_date_sting.split('-')
        new_string=add_date_sting[::-1]
        add_day=" ".join(new_string)

        day=findDay(add_day)


        #Times is a dictionary containing allotments of all doctors of appointment_date
        #Write Times extraction code below using MongoDB
        #print(day)
        #print(day_list)
        #print(str(doc['Phone']))
        if day in day_list:
            print(Times.keys())
            if str(doc['Phone']) in Times.keys():
                print(str(doc['Phone']))
            else:
                print('False')
            #print("~~~~")
            appointment_list_of_doc=Times[str(doc['Phone'])]
            #print(appointment_list_of_doc)
            #print(Times[str(doc['Phone'])])
            #print("~~~~~")
            if day in day_list and sum(appointment_list_of_doc) < len(appointment_list_of_doc):

                #Allotment will be done with this doctor
                

                name=doc['Name']
                info.append(name)
                dep=doc['Department']
                info.append(dep)
                desig=doc['Designation and year of experience ']
                info.append(desig)
                info.append(add_day)
                

                Time = doc['days'][day].split('-')
                start = int(Time[0]) #Starting hour of the Doctor. Use it to find the appointment time by adding minutes
                end=int(Time[1])
                arr=list(range(start,end))

                today=datetime.datetime.now()
                start_hour=today.hour
                #print(start_hour)
                #print(arr)
                if start_hour+2 in arr[:len(arr)-1]:
                    Flag=1
                    print(start_hour+2)
                    start_index=arr.index(start_hour+2)

                #Allot the appointment(setting the value 1 and then break)
                    #print(appointment_list_of_doc)
                    for allotment in range(start_index,len(appointment_list_of_doc)):
                        if appointment_list_of_doc[allotment] == 0:
                            appointment_list_of_doc[allotment]=1
                            break
                  
            break
    #print(start)
    if Flag==1:
        Times[str(doc['Phone'])]=appointment_list_of_doc
        #print(appointment_list_of_doc)
        Time_start = start
        count = sum(appointment_list_of_doc)-1
        if count%2 == 0:
            Time_start += int(count/2)
            Time_start = str(Time_start)
            x=Time_start+":00 - "+Time_start+":30"
        else:
            Time_start += int(count/2)
            x=str(Time_start)+':30 - '+str((int(Time_start))+1)+':00'
        info.append(x)

    #Checking if Time alloted or not
    if Flag==1:
        return info,Times
    else:
        return "-1",Times
