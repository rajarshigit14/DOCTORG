import smtplib
def send_email(to_add,name,date,time):
    my_pw="mpkd gdun zvom onnz"
    my_email="doctorrrrG@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_add,
            msg="Subject: Appointment Confirmation\n\nYour Appointment details:\nName of Doctor:"+name+"\nDate of Appointment:"+date+"\nTime of Appointment:"+time+"\nAddress:Ruby Hospital"    
        )
