
from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
name = Label(top, text = "Name").place(x = 40,y = 60)  
  
email = Label(top, text = "Email").place(x = 40, y = 90)  
  
password = Label(top, text = "Password").place(x = 40, y = 130)  
  
sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 40, y = 170)  
  
e1 = Entry(top).place(x = 80, y = 60)  
  
  
e2 = Entry(top).place(x = 80, y = 90)  
  
  
e3 = Entry(top).place(x = 80, y = 130)  
  
top.mainloop()  