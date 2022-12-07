from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import mysql.connector as sqltor

db =sqltor.connect(host = 'localhost',
                   user = 'root' ,
                   passwd = 'admin')

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS BILLING_SOFT")
cursor.execute('''USE BILLING_SOFT;
                CREATE TABLE IF NOT EXISTS INVOICE (invoice_number int primary key ,
                customer_name varchar(30),
                customer_id varchar(10),
                date date ,
                amount float(9,2))''')

#INSERTING DATA INTO DB
def Save():
    db =sqltor.connect(host = 'localhost',
                   user = 'root' ,
                   passwd = 'admin',
                   database = 'BILLING_SOFT')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO INVOICE VALUES
              (%s,'%s','%s','%s','%s')'''%(invoice_number.get(),customer_name.get(),customer_id.get(),date_entry.get(),grandtotal.get()))
    db.commit()
    db.close()
    
#TO ADD TOTAL COST        
def Calc():
    subtotal.delete(0,END)
    grandtotal.delete(0,END)
    tax.delete(0,END)

    lst = []
    for i in range(20):
        if tree.exists(i):
            lst.append(i)
    p = []
    for i in lst:
        item = tree.item(str(i))
        rec = item['values'][4]
        p.append(rec)
    SUM = sum(p)
    p = []
    subtotal.insert(0,str(float(SUM)))
    tax.insert(0,str(SUM*0.18))
    grandtotal.insert(0,str(SUM*1.18))
    
#TO INSERT ITEMS
def input_record():
    global count
    if id_entry.get()!= '' and UP_entry.get() != ''and QNTY_entry.get() != ''and ProductName_entry.get()!= '':
        if id_entry.get().isdigit() and UP_entry.get().isdigit() and QNTY_entry.get().isdigit():          
            prod = int(QNTY_entry.get()) * int(UP_entry.get())   
            tree.insert('', index = END,iid = count,values=(id_entry.get(),
                                            ProductName_entry.get(),
                                            QNTY_entry.get(),
                                            UP_entry.get(),
                                            prod))

            count += 1
            id_entry.delete(0,END)
            ProductName_entry.delete(0,END)
            QNTY_entry.delete(0,END)
            UP_entry.delete(0,END)
        else:
            tkinter.messagebox.showinfo("WARNING!!!!!!","Enter Valid Entries!! ")

    else:
        tkinter.messagebox.showinfo("WARNING.",  "Enter all the feilds !! ")

#TO REMOVE SELECTED ITEM
def remove_record():
    for i in tree.selection():
        tree.delete(i)

#CREATING THE GUI
window = Tk()
window.geometry("700x600")
bg = PhotoImage(file='bg.png')
label_BG = Label(window, image=bg)
label_BG.place(x=0, y=0)
title_txt = Label(window, text="INVOICING SOFTWARE",font="times 28 bold")
title_txt.place(x=350, y=20, anchor="center")

label9=Label(window,text="CUSTOMER DETAILs",font="times 18")
label9.place(x=25,y=50)
 
label10=Label(window,text="INVOICE NO",font="times 12")
label10.place(x=25,y=100)
invoice_number=Entry(window)
invoice_number.place(x=130,y=100)
 
label11=Label(window,text="DATE",font="times 12")
label11.place(x=500,y=100)
date_entry =Entry(window)
date_entry.place(x=550,y=100)
 
label12=Label(window,text="CUSTOMER NAME: ",font="times 12")
label12.place(x=25,y=125)
customer_name=Entry(window)
customer_name.place(x=180,y=125)
 
label13=Label(window,text="Phone NO.",font="times 12")
label13.place(x=25,y=150)
phone_number =Entry(window)
phone_number.place(x=110,y=150)
 
label13=Label(window,text="CUSTOMER ID",font="times 12")
label13.place(x=250,y=150)
customer_id=Entry(window)
customer_id.place(x=365,y=150)

#CREATING TABLE
columns = ('PID', 'PNAME', 'QTY','U_PRICE','TOTAL')
tree = ttk.Treeview(window, columns=columns, show='headings')

tree.column('PID', width=60)
tree.column('PNAME', width=200)
tree.column('QTY', width=100)
tree.column('U_PRICE', width=100)
tree.column('TOTAL', width=100)


tree.heading('PID', text='ProductID')
tree.heading('PNAME', text='ProductName')
tree.heading('QTY', text='Quantity')
tree.heading('U_PRICE', text='UNIT PRICE')
tree.heading('TOTAL', text='TOTAL')

#INSERTING DATA INTO THE TABLE
global count
count=0
data  = []
for record in data:      
    tree.insert(parent='',index='end'
               ,iid = count,text='',values=record)      
    count += 1
    
tree.pack(side = BOTTOM,expand = True , fill = X)

##INSERT FEATURES
Input_frame = Frame(window)
Input_frame.place(x=25,y=525)

id = Label(Input_frame,text="ProductID")
id.grid(row=0,column=0)

ProductName= Label(Input_frame,text="ProductName")
ProductName.grid(row=0,column=1)

QNTY = Label(Input_frame,text="Quantity")
QNTY.grid(row=0,column=2)

UP = Label(Input_frame,text="UNIT PRICE")
UP.grid(row=0,column=3)

id_entry = Entry(Input_frame)
id_entry.grid(row=1,column=0)

ProductName_entry = Entry(Input_frame)
ProductName_entry.grid(row=1,column=1)

QNTY_entry = Entry(Input_frame)
QNTY_entry.grid(row=1,column=2)

UP_entry = Entry(Input_frame)
UP_entry.grid(row=1,column=3)

subtotallable = Label(window,text='SUBTOTAL :>>>',font="times 14")
subtotallable.place(x=400,y=415)

subtotal = Entry(window,width = 10,font = ('Arial',16))
subtotal.place(x=550,y=415)

taxlable=Label(window,text='18% GST:>>>',font="times 14")
taxlable.place(x=400,y=450)

tax=Entry(window,width = 10,font = ('Arial',16))
tax.place(x=550,y=450)

totallable=Label(window,text='TOTAL:>>>',font="times 14")
totallable.place(x=400,y=485)

grandtotal = Entry(window,width = 10,font = ('Arial',16))
grandtotal.place(x=550,y=485)

#BUTTONS
Insert_Button = Button(Input_frame,text = "INSERT PRODUCT",command= input_record)
Insert_Button.grid(row = 2, column = 2)
Remove_Button = Button(Input_frame,text = "REMOVE PRODUCT", command = remove_record)
Remove_Button.grid(row = 2, column = 1)
Total_Button = Button(Input_frame,text = "TOTAL",command= Calc)
Total_Button.grid(row = 2, column = 0)
Save_Button = Button(Input_frame,text = "SAVE",command= Save)
Save_Button.grid(row = 2, column = 3)

db.close()
window.mainloop()
