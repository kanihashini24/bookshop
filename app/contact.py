# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:55:27 2022

@author: DS
"""

from tkinter import*
#import tkinter.messagebox as tkMessageBox
import sqlite3
top=Tk()
top.geometry('300x300')
Name=StringVar()
Gender=StringVar()
def database():
   name1=Name.get()
   gen=Gender.get()
   conn = sqlite3.connect('goutham.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS student (Name TEXT, Gender TEXT)')
   cursor.execute('INSERT INTO student (Name, Gender) \
                  VALUES(?,?)', (name1, gen))
   conn.commit()
lab1=Label(top, text="Save details")
lab1.place(x=120, y=10)
lab2=Label(top, text="Name")
lab2.place(x=40, y=40)
ent1=Entry(top, textvariable=Name )
ent1.place(x=120, y=40)
lab3=Label(top, text="Gender")
lab3.place(x=40, y=70)
ent2=Entry(top, textvariable=Gender)
ent2.place(x=120, y=70)
sav=Button(top, text="Save", command=database)
sav.place(x=140, y=100)
top.mainloop()