import pandas as pd
import sqlalchemy
from mysql import connector as myc
con = myc.Connect(host="localhost", user="root", passwd="akshat", database="airlines")

if con.is_connected():
    print("Successfully connected!!!!")
else:
    print("no connection")
engine=sqlalchemy.create_engine("mysql+pymysql://root:akshat@localhost:3306/airlines")

def option():
    option = int(input("Enter Your Choice:"))
    if option == 1:
        About()
    elif option == 2:
        flight_details()
    elif option == 3:
        Passenger()
    elif option == 4:
        new_passenger()
    elif option == 5:
        classtype()
    elif option == 6:
        new_classtype()
    elif option == 7:
        Food()
    elif option == 8:
        add_food_item()
    elif option == 9:
        Rev_food_rates()
    elif option == 10:
        Lugguage_rates()
    elif option == 11:
        seats()
    elif option == 12:
        Lugguage_bill()
    elif option == 13:
        Food_bill()
    elif option == 14:
        barred_items()

def menu():
    print("*"*104)
    print(" "*40," FLIGHT MANAGEMENT SYSTEM "," "*40)
    print("*"*104)
    print("1.About the system")
    print("2.Show Flight details")
    print("3.Show Passenger Details")
    print("4.Add new Passenger Details")
    print("5.Show Class Type Details")
    print("6.Add new Class Type Details")
    print("7.Show Food items available")
    print("8.Add new Food items ")
    print("9.Revise Rates of Food items")
    print("10.Show rates for extra lugguage (>35 kg)")
    print("11.Reserve Tickets & show bill for the same")
    print("12.Show bill for extra lugguage")
    print("13.Show bill for Food if ordered")
    print("14.Show list of prohbited items in flight")
    option()

def About():
        print("This software is helpful to the people, being tourism lovers,\n and for the people who travel a lot for their personal or professional purposes.\n This application helps getting air transport details, storing lots of data,\n performing different types of operations on the stored data, adding new data\n & updating it, and at that the same time time providing a user friendly interface.\n")
        option()

def flight_details():
    D6= pd.DataFrame()
    D6 = pd.read_sql_query("select * from flight_details", engine, index_col="S_No")
    print(D6)
    option()

def Passenger():
    D2=pd.DataFrame()
    D2=pd.read_sql_query("Select * from passenger", engine, index_col="S_No")
    print(D2)
    option()

def new_passenger():
    cursor = con.cursor()
    while True:
        S_No = int(input("Enter S_No:"))
        Passenger_name = str(input("Enter Passenger name:"))
        Reservation_date = str(input("Enter date of reservation(dd-mm-yyyy):"))
        Source = str(input("Enter Source:"))
        Destination = str(input("Enter Destination:"))
        classtype = str(input("Enter classtype:"))
        query = "insert into passenger(S_No, Passenger_name, Reservation_date, Source, Destination, classtype) values({}, '{}', {}, '{}', '{}','{}')".format(S_No,Passenger_name,Reservation_date,Source, Destination, classtype)
        cursor.execute(query)
        con.commit()
        print("Data inserted successfully.....")
        x = int(input("1->insert more\n2->Exit\nEnter choice:"))
        if x == 2:
            break
    option()

def new_classtype():
    cursor = con.cursor()
    while True:
        S_No = int(input("Enter S_No:"))
        Classtype=str(input("Enter new Class type:"))
        Rate=int(input("Enter rate of new classtype:"))
        query = "insert into classtype(S_No,Classtype,Rate) values({}, '{}', {})".format(S_No,Classtype,Rate)
        cursor.execute(query)
        con.commit()
        print("Data inserted successfully.....")
        x = int(input("1->insert more\n2->Exit\nEnter choice:"))
        if x == 2:
            break
    option()

def classtype():
    D5 = pd.DataFrame()
    D5 = pd.read_sql_query("select * from classtype", engine,index_col="S_No")
    print(D5)
    option()

def Food():
    D1=pd.DataFrame()
    D1=pd.read_sql_query("select * from food",engine, index_col="S_No")
    print(D1)
    option()

def add_food_item():
    cursor = con.cursor()
    while True:
        S_No = int(input("Enter S_No:"))
        Food_item = str(input("Enter new food item:"))
        Rate = int(input("Enter rate of food item:"))
        query = "insert into food(S_No,Food_item,Rate) values({},'{}',{})".format(S_No,Food_item,Rate)
        cursor.execute(query)
        con.commit()
        print("Data inserted successfully.....")
        x = int(input("1->insert more\n2->Exit\nEnter choice:"))
        if x == 2:
            break
    option()

def Rev_food_rates():
    print("Here is the list of food items. Select the food item you want to revise!!")
    cursor = con.cursor()
    while True:
        Food_item = str(input("Enter name of food item:"))
        Rate = int(input("Enter new Rate:"))
        query = "update food set Rate={} where Food_item='{}'".format(Rate,
        Food_item)
        cursor.execute(query)
        con.commit()
        if cursor.rowcount > 0:
            print("Data updated successfully.....")
        else:
            print("No Data Found!!")
        x = int(input("1->Update more\n2->Exit\nEnter choice:"))
        if x == 2:
            break
    option()

def Lugguage_rates():
    D3=pd.DataFrame()
    D3=pd.read_sql_query("select * from lugguage", engine,index_col="S_No")
    print(D3)
    option()

def seats():
    print("Following types of seats are available:")
    c = pd.DataFrame()
    c = pd.read_sql_query("select * from classtype", engine, index_col="S_No")
    print(c)
    x=int(input("Please enter your choice of ticket:"))
    n=int(input("How many tickets to be reserved?"))
    if x==1:
        print("You have chosen FIRST CLASS!")
        s=6000*n
    elif x==2:
        print("You have chosen BUSINESS CLASS!")
        s=12000*n
    elif x == 3:
        print("You have chosen ECONOMY CLASS!")
        s = 5000 * n
    else:
        print("Please choose a room")
    print("Your total Ticket price is : Rs.", s, "\n")
    option()

def Lugguage_bill():
    X = pd.DataFrame()
    X = pd.read_sql_query("select * from lugguage", engine, index_col="S_No")
    print(X)
    x=int(input("Enter serial no. of weight of extra lugguage:"))
    if x==1:
        print("You have 10 Kg extra!")
        s = 500
    elif x == 2:
        print("You have 15 Kg extra!")
        s = 700
    elif x == 3:
        print("You have 20 Kg extra!")
        s = 1000
    elif x == 4:
        print("You have 25 Kg extra!")
        s = 1200
    elif x == 5:
        print("You have 30 Kg extra!")
        s = 1400
    else:
        print("Please choose a correct Serial No.!!")
    print("Your extra lugguage costs Rs.", s, "\n")
    option()

def Food_bill():
    print("All Food items available!")
    A = pd.DataFrame()
    A = pd.read_sql_query("select * from food", engine, index_col="S_No")
    print(A)
    x = int(input("Enter Serial no. of Food item:"))
    n = int(input("Enter quantity of food item:"))
    if x == 1:
        print("You have selected Tea!")
        s = n * 60
    elif x == 2:
        print("You have selected Milk!")
        s = n * 40
    elif x == 3:
        print("You have selected Coffee!")
        s = n * 85
    elif x == 4:
        print("You have selected Standard meal!")
        s = n * 225
    elif x == 5:
        print("You have selected Delux meal!")
        s = n * 250
    elif x == 6:
        print("You have selected Premium meal!")
        s = n * 325
    elif x == 7:
        print("You have selected Burger!")
        s = n * 90
    elif x == 8:
        print("You have selected Pizza!")
        s = n * 160
    else:
        print("Selected food not available!!")

    print("Your Food costs Rs.", s, "\n")
    option()

def barred_items():
    B = pd.DataFrame()
    B = pd.read_sql_query("select * from barred_items", engine, index_col="S_No")
    print(B)
    option()

menu()
option()



