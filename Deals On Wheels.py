import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox

import mysql.connector
car=mysql.connector.connect(
    user='root', 
    password='venomous',
    host='localhost',
    database='COMP_PROJECT')
mycursor=car.cursor()






#25.SQL QUERIES
def sql_queries():
    mycursor.execute('''CREATE TABLE BOOKING_CARS(BOOKING_ID VARCHAR(5),CUSTOMER_NAME VARCHAR(30),
    DOB DATE,BRAND VARCHAR(20),MODEL VARCHAR(20),COLOUR VARCHAR(20),EMAIL_ID VARCHAR(50),PHNO BIGINT,EMPLOYEE VARCHAR(20),PRICE BIGINT)''')
    mycursor.execute('''CREATE TABLE BOOKING_ACCESSORIES(BOOKING_ID VARCHAR(5),CUSTOMER_NAME VARCHAR(30),
    DOB DATE,ACCESSORIES VARCHAR(30),QTY INT,EMAIL_ID VARCHAR(50),PHNO BIGINT,EMPLOYEE VARCHAR(20),TOTAL_PRICE BIGINT)''')
    mycursor.execute("CREATE TABLE COMPANY_LOGIN(COMP_ID INT PRIMARY KEY,NAME VARCHAR(30),PASSWORD INT,JOB VARCHAR(15))")
    mycursor.execute("CREATE TABLE CARS(SLNO INT, BRAND VARCHAR(15), MODEL VARCHAR(15), PRICE BIGINT)")
    mycursor.execute("CREATE TABLE ACCESSORIES(SLNO INT, NAME VARCHAR(15), PRICE BIGINT)")
    SQL1="INSERT INTO CARS(SLNO,BRAND,MODEL,PRICE) VALUES(%s,%s,%s,%s)"
    SQL2="INSERT INTO ACCESSORIES(SLNO,NAME,PRICE) VALUES(%s,%s,%s)"
    SQL3="INSERT INTO COMPANY_LOGIN(EMP_ID,NAME,PASSWORD,JOB) VALUES(%s,%s,%s,%s)"
    L1=[[1,'HYUNDAI','I20',1300000],[2,'HYUNDAI','VERNA',1200000],
    [3,'HYUNDAI','CRETA',1800000],[4,'HONDA','JAZZ',900000],[5,'HONDA','CITY',1500000],
    [6,'HONDA','WR-V',1000000],[7,'KIA','SONET',1100000],[8,'KIA','SELTOS',1600000],
    [9,'KIA','CARENS',1500000],[10,'MG','ASTOR',1300000],[11,'MG','HECTOR',1700000],
    [12,'MG','GLOSTER',3000000],[13,'TATA','ALTROZ',870000],[14,'TATA','HARRIER',2000000],
    [15,'TATA','SAFARI',2200000]]
    L2=[[1,'SPOILERS',10000],[2,'NAVIGATION',7000],[3,'JUMPER CABLE',1500],
    [4,'CAR COVER',1000],[5,'CAR VACUUM',2000],[6,'PUDDLE LAMP',2500],[7,'DOOR VISORS',2000],[8,'FOG LAMP',3000],[9,'FLOOR MATS',1700],
    [10,'AIR FILTER',5000]]
    L3=[[1001,'SAI',12345,'ADMIN'],[1002,'ANISH',67890,'ADMIN'],[1003,'VISHAL',24675,'EMPLOYEE'],
    [1004,'RISHIT',17684,'EMPLOYEE'],[1005,'SAAKSHI',29594,'EMPLOYEE'],[1006,'ADITI',14061,'EMPLOYEE'],[1007,'SHRUTI',25643,'EMPLOYEE'],[1008,'SURESH',59745,'EMPLOYEE']]
    for i in L1:
        mycursor.execute(SQL1,i)
    for i in L2:
        mycursor.execute(SQL2,i)
    for i in L3:
        mycursor.execute(SQL3,i)
    car.commit()





#24.GENERATING BOOKING ID
def customer_id():                                                                  
    import random
    import string
    characters = string.ascii_uppercase + string.digits
    book_id= ''.join(random.choice(characters) for i in range(5))
    return book_id






#23.BILL RECEIPT OF ACCESSORIES
def billreceipt_accessories():
    def back():
        window3.destroy()
    bookid=E1.get()
    mycursor.execute("SELECT * FROM BOOKING_ACCESSORIES")
    cars=mycursor.fetchall()
    L=[]
    for i in cars:
        if i[0]==bookid:
            L.append(i)
            
    label14=Label(window3,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",30)).place(x=350,y=80)
    label=Label(window3,text="BILL RECEIPT",fg='white',bg='black',font=("Stencil",24)).place(x=420,y=130)
    label1=Label(window3,text="BOOKING ID: "+L[0][0],fg='white',bg='black',font=("Stencil",11)).place(x=10,y=210)
    label2=Label(window3,text="CUSTOMER NAME: "+L[0][1],fg='white',bg='black',font=("Stencil",11)).place(x=10,y=230)
    label3=Label(window3,text="PHONE NUMBER: "+str(L[0][6]),fg='white',bg='black',font=("Stencil",11)).place(x=10,y=250)
    label4=Label(window3,text="EMAIL ID: "+L[0][5],fg='white',bg='black',font=("Stencil",11)).place(x=700,y=210)
    label5=Label(window3,text="DATE OF BOOKING: "+str(L[0][2]),fg='white',bg='black',font=("Stencil",11)).place(x=700,y=230)
    label9=Label(window3,text="ASST. EMPLOYEE: "+L[0][7],fg='white',bg='black',font=("Stencil",11)).place(x=700,y=250)
    label8=Label(window3,text="ACCESSORIES ",fg='white',bg='black',font=("Stencil",14)).place(x=150,y=300)
    label10=Label(window3,text="QUANTITY ",fg='white',bg='black',font=("Stencil",14)).place(x=450,y=300)
    label11=Label(window3,text="PRICE",fg='white',bg='black',font=("Stencil",14)).place(x=750,y=300)
    z=330
    amt=0
    for i in L:
        label6=Label(window3,text=i[3],fg='white',bg='black',font=("Stencil",11)).place(x=150,y=z)
        label7=Label(window3,text=str(i[4]),fg='white',bg='black',font=("Stencil",11)).place(x=450,y=z)
        label8=Label(window3,text=str(i[8]),fg='white',bg='black',font=("Stencil",11)).place(x=750,y=z)
        z=z+20
        amt=amt+i[8]
    label16=Label(window3,text="TOTAL BILL: "+str(amt),fg='white',bg='black',font=("Stencil",11)).place(x=660,y=z)
    label11=Label(window3,text="THANK YOU FOR CHOOSING US!!",fg='white',bg='black',font=("Stencil",16)).place(x=370,y=550)
    bt8=Button(window3,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
    bt8.place(x=900,y=550)






#22.BOOKING ID FOR BILL RECEIPT OF ACCESSORIES
def billingid_accessories():
    global window3
    global E1
    window3=tk.Tk()
    window3.title("BILLING")
    window3.geometry('1000x600')
    window3.configure(width=1000,height=700,bg='black')
    label8=Label(window3,text=" ENTER BOOKING ID: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=10,y=15)
    E1=Entry(window3)
    E1.place(x=150,y=15)
    bt6=Button(window3,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",12),command=billreceipt_accessories)
    bt6.place(x=280,y=10)






#21.BILL RECEIPT OF CARS
def billreceipt_cars():
    def back():
        window3.destroy()
    bookid=E1.get()
    mycursor.execute("SELECT * FROM BOOKING_CARS")
    cars=mycursor.fetchall()
    
    for i in cars:
        if i[0]==bookid:
            label14=Label(window3,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",30)).place(x=350,y=80)
            label=Label(window3,text="BILL RECEIPT",fg='white',bg='black',font=("Stencil",24)).place(x=420,y=130)
            label1=Label(window3,text="BOOKING ID: "+i[0],fg='white',bg='black',font=("Stencil",11)).place(x=10,y=210)
            label2=Label(window3,text="CUSTOMER NAME: "+i[1],fg='white',bg='black',font=("Stencil",11)).place(x=10,y=230)
            label3=Label(window3,text="PHONE NUMBER: "+str(i[7]),fg='white',bg='black',font=("Stencil",11)).place(x=10,y=250)
            label4=Label(window3,text="EMAIL ID: "+i[6],fg='white',bg='black',font=("Stencil",11)).place(x=10,y=270)
            label5=Label(window3,text="DATE OF BOOKING: "+str(i[2]),fg='white',bg='black',font=("Stencil",11)).place(x=10,y=290)
            label6=Label(window3,text="BRAND: "+i[3],fg='white',bg='black',font=("Stencil",11)).place(x=800,y=230)
            label7=Label(window3,text="MODEL: "+i[4],fg='white',bg='black',font=("Stencil",11)).place(x=800,y=250)
            label8=Label(window3,text="COLOUR: "+i[5],fg='white',bg='black',font=("Stencil",11)).place(x=800,y=270)
            label9=Label(window3,text="ASST. EMPLOYEE: "+i[8],fg='white',bg='black',font=("Stencil",11)).place(x=800,y=290)
            label10=Label(window3,text="BILL AMOUNT: "+str(i[9]),fg='white',bg='black',font=("Stencil",11)).place(x=800,y=310)
            label11=Label(window3,text="THANK YOU FOR CHOOSING US!!",fg='white',bg='black',font=("Stencil",16)).place(x=370,y=400)
    bt8=Button(window3,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
    bt8.place(x=900,y=450)        
            
            
    



#20.BOOKING ID FOR BILL RECEIPT OF CARS
def billingid_cars():
    global window3
    global E1
    window3=tk.Tk()
    window3.title("BILLING")
    window3.geometry('1000x500')
    window3.configure(width=1000,height=700,bg='black')
    label8=Label(window3,text=" ENTER BOOKING ID: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=10,y=15)
    E1=Entry(window3)
    E1.place(x=150,y=15)
    bt6=Button(window3,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",12),command=billreceipt_cars)
    bt6.place(x=280,y=10)
    






#19.BILL RECEIPT PAGE
def bill_receipt():
    window1.destroy()
    def back():
        window2.destroy()
        customer()
    global window2
    window2=tk.Tk()
    window2.title("BILLING")
    window2.geometry('1000x500')
    window2.configure(width=1000,height=700,bg='black')
    label5=Label(window2,text="BILL RECEIPT",fg='white',bg='black',font=("Stencil",20)).place(x=420,y=120)
    label4=Label(window2,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
    bt6=Button(window2,text="CARS",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=billingid_cars)
    bt6.place(x=400,y=200)
    bt7=Button(window2,text="ACCESSORIES",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=billingid_accessories)
    bt7.place(x=400,y=300)
    bt8=Button(window2,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
    bt8.place(x=900,y=450)

    





#18.ACCESSORIES UNDER EMPLOYEE NAME
def emp_accessories():
    global name
    window4=tk.Tk()
    window4.title("EMPLOYEE ACCESSORIES")
    window4.geometry('1000x500')
    window4.configure(width=1000,height=700,bg='black')
    mycursor.execute("SELECT BOOKING_ID,CUSTOMER_NAME,ACCESSORIES,QTY,PHNO,EMPLOYEE,TOTAL_PRICE FROM BOOKING_ACCESSORIES ")
    result=mycursor.fetchall()
    L=[]
    for i in result:
        if i[5]==name:
            L.append(i)

    if L==[]:
        label10=Label(window4,text=" YOU HAVE NO ORDERS CURRENTLY. ",fg='white',bg='black',font=("Stencil",14))
        label10.place(x=10,y=10)
    else:
        i=0
        for orders in L:
            for j in range(len(orders)):
                e=Entry(window4,width=15,fg="black")
                e.grid(row=i,column=j)
                e.insert(END,orders[j])
            
            i=i+1
        label10=Label(window4,text=" THESE ARE YOUR CURRENT ORDERS. ",fg='white',bg='black',font=("Stencil",14))
        label10.place(x=10,y=300)







#17.CARS UNDER EMPLOYEE NAME
def emp_cars():
    global name
    window4=tk.Tk()
    window4.title("EMPLOYEE CARS")
    window4.geometry('1000x500')
    window4.configure(width=1000,height=700,bg='black')
    mycursor.execute("SELECT BOOKING_ID,CUSTOMER_NAME,DOB,BRAND,MODEL,COLOUR,PHNO,EMPLOYEE,PRICE FROM BOOKING_CARS ")
    result=mycursor.fetchall()
    L=[]
    for i in result:
        if i[7]==name:
            L.append(i)

    if L==[]:
        label10=Label(window4,text=" YOU HAVE NO ORDERS CURRENTLY. ",fg='white',bg='black',font=("Stencil",14))
        label10.place(x=10,y=10)
    else:
        i=0
        for orders in L:
            for j in range(len(orders)):
                e=Entry(window4,width=15,fg="black")
                e.grid(row=i,column=j)
                e.insert(END,orders[j])
            
            i=i+1
        label10=Label(window4,text=" THESE ARE YOUR CURRENT ORDERS. ",fg='white',bg='black',font=("Stencil",14))
        label10.place(x=10,y=300)
    
            
    





#16.EMPLOYEE LOGIN
def employee1():
    global name
    name=E1.get()
    password=E2.get()
    mycursor.execute("SELECT NAME,PASSWORD FROM COMPANY_LOGIN")
    result=mycursor.fetchall()
    for i in result:
        if name in i:
            if i[1]==int(password):
                label9=Label(window2,text=" WELCOME "+name+" !!",fg='white',bg='black',font=("Stencil",10))
                label9.place(x=350,y=270)
                label10=Label(window2,text=" WHAT WOULD YOU LIKE TO CHECK? ",fg='white',bg='black',font=("Stencil",10))
                label10.place(x=350,y=290)
                bt7=Button(window2,text="CARS BOOKED",width=25,height=1,fg='white',bg='black',font=("Stencil",12),command=emp_cars)
                bt7.place(x=350,y=320)
                bt8=Button(window2,text="ACCESSORIES BOOKED",width=25,height=1,fg='white',bg='black',font=("Stencil",12),command=emp_accessories)
                bt8.place(x=350,y=370)
                break
            
            else:
                label9=Label(window2,text=" INCORRECT PASSWORD!! ",fg='white',bg='black',font=("Stencil",14))
                label9.place(x=350,y=290)
    else:
        label9=Label(window2,text=" YOU ARE NOT AN EMPLOYEE!! ",fg='white',bg='black',font=("Stencil",14))
        label9.place(x=350,y=290)



def company_employee():
    def back():
        window2.destroy()
    global window2
    global E1
    global E2
    window2=tk.Tk()
    window2.title("EMPLOYEE LOGIN")
    window2.geometry('1000x500')
    window2.configure(width=1000,height=700,bg='black')
    label2=Label(window2,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
    label7=Label(window2,text=" ENTER NAME: ",fg='white',bg='black',font=("Stencil",10))
    label7.place(x=350,y=150)
    label8=Label(window2,text=" ENTER PASSWORD: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=350,y=190)
    E1=Entry(window2)
    E1.place(x=500,y=150)
    E2=Entry(window2)
    E2.place(x=500,y=190)
    bt6=Button(window2,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",12),command=employee1)
    bt6.place(x=440,y=230)
    bt5=Button(window2,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
    bt5.place(x=880,y=440)
                
                


def admin_remove():
    def back():
        window4.destroy()
    window4=tk.Tk()
    window4.title("REMOVE")
    window4.geometry('1000x500')
    window4.configure(width=1000,height=700,bg='black')
    def remove():
        comp_id=E1.get()
        s='DELETE FROM COMPANY_LOGIN WHERE COMP_ID LIKE '+str(comp_id)
        mycursor.execute(s)
        car.commit()
        label6=Label(window4,text=" SUCCESSFULLY REMOVED! ",fg='white',bg='black',font=("Stencil",30))
        label6.place(x=10,y=400)

    global E1
    label6=Label(window4,text=" ENTER EMPLOYEE ID: ",fg='white',bg='black',font=("Stencil",10))
    label6.place(x=10,y=20)
    E1=Entry(window4)
    E1.place(x=200,y=20)
    bt5=Button(window4,text="DONE",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=remove)
    bt5.place(x=400,y=65)
    bt6=Button(window4,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
    bt6.place(x=880,y=440)



    

   


def admin_add():
    def back():
        window4.destroy()
    window4=tk.Tk()
    window4.title("ADD")
    window4.geometry('1000x500')
    window4.configure(width=1000,height=700,bg='black')
    def add():
        comp_id=E1.get()
        name=E2.get()
        password=E3.get()
        job=combo3.get()
        L=[comp_id,name,password,job]
        cust=(L)
        SQL=("INSERT INTO COMPANY_LOGIN(COMP_ID,NAME,PASSWORD,JOB) VALUES(%s,%s,%s,%s)")
        mycursor.execute(SQL,cust)
        car.commit()
        label6=Label(window4,text=" SUCCESSFULLY ADDED! ",fg='white',bg='black',font=("Stencil",30))
        label6.place(x=10,y=400)

    global E1
    global E2
    global E3
    global combo3
    label6=Label(window4,text=" ENTER EMPLOYEE ID: ",fg='white',bg='black',font=("Stencil",10))
    label6.place(x=10,y=20)
    label7=Label(window4,text=" ENTER NAME: ",fg='white',bg='black',font=("Stencil",10))
    label7.place(x=10,y=50)
    label8=Label(window4,text=" ENTER PASSWORD: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=10,y=80)
    label9=Label(window4,text=" ENTER JOB: ",fg='white',bg='black',font=("Stencil",10))
    label9.place(x=10,y=110)
    E1=Entry(window4)
    E1.place(x=200,y=20)
    E2=Entry(window4)
    E2.place(x=200,y=50)
    E3=Entry(window4)
    E3.place(x=200,y=80)
    Value=['EMPLOYEE','ADMIN']
    combo3=ttk.Combobox(window4,values=Value)
    combo3.set("SELECT")
    combo3.place(x=200,y=110)
    bt5=Button(window4,text="DONE",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=add)
    bt5.place(x=400,y=65)
    bt6=Button(window4,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
    bt6.place(x=880,y=440)


def admin1():
    def back():
        window3.destroy()
    global window3
    global name
    name=E1.get()
    password=E2.get()
    mycursor.execute("SELECT NAME,PASSWORD, JOB FROM COMPANY_LOGIN")
    result=mycursor.fetchall()
    for i in result:
        if name in i:
            if i[1]==int(password):
                if i[2]=='ADMIN':
                    window2.destroy()
                    window3=tk.Tk()
                    window3.title("ADMIN LOGIN")
                    window3.geometry('1000x500')
                    window3.configure(width=1000,height=700,bg='black')
                    mycursor.execute("SELECT COMP_ID,NAME,PASSWORD,JOB FROM COMPANY_LOGIN")
                    i=0
                    for orders in mycursor:
                        for j in range(len(orders)):
                            e=Entry(window3,width=20,fg="black")
                            e.grid(row=i,column=j)
                            e.insert(END,orders[j])
            
                        i=i+1
                    label2=Label(window3,text="WELCOME "+name+" !",fg='white',bg='black',font=("Stencil",20)).place(x=500,y=10)
                    bt6=Button(window3,text="ADD EMPLOYEE",width=15,height=1,fg='white',bg='black',font=("Stencil",12),command=admin_add)
                    bt6.place(x=500,y=80)
                    bt7=Button(window3,text="REMOVE EMPLOYEE",width=15,height=1,fg='white',bg='black',font=("Stencil",12),command=admin_remove)
                    bt7.place(x=700,y=80)
                    bt5=Button(window3,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
                    bt5.place(x=880,y=440)
                        
                    
                    
                    
                    
            




def company_admin():
    def back():
        window2.destroy()
    global window2
    global E1
    global E2
    window2=tk.Tk()
    window2.title("ADMIN LOGIN")
    window2.geometry('1000x500')
    window2.configure(width=1000,height=700,bg='black')
    label2=Label(window2,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
    label7=Label(window2,text=" ENTER NAME: ",fg='white',bg='black',font=("Stencil",10))
    label7.place(x=350,y=150)
    label8=Label(window2,text=" ENTER PASSWORD: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=350,y=190)
    E1=Entry(window2)
    E1.place(x=500,y=150)
    E2=Entry(window2)
    E2.place(x=500,y=190)
    bt6=Button(window2,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",12),command=admin1)
    bt6.place(x=440,y=230)
    bt5=Button(window2,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
    bt5.place(x=880,y=440)
    



#15.COMPANY LOGIN PAGE
def company():
    def back():
        window1.destroy()
    window1=tk.Tk()
    window1.title("COMPANY LOGIN")
    window1.geometry('1000x500')
    window1.configure(width=1000,height=700,bg='black')
    label1=Label(window1,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
    bt1=Button(window1,text="ADMIN LOGIN",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=company_admin)
    bt1.place(x=400,y=200)
    bt2=Button(window1,text="EMPLOYEE LOGIN",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=company_employee)
    bt2.place(x=400,y=300)
    bt5=Button(window1,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
    bt5.place(x=880,y=440)



#14.ACCESSORIES BOOKED
def final_accessories():
    name=E1.get()
    email=E2.get()
    phno=E3.get()
    custid=customer_id()
    str(custid)
    if '@' in email and len(phno)==10:
        mycursor.execute('SELECT NAME FROM COMPANY_LOGIN;')
        result1=mycursor.fetchall()
        rand=random.randint(0,8)-1
        employee=result1[rand][0]
        label=Label(window4,text="YOUR BILL AMOUNT IS Rs."+str(final_price),fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=320)
        label=Label(window4,text=" PLEASE NOTE: YOUR BOOKING ID IS "+custid+" AND THE EMPLOYEE HELPING YOU WOULD BE "+employee,fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=350)
        label=Label(window4,text=" YOUR BOOKING HAS BEEN SUCCESSFULLY COMPLETED!! ",fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=380)
        label=Label(window4,text=" THANK YOU FOR CHOOSING US!! ",fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=410)
        name=E1.get()
        email=E2.get()
        phno=E3.get()
        mycursor.execute('SELECT CURDATE()')
        result=mycursor.fetchall()
        for x in result:
            date=x[0]
        for i in items:
            L=[custid,name,date,i[0],int(i[1]),email,int(phno),employee,i[2]]
            cust=(L)
            SQL="INSERT INTO BOOKING_ACCESSORIES(BOOKING_ID,CUSTOMER_NAME,DOB,ACCESSORIES,QTY,EMAIL_ID,PHNO,EMPLOYEE,TOTAL_PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(SQL,cust)
            car.commit()
    else:
        messagebox.showwarning("ERROR","INCORRECT VALUES ENTERED.")
        window3.mainloop()






    
#13.CUSTOMER INFO OF ACCESSORIES
def billing_accessories():
    global E1
    global E2
    global E3
    label6=Label(window4,text=" CUSTOMER DETAILS: ",fg='white',bg='black',font=("Stencil",13))
    label6.place(x=10,y=200)
    label7=Label(window4,text=" ENTER NAME: ",fg='white',bg='black',font=("Stencil",10))
    label7.place(x=10,y=220)
    label8=Label(window4,text=" ENTER EMAIL ID: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=10,y=240)
    label9=Label(window4,text=" ENTER PHONE NUMBER: ",fg='white',bg='black',font=("Stencil",10))
    label9.place(x=10,y=260)
    E1=Entry(window4)
    E1.place(x=210,y=220)
    E2=Entry(window4)
    E2.place(x=210,y=240)
    E3=Entry(window4)
    E3.place(x=210,y=260)
    bt13=Button(window4,text="DONE",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=final_accessories)
    bt13.place(x=400,y=240)

final_price=0
items=[]







#12.ADDING ACCESORIES
def add_accessories():
    global final_price
    global items
    accessory=combo3.get()
    qty=E4.get()
    mycursor.execute('SELECT SLNO, NAME, PRICE FROM ACCESSORIES;')
    result=mycursor.fetchall()
    list1=result[int(accessory)-1]
    item=list1[1]
    price=list1[2]
    total_price=price*int(qty)
    final_price+=total_price
    L=[item,qty,total_price]
    items.append(L)
    
    
    
    
    


#11.BUYING ACCESSORIES PAGE   
def accessories():
    def back():
        global final_price
        global items
        window4.destroy()
        final_price=0
        items=[]
    global window4
    global combo3
    global E4

    window4=tk.Tk()
    window4.title("ACCESSORIES")
    window4.geometry('1000x500')
    window4.configure(width=1000,height=700,bg='black')

    label20=Label(window4,text=" CHOOSE THE ACCESSORIES YOU WOULD LIKE TO BUY FROM THE TABLE :) ",fg='white',bg='black',font=("Stencil",10))
    label20.place(x=400,y=40)

    bt15=Button(window4,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
    bt15.place(x=900,y=450)

    Value=[1,2,3,4,5,6,7,8,9,10]
    combo3=ttk.Combobox(window4,values=Value)
    combo3.set("SELECT OPTION")
    combo3.place(x=440,y=70)

    label21=Label(window4,text=" QTY: ",fg='white',bg='black',font=("Stencil",10))
    label21.place(x=400,y=100)

    E4=Entry(window4)
    E4.place(x=440,y=100)

    bt14=Button(window4,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=billing_accessories)
    bt14.place(x=440,y=130)

    bt20=Button(window4,text="ADD ITEM",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=add_accessories)
    bt20.place(x=530,y=130)

    mycursor.execute("SELECT SLNO,NAME,PRICE FROM ACCESSORIES")
    i=0
    for orders in mycursor:
        for j in range(len(orders)):
            e=Entry(window4,width=20,fg="black")
            e.grid(row=i,column=j)
            e.insert(END,orders[j])
            
        i=i+1







#10.CAR AND ACCESSORIES IS BOOKED
def final_cars_accessories():
    global final_price
    cars1=choice[0]
    colour1=choice[1]
    name=E1.get()
    email=E2.get()
    phno=E3.get()
    custid=customer_id()
    str(custid)
    if '@' in email and len(phno)==10:
        mycursor.execute('SELECT NAME FROM COMPANY_LOGIN;')
        result1=mycursor.fetchall()
        rand=random.randint(0,8)-1
        employee=result1[rand][0]
        label=Label(window4,text=" PLEASE NOTE: YOUR BOOKING ID IS "+custid+" AND THE EMPLOYEE HELPING YOU WOULD BE "+employee,fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=370)
        label=Label(window4,text=" YOUR BOOKING HAS BEEN SUCCESSFULLY COMPLETED!! ",fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=410)
        label=Label(window4,text=" THANK YOU FOR CHOOSING US!! ",fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=440)
        mycursor.execute('SELECT CURDATE()')
        result=mycursor.fetchall()
        for x in result:
            date=x[0]
        for i in items:
            L=[custid,name,date,i[0],int(i[1]),email,int(phno),employee,i[2]]
            cust=(L)
            SQL="INSERT INTO BOOKING_ACCESSORIES(BOOKING_ID,CUSTOMER_NAME,DOB,ACCESSORIES,QTY,EMAIL_ID,PHNO,EMPLOYEE,TOTAL_PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(SQL,cust)
            car.commit()
        mycursor.execute('SELECT SLNO,BRAND, MODEL, PRICE FROM CARS;')
        result1=mycursor.fetchall()
        list1=result1[int(cars1)-1]
        brand=list1[1]
        model=list1[2]
        price=list1[3]
        final_price+=price
        label=Label(window4,text=" YOUR TOTAL BILL AMOUNT IS "+str(final_price),fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=340)
        L=[custid,name,date,brand,model,colour1,email,int(phno),employee,price]
        cust=(L)
        SQL="INSERT INTO BOOKING_CARS(BOOKING_ID,CUSTOMER_NAME,DOB,BRAND,MODEL,COLOUR,EMAIL_ID,PHNO,EMPLOYEE,PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(SQL,cust)
        car.commit()
    else:
        messagebox.showwarning("ERROR","INCORRECT VALUES ENTERED.")
        window3.mainloop()
    







#9.BILLING ACCESSORIES AFTER CAR
def billing_car_accessories():
    global E1
    global E2
    global E3
    label6=Label(window4,text=" CUSTOMER DETAILS: ",fg='white',bg='black',font=("Stencil",13))
    label6.place(x=10,y=200)
    label7=Label(window4,text=" ENTER NAME: ",fg='white',bg='black',font=("Stencil",10))
    label7.place(x=10,y=220)
    label8=Label(window4,text=" ENTER EMAIL ID: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=10,y=240)
    label9=Label(window4,text=" ENTER PHONE NUMBER: ",fg='white',bg='black',font=("Stencil",10))
    label9.place(x=10,y=260)
    E1=Entry(window4)
    E1.place(x=210,y=220)
    E2=Entry(window4)
    E2.place(x=210,y=240)
    E3=Entry(window4)
    E3.place(x=210,y=260)
    bt13=Button(window4,text="DONE",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=final_cars_accessories)
    bt13.place(x=400,y=240)
    







#8.BUYING ACCESSORIES AFTER CAR
def cars_accessories():
    global choice
    cars=combo1.get()
    colour=combo2.get()
    choice=[cars,colour]
    window3.destroy()
    def back():
        global final_price
        global items
        window4.destroy()
        final_price=0
        items=[]
    global window4
    global combo3
    global E4

    window4=tk.Tk()
    window4.title("ACCESSORIES")
    window4.geometry('1000x500')
    window4.configure(width=1000,height=700,bg='black')

    label20=Label(window4,text=" CHOOSE THE ACCESSORIES YOU WOULD LIKE TO BUY FROM THE TABLE :) ",fg='white',bg='black',font=("Stencil",10))
    label20.place(x=400,y=40)

    bt15=Button(window4,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
    bt15.place(x=900,y=450)

    Value=[1,2,3,4,5,6,7,8,9,10]
    combo3=ttk.Combobox(window4,values=Value)
    combo3.set("SELECT OPTION")
    combo3.place(x=440,y=70)

    label21=Label(window4,text=" QTY: ",fg='white',bg='black',font=("Stencil",10))
    label21.place(x=400,y=100)

    E4=Entry(window4)
    E4.place(x=440,y=100)

    bt14=Button(window4,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=billing_car_accessories)
    bt14.place(x=440,y=130)

    bt20=Button(window4,text="ADD ITEM",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=add_accessories)
    bt20.place(x=530,y=130)

    mycursor.execute("SELECT SLNO,NAME,PRICE FROM ACCESSORIES")
    i=0
    for orders in mycursor:
        for j in range(len(orders)):
            e=Entry(window4,width=20,fg="black")
            e.grid(row=i,column=j)
            e.insert(END,orders[j])
            
        i=i+1
    
    
    


    
#7.DECIDING WHETHER TO BUY ACCESSORIES
def decision():
    global label0
    global bt14
    global bt15
    label0=Label(window3,text=" DO YOU WANT TO BUY ACCESSORIES?",fg='white',bg='black',font=("Stencil",10))
    label0.place(x=500,y=160)
    bt14=Button(window3,text="YES",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=cars_accessories)
    bt14.place(x=500,y=200)
    bt15=Button(window3,text="NO",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=billing_car)
    bt15.place(x=600,y=200)
    
    





    
#6.CAR IS BOOKED
def final_car():
    global final_price
    name=E1.get()
    email=E2.get()
    phno=E3.get()
    custid=customer_id()
    str(custid)
    if '@' in email and len(phno)==10:
        mycursor.execute('SELECT NAME FROM COMPANY_LOGIN;')
        result1=mycursor.fetchall()
        rand=random.randint(0,8)-1
        employee=result1[rand][0]
        label=Label(window3,text=" PLEASE NOTE: YOUR CUSTOMER ID IS "+custid+" AND THE EMPLOYEE HELPING YOU WOULD BE "+employee,fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=370)
        label=Label(window3,text=" YOUR BOOKING HAS BEEN SUCCESSFULLY COMPLETED!! ",fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=410)
        label=Label(window3,text=" THANK YOU FOR CHOOSING US!! ",fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=440)
        cars=combo1.get()
        colour=combo2.get()
        mycursor.execute('SELECT CURDATE()')
        result=mycursor.fetchall()
        for x in result:
            date=x[0]
        mycursor.execute('SELECT SLNO,BRAND, MODEL, PRICE FROM CARS;')
        result=mycursor.fetchall()
        list1=result[int(cars)-1]
        brand=list1[1]
        model=list1[2]
        price=list1[3]
        final_price+=price
        label=Label(window4,text=" YOUR TOTAL BILL AMOUNT IS "+str(final_price),fg='white',bg='black',font=("Stencil",14))
        label.place(x=10,y=340)
        L=[custid,name,date,brand,model,colour,email,phno,employee,price]
        cust=(L)
        SQL="INSERT INTO BOOKING_CARS(BOOKING_ID,CUSTOMER_NAME,DOB,BRAND,MODEL,COLOUR,EMAIL_ID,PHNO,EMPLOYEE,PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(SQL,cust)
        car.commit()

    else:
        messagebox.showwarning("ERROR","INCORRECT VALUES ENTERED.")
        window3.mainloop()







    
#5.CUSTOMER INFO OF CARS
def billing_car():
    label0.destroy()
    bt14.destroy()
    bt15.destroy()
    global E1
    global E2
    global E3
    label6=Label(window3,text=" CUSTOMER DETAILS: ",fg='white',bg='black',font=("Stencil",13))
    label6.place(x=500,y=120)
    label7=Label(window3,text=" ENTER NAME: ",fg='white',bg='black',font=("Stencil",10))
    label7.place(x=500,y=160)
    label8=Label(window3,text=" ENTER EMAIL ID: ",fg='white',bg='black',font=("Stencil",10))
    label8.place(x=500,y=180)
    label9=Label(window3,text=" ENTER PHONE NUMBER: ",fg='white',bg='black',font=("Stencil",10))
    label9.place(x=500,y=200)
    E1=Entry(window3)
    E1.place(x=700,y=160)
    E2=Entry(window3)
    E2.place(x=700,y=180)
    E3=Entry(window3)
    E3.place(x=700,y=200)
    bt13=Button(window3,text="DONE",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=final_car)
    bt13.place(x=600,y=230)
    
    






#4.BUYING CARS PAGE
def cars():
    def back():
        window3.destroy()
    global window3
    global combo1
    global combo2
    window3=tk.Tk()
    window3.title("CARS")
    window3.geometry('1000x500')
    window3.configure(width=1000,height=700,bg='black')

    bt9=Button(window3,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
    bt9.place(x=900,y=450)

    label4=Label(window3,text=" CHOOSE THE CAR YOU WOULD LIKE TO BUY FROM THE TABLE :) ",fg='white',bg='black',font=("Stencil",10))
    label4.place(x=500,y=50)

    Value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    combo1=ttk.Combobox(window3,values=Value)
    combo1.set("SELECT OPTION")
    combo1.place(x=500,y=70)

    Value=['BLACK','WHITE','RED','SILVER','BLUE','ORANGE']
    combo2=ttk.Combobox(window3,values=Value)
    combo2.set("SELECT COLOUR")
    combo2.place(x=500,y=90)

    bt10=Button(window3,text="SUBMIT",width=8,height=1,fg='white',bg='black',font=("Stencil",9),command=decision)
    bt10.place(x=700,y=72)

    mycursor.execute("SELECT SLNO,BRAND,MODEL,PRICE FROM CARS")
    i=0
    for orders in mycursor:
        for j in range(len(orders)):
            e=Entry(window3,width=20,fg="black")
            e.grid(row=i,column=j)
            e.insert(END,orders[j])
            
        i=i+1
    







#3.BUYING PAGE           
def buying():
        window1.destroy()
        def back():
            window2.destroy()
            customer()
        global window2
        window2=tk.Tk()
        window2.title("BUYING")
        window2.geometry('1000x500')
        window2.configure(width=1000,height=700,bg='black')
        label3=Label(window2,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
        bt6=Button(window2,text="CARS",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=cars)
        bt6.place(x=400,y=200)
        bt7=Button(window2,text="ACCESSORIES",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=accessories)
        bt7.place(x=400,y=300)
        bt8=Button(window2,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",10),command=back)
        bt8.place(x=900,y=450)







#2.CUSTOMER LOGIN PAGE
def customer():
    def back():
        window1.destroy()
    global window1
    window1=tk.Tk()
    window1.title("CUSTOMER LOGIN")
    window1.geometry('1000x500')
    window1.configure(width=1000,height=700,bg='black')
    label2=Label(window1,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
    bt3=Button(window1,text="BUYING",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=buying)
    bt3.place(x=400,y=200)
    bt4=Button(window1,text="BILL RECEIPT",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=bill_receipt)
    bt4.place(x=400,y=300)
    bt5=Button(window1,text="BACK",width=10,height=2,fg='white',bg='black',font=("Stencil",12),command=back)
    bt5.place(x=880,y=440)








#1.MAIN MENU OF PROGRAM
def mainmenu():
    global window
    window=tk.Tk()
    window.title("WELCOME!")
    window.geometry('1000x500')
    window.configure(width=1000,height=700,bg='black')
    label1=Label(window,text="DEALS ON WHEELS",fg='white',bg='black',font=("Stencil",45)).place(x=270,y=30)
    bt1=Button(window,text="CUSTOMER LOGIN",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=customer)
    bt1.place(x=400,y=200)
    bt2=Button(window,text="COMPANY LOGIN",width=20,height=2,fg='white',bg='black',font=("Stencil",12),command=company)
    bt2.place(x=400,y=300)
    window.mainloop()
   

'''print("1.CREATE SQL DATABASE")
print("2.RUN APPLICATION")
ch=int(input("ENTER YOUR CHOICE: "))
if ch==1:
    sql_queries()
elif ch==2:'''
mainmenu()












