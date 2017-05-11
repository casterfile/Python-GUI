from tkinter import *

myGui = Tk()
myGui.title("Hello World")
myGui.geometry("500x500+0+0")#WxH+X+Y
myLabel1 = Label(text='This is a label',fg='red', bg='yellow')
myLabel1.place(x=10,y=10)
myLabel2 = Label(text='This is the second label',fg='blue', bg='green').place(x=50,y=10)
myGui.mainloop()#Program will run on the loop
