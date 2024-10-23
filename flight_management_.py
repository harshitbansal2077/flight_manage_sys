#Import mysql.

import mysql.connector as c
db = c.connect(host = 'localhost', user = 'miyaaa', passwd = 'Izumiii2077')
mc = db.cursor()
db.autocommit = True

#Creating tables if they don't exists.

mc.execute("create database if not exists reservation")
mc.execute("use reservation")
mc.execute("create table if not exists bookings(name varchar(100),Ticket_no int primary key, mobl varchar(15), age int, gender varchar(50), class_type varchar(500), fro_f varchar(100), to_f varchar(100), date_d varchar(20), tic_price varchar(20), food_price varchar(20))")
mc.execute("create table if not exists passenger(name varchar(20),Ticket_no int primary key, mobile varchar(15), class_t varchar(500), boarding_point varchar(20), destination varchar(20), food_req varchar(20))")
mc.execute("create table if not exists veg(sno int primary key, food varchar(50), price varchar(20))")
mc.execute("create table if not exists non_veg(sno int primary key, food varchar(50), price varchar(20))")
mc.execute("create table if not exists user_login(user_n varchar(50) primary key, sec_key varchar(50))")

print("                    ******************************************")
print("                  ___WELCOME TO FLIGHT RESERVATION MANAGEMENT___")
print("                    ******************************************")

print("")

#Function to book tickets.

def ticket_booking():
    
    import mysql.connector
    import csv as cs
    import random as rd
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print("Enter how many tickets you want to book.")
    nu = int(input("Enter your choice: "))
    for i in range(0,nu):
        Tn=Tic_no()
        nm=input('enter your name:')
        phno=input('enter your phone number:')
        age=int(input('enter your age:'))
        print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
        gender=input('enter your gender:')
        Gender=gender.upper()
        fr=input('enter ur starting point:')
        to=input('enter your destination:')
        date1=input('enter date(dd):')
        date2=input('enter month(mm):')
        date3=input('enter year(yyyy):')
        date=date1+"/"+date2+"/"+date3
        a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
        v=a[Gender]
        cursor.execute("insert into bookings(name,Ticket_no, mobl, age, gender, fro_f, to_f, date_d) values('{}',{},{},{},'{}','{}','{}','{}')".format(nm,Tn,phno,age,v,fr,to,date))
        cursor.execute("insert into passenger(name,Ticket_no,mobile, boarding_point, destination) values(%s, %s, %s, %s, %s)", (nm ,Tn ,phno, fr, to))
        class_ty(Tn)
        print("")
        print("Enter 1 if you want veg food.")
        print("Enter 2 if you want non-veg food.")
        print("Enter 0 if you want nothing.")
        print("")
        food = int(input("Enter if you want food: "))
        if food == 1:
            cursor.execute("select * from veg")
            for i in cursor:
                print(i)
            a = int(input("Enter number of the food you want: "))
            cursor.execute("update passenger set food_req = (select food from veg where sno = %s) where mobile = %s ", (a,phno))
            cursor.execute("update bookings set food_price = (select price from veg where sno = %s) where mobl = %s ", (a,phno))
            print("Food successfully ordered.")
        elif food  == 2:
            cursor.execute("select * from non_veg")
            for i in cursor:
                print(i)
            a = int(input("Enter number of the food you want: "))
            cursor.execute("update passenger set food_req = (select food from non_veg where sno = %s) where mobile = %s ", (a,phno))
            cursor.execute("update bookings set food_price = (select price from non_veg where sno = %s) where mobl = %s ", (a,phno))
            print("Food successfully ordered.")
        elif food == 0:
            pass
        print("")
        print("Your ticket no:- ",Tn)
        print('BOOKED SUCCESSFULLY')
        cursor.execute("select * from bookings where Ticket_no=%s", (Tn,))
        y=cursor.fetchone()
        z=list(y)
        ls = ['name', 'Ticket_number', 'Mobile', 'Age', 'Gender', 'Class-Type', 'Boarding_Point', 'Destination', 'Date of Departure', 'Ticket-price', 'Food-price']
        v=str(Tn)+"Ticket"+".csv"
        file=open(v,"w")
        w=cs.writer(file)
        w.writerow(ls)
        w.writerow(z)

def info():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    B=[]

    cursor.execute("select Ticket_no from bookings")
    b=cursor.fetchall()
    for i in b:
        m=i[0]
        B.append(m)
    return B
A=[]
A=info()

#To create a ticket number.

def Tic_no():
    import random as r
    c=r.randrange(100000,1000000)
    global A
    if c in A:
        Tic_no()
    else:
        A.append(c)
    return c

#For adding class type
        
def class_ty(Tn):
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print("For classtype:")
    print("Enter 1 for Economy class(Price = Rs.6000/-).")
    print("Enter 2 for Premium Economy(Price = Rs.10000/-).")
    print("Enter 3 for Business class(Price = Rs.25500/-).")
    c_type = int(input("Enter choice: "))
    if c_type == 1:
        cursor.execute("update bookings set class_type = 'Economy class' where Ticket_no = %s", (Tn,))
        cursor.execute("update bookings set tic_price = 'Rs.6000/-' where Ticket_no = %s", (Tn,))
        cursor.execute("update passenger set class_t = 'Economy class' where Ticket_no = %s", (Tn,))        
    elif c_type == 2:
        cursor.execute("update bookings set class_type = 'Premium Economy class' where Ticket_no = %s", (Tn,))
        cursor.execute("update bookings set tic_price = 'Rs.10000/-' where Ticket_no = %s", (Tn,))
        cursor.execute("update passenger set class_t = 'Premium Economy class' where Ticket_no = %s", (Tn,))        
    elif c_type == 3:
        cursor.execute("update bookings set class_type = 'Business' where Ticket_no = %s", (Tn,))
        cursor.execute("update bookings set tic_price = 'Rs.25500/-' where Ticket_no = %s", (Tn,))
        cursor.execute("update passenger set class_t = 'Business' where Ticket_no = %s", (Tn,))
    else:
        print("Class not found.")
        class_ty(Tn)



#Function to cancel bookings.

def ticket_cancelling():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))
    if ch==1:
        Tn=input('enter your ticket number:')
        cursor.execute("delete from bookings where Ticket_no=%s", (Tn,))
        cursor.execute("delete from passenger where Ticket_no = %s", (Tn,))
        print('TICKET CANCELLED')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')


#Function to check bookings

def check():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    Tn=input('enter your Ticket number:')
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))
    if ch==1:
        print("Your ticket info:- ")
        print("")
        cursor.execute("select * from passenger where Ticket_no = %s", (Tn,))
        result = cursor.fetchone()
        if result:
            print(result)
        elif not result:
            print("TICKET NOT FOUND")           
    elif ch==2:
        print('THANK YOU')
    else:
        print("ERROR 404:PAGE NOT FOUND")

#To sign_up.

def user_signup():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print("")
    print("Welcome to sign up page.")
    print("------------------------")
    try:
        u_n = input("Create a username: ")
        sec_k = input("Create a password: ")
        cursor.execute("insert into user_login values(%s, %s)", (u_n, sec_k))
        print("")
        print("Signed up successfully.")
        print("-----------------------")
        user_log()
    except:
        print("")
        print("Username not available.")
        user_signup()
#To login.

def user_log():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='miyaaa',passwd='Izumiii2077',database='reservation')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print("Enter login details:- ")
    print("")
    us_n = input("Enter your username: ")
    pas_key = input("Enter your password: ")
    cursor.execute("select * from user_login where user_n = %s", (us_n,))
    k = cursor.fetchone()
    cursor.execute("select * from user_login where sec_key = %s", (pas_key,))   
    z = cursor.fetchone()
    if k and z:
        print('')
        print("Successfully Logged in")
        

        #Menu

        while True:
            print("")
            print("----------------------------")
            print("What do you want to perform.")
            print("----------------------------")
            print("")
            print("Enter 1 to book ticket.")
            print("Enter 2 to cancel a booking.")
            print("Enter 3 to check Ticket details.")
            print("Enter 0 to log out.")
            print("")
            try:
                inp = input("Enter your choice: ")
                print("")
                if inp == '1':
                    ticket_booking()        
                elif inp == '2':
                    ticket_cancelling()        
                elif inp == '3':
                    check()
                elif inp == '0':
                    print("May you have a safe journey.")
                    print("Thanks for using our service.")
                    break
            except ValueError:
                print("You entered wrong choice.")
            
    elif not k or not z:
        print("Incorrect username or password")
        print("Try Again!!")
        user_log()
print("What do you Want to perform:-")
print("-----------------------------")
print("Enter 1 for sign-up")
print("Enter 2 for log-in")
print("Enter 3 to exit")
print("-----------------------------")
try:
    cho = int(input("Enter your choice: "))
    print("--------------------")
    if cho == 1:
        user_signup()
    elif cho == 2:
        user_log()
    elif cho == 0:
        print("Thanks for using our service.")
        pass
except ValueError:
    print("You entered wrong choice.")