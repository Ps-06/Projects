import io
import getpass
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
def rd():
    df = pd.read_csv('Emp.csv')    

def menu():
    print("-"*40)
    print("Employee Management System")
    print("-"*40)
    print("""
    1) Add New Records
    2) Remove a Records
    3) Update a Records
    4) Find Employees Details
    5) Display Records
    6) Exit""")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        new_rec()
    elif ch ==2:
        rem_rec()
    elif ch ==3:
        upd_rec()
    elif ch ==4:
        fin_rec()
    elif ch ==5:
        dis_rec()
    elif ch == 6:
        ex()

def new_rec():
    emp_id = int(input("Enter Employee ID : "))
    first_name = input("Enter First Name : ")
    last_name = input("Enter Last Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Mobile Number : ")
    doj = input("Enter Date of Joining : ")
    job_id = input("Enter Job ID : ")
    salary = int(input("Enter Salary : "))
    commision = int(input("Enter Commission : "))
    manag_id = int(input("Enter Manager ID : "))
    dep_id = int(input("Enter Department ID : "))   
    df.loc[emp_id,:] = [emp_id,first_name,last_name,email,phone,doj,job_id,salary,commision,manag_id,dep_id]
    print("Records Successflly Added")
    print(df)
def rem_rec():
    print(""" 
    1. Remove using Index
    2. Remove using Employee_ID
    3. Remove the Column using Column Name""")
    ch = int(input("Enter Your Choice : "))
    if ch == 2:
        df = pd.read_csv("Emp.csv",index_col=0)
        f = int(input("Enter the Employee_ID to Delete : "))
        df.drop(f,inplace = True,axis = 0)
        print(df)
    elif ch == 1:
        df = pd.read_csv('Emp.csv')
        f = int(input("Enter Index to Delete : "))
        df.drop(f,inplace = True,axis = 0)
        print(df)
    elif ch == 3:
        df1 = pd.read_csv('Emp.csv')
        f = input("Enter Column Name to Delete : ")
        df1.drop(f,axis = 1,inplace = True)
        print(df1)
def dis_rec():
    print(pd.read_csv('Emp.csv'))
    
def upd_rec():
    df = pd.read_csv('Emp.csv')
    print("""
    1. Update Names of the Members based on Index
    2. Update Other Fields based on Names""")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        f = int(input("Enter the Index to Update Name : "))
        nm = input("Enter the First Name of the Person : ")
        nm1 = input("Enter the Last Name of the Person : ")
        df.loc[f,'FIRST_NAME'] = nm
        df.loc[f,"LAST_NAME"] = nm1
        print("Updated DataFrame")
        print(df)

def fin_rec():
    print("""
    1. Find Records on based on Index
    2. Find Records on based on FIRST_NAME""")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        df = pd.read_csv('Emp.csv')
        f = int(input("Enter Index to Find : "))
        print(df.loc[f,:])
    elif ch == 2:
        df = pd.read_csv('Emp.csv')
        f = input("Enter First Name to Find : ")
        print(df.loc[df['FIRST_NAME']==f])
def ex():
    import os
    print("1. Shutdown Computer Immediately")
    print("2. Shutdown Computer After Given Time")
    print("3. Restart Computer Immediately")
    print("4. Restart Computer After Given Time")
    print("5. Exit")
    print(end = "Enter Your Choice : ")
    choice = int(input())
    if choice == 1:
        os.system("Shutdown /s /t 0")
    elif choice == 2:
        print(end = "Enter Number of Seconds : ")
        sec = int(input())
        StrOne = "Shutdown /s /t"
        StrTwo = str(sec)
        Str = StrOne + StrTwo
        os.system(Str)
    elif choice == 3:
        os.system("Shutdown /r /t 0")
    elif choice == 4:
        sec = int(input("Enter Number of Seconds : "))
        StrOne = "Shutdown /r /t"
        StrTwo = str(sec)
        Str = StrOne + StrTwo
        os.system(Str)
    elif choice == 5:
        exit()
    else:
        print("Wrong Choice")
        menuset()
        
menu()
