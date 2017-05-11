from tkinter import *

myGui = Tk()
myGui.title("Hello World")
myGui.geometry("500x500+0+0")#WxH+X+Y
myLabel1 = Label(text='myLabel1').grid(row=0,column=0, sticky='w')
myLabel2 = Label(text='myLabel2 myLabel2').grid(row=1,column=0)
myLabel3 = Label(text='myLabel3 myLabel3 myLabel3').grid(row=2,column=0)
myLabel4 = Label(text='myLabel4 myLabel4 myLabel4 myLabel4').grid(row=2,column=1)
myGui.mainloop()#Program will run on the loop
