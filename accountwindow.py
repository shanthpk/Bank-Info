# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 11:47:35 2023

@author: Shanthi Pandiyarajan
"""

from sqlite3 import *
from bankdbaccess import*
from tkinter import*
from tkinter import messagebox
from tkinter import ttk as tk

def validation():
    
    eacno=acno.get()
    if len(eacno)==0:
        errormsg.set("Account No should not be blank")
        return False
    
    eacno=acno.get()
    if len(eacno)<6 or len(eacno)>6:
        errormsg.set("Account No should be 6 digit")
        return False
    
    ename=name.get()
    if len(ename)==0:
        errormsg.set("Name should not be blank")
        return False
    
    eadh=adh.get()
    if int(eadh)==0:
        errormsg.set("Aadhaar No should not be blank")
        return False
    eadh=adh.get()
    if len(eadh)<8 or len(eadh)>8:
        errormsg.set("Aadhaar No should be 8 digit")
        return False
    
    eactp=actp.get()
    if len(eactp)==0:
        errormsg.set("Account type should not be blank")
        return False
    
    edob=dob.get()
    if len(edob)==0:
        errormsg.set("Date of Birth should not be blank")
        return False
    
    eadd=add.get()
    if len(eadd)==0:
        errormsg.set("Address should not be blank")
        return False
    
    enlty=box.get()
    if len(enlty)==0:
        errormsg.set("Nationality should not be blank")
        return False 
    
    cc1=info1.get()
    cc2=info2.get()
    cc3=info3.get()
    cc4=info4.get()
    if (cc1==0 and cc2==0 and cc3==0 and cc4==0):
        errormsg.set("Information should not be blank")
        return False
   
    errormsg.set("")
    return True
        

def valueassign():
    Acno=acno.get()
    Name=name.get()
    Actp=actp.get()
    DOB=dob.get()
    gvalue=""
    I1=""
    I2=""
    I3=""
    I4=""
    if gender.get()==1:
        gvalue="M"
    elif gender.get()==2:
        gvalue="F"
    Add=add.get()
    Adh=adh.get()
    Nlty=box.get()
    
    if info1.get()==1:
        I1="SMS"
    else:
        I1=""
    
    if info2.get()==1:
        I2="Email"
    else:
        I2=""
        
    if info3.get()==1:
        I3="Postal"
    else:
        I3=""
        
    if info4.get()==1:
        I4="Other"
    else:
        I4=""
        
    infov="-".join([I1,I2,I3,I4])
    
    eobj=bankinfodbaccess()
    eobj.acno=Acno
    eobj.name=Name
    eobj.actp=Actp
    eobj.dob=DOB
    eobj.gender=gvalue
    eobj.add=Add
    eobj.adh=Adh
    eobj.nlty=Nlty
    eobj.info=infov
    return eobj

def clearcontrol():
    acno.set("")
    name.set("")
    actp.set("")
    dob.set("")
    add.set("")
    adh.set("")
    nlty.set("")
    gender.set(None)
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect() 
    
#def sbtn():
 #  e=valueassign()
#    adb=bankDB()
 #   adb.addrecord(e)
  #  errormsg.set("Record saved successfully")
   # return

def search():
    name.set("")
    actp.set("")
    dob.set("")
    add.set("")
    adh.set("")
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect() 
    nlty.set("")
    if len(acno.get())==0:
        errormsg.set("Account No should be enter...")
        return
    adb=bankDB()
    found,e=adb.search(acno.get())
    
    if found:
        acno.set(e.acno)
        name.set(e.name)
        actp.set(e.actp)
        dob.set(e.dob)
        add.set(e.add)
        adh.set(e.adh)
        box.set(e.nlty)
        if e.gender=="M":
            e_gender.select()
        elif e.gender=="F":
            e_gender1.select()
            
        if str(e.info).find("SMS")>=0:
            c1.select()
        
        if str(e.info).find("Email")>=0:
            c2.select()
            
        if str(e.info).find("Postal")>=0:
            c3.select()
            
        if str(e.info).find("Other")>=0:
            c4.select()
            
        errormsg.set("Record showed successfully")
        edbtn.config(state=NORMAL)
        delbtn.config(state=NORMAL)
        
    else:
        errormsg.set("Record not found")
        edbtn.config(state=DISABLED)
        delbtn.config(state=DISABLED)
        
        
def delrecord():
    yes=messagebox.askyesno("Remove Records", "Do you want delete this record")
    if yes:
        e=bankDB()
        e.delrecord(acno.get())
        messagebox.showinfo("Delete","Record deleted sucessfully...")
    return

def newrecord():
    global exitflag
    control(NORMAL)
    nbtn.config(state=DISABLED)
    edbtn.config(state=DISABLED)
    delbtn.config(state=DISABLED)
    sbtn.config(state=NORMAL)
    ebtn.config(text="Cancel")
    exitflag=False
    
def newb():
    global saveflag
    saveflag=1
    newrecord()
    clearcontrol()
    
    
def editb():
    global saveflag
    saveflag=2
    newrecord()
    e_acno.config(state=DISABLED)
    
    
def saverecord():
    global exitflag
    global saveflag
    
    if saveflag==1:
     if  validation():
         e=valueassign()
         adb=bankDB()
         adb.addrecord(e)
         errormsg.set("Record saved successfully")
       
    elif saveflag==2:
     if  validation():
           e=valueassign()
           adb=bankDB()
           adb.updaterecord(e)
           errormsg.set("Record updated successfully")
     
    ebtn.config(text="Exit")
    exitflag=True
    control(DISABLED)
    sbtn.config(state=DISABLED)
    edbtn.config(state=DISABLED)
    delbtn.config(state=DISABLED)
    nbtn.config(state=NORMAL)
    
def appquit():
    global exitflag
    if exitflag:
        mainwin.destroy()
    else:
        clearcontrol()
        edbtn.config(text="Exit")
        exitflag=True
        control(DISABLED)
        nbtn.config(state=NORMAL)
        edbtn.config(state=DISABLED)
        delbtn.config(state=DISABLED)
        sbtn.config(state=DISABLED)
        
def control(s):
    
    e_name.config(state=s)
    e_gender.config(state=s)
    e_gender1.config(state=s)
    e_actp.config(state=s)
    e_dob.config(state=s)
    e_add.config(state=s)
    e_adh.config(state=s)
    c1.config(state=s)
    c2.config(state=s)
    c3.config(state=s)
    c4.config(state=s)
    box.config(state=s)
    #e_basicpay.config(state=s)
    sbtn.config(state=s)
    edbtn.config(state=s)
    delbtn.config(state=s)
        
    
    
        
        
mainwin=Tk()
mainwin.geometry("650x900")

exitflag=True
saveflag=1

lblhead=Label(mainwin,text="Welcome to IOB",fg="blue",font="Times 16 bold")
lblhead.place(x=225,y=10)


lblh1=Label(mainwin,text="Enter Account No",font="Arial 14 bold")
lblh1.place(x=30,y=50)
acno=StringVar()
e_acno=Entry(mainwin,textvariable=acno,bd=2,font="helvetica 10")
e_acno.place(x=220,y=50,width=150,height=30)


lblh2=Label(mainwin,text="Enter the Name",font="Arial 14 bold")
lblh2.place(x=30,y=100)
name=StringVar()
e_name=Entry(mainwin,textvariable=name,bd=2,font="helvetica 10")
e_name.place(x=220,y=100,width=250,height=30)



lblh3=Label(mainwin,text="Account Type",font="Arial 14 bold")
lblh3.place(x=30,y=150)
actp=StringVar()
e_actp=Entry(mainwin,textvariable=actp,bd=2,font="helvetica 10")
e_actp.place(x=220,y=150,width=250,height=30)

lblh4=Label(mainwin,text="Date of Birth",font="Arial 14 bold")
lblh4.place(x=30,y=200)
dob=StringVar()
e_dob=Entry(mainwin,textvariable=dob,bd=2,font="helvetica 10")
e_dob.place(x=220,y=200,width=150,height=30)

lblh5=Label(mainwin,text="Gender",font="Arial 14 bold")
lblh5.place(x=30,y=250)
gender=IntVar()
e_gender=Radiobutton(mainwin,text="Male",variable=gender,value=1)
e_gender.place(x=220,y=250)
e_gender1=Radiobutton(mainwin,text="Female",variable=gender,value=2)
e_gender1.place(x=280,y=250)

lblh6=Label(mainwin,text="Address",font="Arial 14 bold")
lblh6.place(x=30,y=300)
add=StringVar()
e_add=Entry(mainwin,textvariable=add,bd=2,font="helvetica 10")
e_add.place(x=220,y=300,width=250,height=30)
 

lblh7=Label(mainwin,text="Aadhaar Number",font="Arial 14 bold")
lblh7.place(x=30,y=350)
adh=StringVar()
e_adh=Entry(mainwin,textvariable=adh,bd=2,font="helvetica 10")
e_adh.place(x=220,y=350,width=250,height=30)



lblh8=Label(mainwin,text="Nationality",font="Arial 14 bold")
lblh8.place(x=30,y=400)
nlty=StringVar()
entries=("India","Pakistan","China","America")
box=tk.Combobox(mainwin,value=entries,textvariable=nlty)
box.place(x=220,y=400)



lblh9=Label(mainwin,text="Information Via",font="Arial 14 bold")
lblh9.place(x=30,y=490)
info1=IntVar()
info2=IntVar()
info3=IntVar()
info4=IntVar()
c1=Checkbutton(mainwin,text="SMS",variable=info1,onvalue=1,offvalue=0,height=3,width=15)
c2=Checkbutton(mainwin,text="Email",variable=info2,onvalue=1,offvalue=0,height=3,width=15)
c3=Checkbutton(mainwin,text="Postal",variable=info3,onvalue=1,offvalue=0,height=3,width=15)
c4=Checkbutton(mainwin,text="Other",variable=info4,onvalue=1,offvalue=0,height=3,width=15)
c1.place(x=210,y=479)
c2.place(x=360,y=479)
c3.place(x=210,y=529)
c4.place(x=360,y=529)


shbtn=Button(mainwin,text='Search',bg="cyan",fg="black",command=search)
shbtn.place(x=390,y=50,width=60,height=30)

sbtn=Button(mainwin,text="Save",bg="blue",fg="white",command=saverecord)
sbtn.place(x=70,y=580,width=100,height=30)

nbtn=Button(mainwin,text="New",bg="green",fg="white",command=newb)
nbtn.place(x=170,y=580,width=100,height=30)

edbtn=Button(mainwin,text="Edit",bg="pink3",fg="white",command=editb)
edbtn.place(x=270,y=580,width=100,height=30)

delbtn=Button(mainwin,text="Delete",bg="orange",fg="white",command=delrecord)
delbtn.place(x=370,y=580,width=100,height=30)


ebtn=Button(mainwin,text="Exit",bg="red",fg="white",command=mainwin.destroy)
ebtn.place(x=470,y=580,width=100,height=30)


errormsg=StringVar()
lblerror=Label(mainwin,textvariable=errormsg,font="Arial 12 bold",fg="red",wraplength="400")
lblerror.place(x=180,y=650)


cln=Label(mainwin,text=":",font="Arial 14 bold")
cln.place(x=200,y=50)
cln1=Label(mainwin,text=":",font="Arial 14 bold")
cln1.place(x=200,y=100)
cln2=Label(mainwin,text=":",font="Arial 14 bold")
cln2.place(x=200,y=150)
cln3=Label(mainwin,text=":",font="Arial 14 bold")
cln3.place(x=200,y=200)
cln4=Label(mainwin,text=":",font="Arial 14 bold")
cln4.place(x=200,y=250)
cln5=Label(mainwin,text=":",font="Arial 14 bold")
cln5.place(x=200,y=300)
cln6=Label(mainwin,text=":",font="Arial 14 bold")
cln6.place(x=200,y=350)
cln7=Label(mainwin,text=":",font="Arial 14 bold")
cln7.place(x=200,y=400)
cln8=Label(mainwin,text=":",font="Arial 14 bold")
cln8.place(x=200,y=490)
control(DISABLED)
mainwin.mainloop()
