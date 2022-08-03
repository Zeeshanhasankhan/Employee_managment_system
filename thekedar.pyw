from asyncore import read, write
from audioop import add
from cProfile import label
import json
from msilib.schema import ComboBox
from re import search
from textwrap import fill
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
    

root= Tk()
root.geometry("1390x720")
root.title("Central Warehouse")


#>>>
location=0
#funtions
def done():
    file=open("emp.json","r")
    emp=json.load(file)
    if searchvalue.get() in emp["name"]:
        print("found")
        global location
        location=emp["name"].index(searchvalue.get())
        print(location)
        
#Searchbar
        
        Label(searchframe,text=(emp["intime"][location]),font=("monospace","12")).place(x=12,y=130)   
        
        Label(searchframe,text=(emp["outtime"][location]),font=("monospace","12")).place(x=15,y=230)
        
    else:
        Label(searchframe,text="Not Found",pady=5).place(x=12,y=130)
        
        Label(searchframe,text="Not Found",pady=5).place(x=15,y=230)
        
#////

searchvalue=StringVar()

searchframe=Frame(root,background="pink",padx=25,pady=50)
searc=Entry(searchframe,textvariable=searchvalue).pack(anchor=NW)
submit=Button(searchframe,text="Search",font=("monospace","12","bold"),command=done).pack(anchor=NW)
searchframe.pack(side="left",fill="y")


#We read our json file and all json data store in "data" variable.

def add():
    file=open("emp.json","r")
    fileread=file.read()
    data=json.loads(fileread)
    file.close()

    
    #Now we add input data values into "data" variable
    data["name"].append(namevalue.get())
    data["intime"].append(intimevalue.get())
    data["outtime"].append(outtimevalue.get())
    
    

    
#then replace new data from old data
    file2=open("emp.json","w")
    add=json.dumps(data,indent=4)
    file2.write(add)
    
    namein.delete(0,END)
    outin.delete(0,END)
    inin.delete(0,END)
    messagebox.showinfo("Done","data have been submited")
    
namevalue=StringVar()
intimevalue=StringVar()
outtimevalue=StringVar()

f1=Frame()

Label(root,text="Central Warehouse",font=("space mono","28","bold","underline"), bg="blue",fg="white",padx=35,pady=20).pack()
Label(root,text="For Other Employee",font=("monospace","16"),fg="blue").pack()

Label(root,text="SUBMIT ATTENDENCE",font=("Monaco","16"),pady=30).pack()


#Main
Label(searchframe,text="Intime",font=("spacemono","18","bold")).place(x=0,y=100)
Label(searchframe,text="Outtime",font=("spacemono","18","bold")).place(x=0,y=200)
Label(searchframe,text="Date",font=("monospace","18","bold")).place(x=15,y=280)


name=Label(f1,text="NAME :",font=("Monaco","14"),padx=30,pady=30).grid(row=1,column=1)
namein=Entry(f1,textvariable=namevalue,width=30)
namein.grid(row=1,column=2)

intime=Label(f1,text="INTIME :",font=("Monaco","14"),padx=30,pady=30)
intime.grid(row=2,column=1)

inlist=["7:00AM","8:30AM","3:00PM","5:00PM","7:00PM","8:00PM","11:00PM"]
inin=ttk.Combobox(f1,values=inlist,textvariable=intimevalue,width=30)
inin.grid(row=2,column=2)

out=Label(f1,text="OUTIME :",font=("Monaco","14"),padx=30,pady=30).grid(row=3,column=1)
outin=ttk.Combobox(f1,values=inlist,textvariable=outtimevalue,width=30)
outin.grid(row=3,column=2)

submit=Button(f1,text="SUBMIT",font=("spacemono","14"),command=add)
submit.grid(row=4,column=1)
f1.pack()
quit=Button(text="Quit",font=("spacemono","14"),command=root.quit).pack(side="bottom")

root.state("zoomed")
root.mainloop()