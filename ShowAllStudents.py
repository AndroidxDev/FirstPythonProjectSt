from tkinter import *
import data

windowTk = None

def ShowAllStudents(root):
    global windowTk
    if  windowTk is not None and windowTk.winfo_exists():
        print("NONMOOOONONOO ITS NOT NEED FOR U BROO xd2")
        windowTk.lift()
    else: 
        windowTk = Toplevel(root)
        windowTk.title("Show students")

    counter = -1
    for i in data.students:
        counter += 1
        text = Label(windowTk, text="Name: " + i[0] + ", Age: " + i[1])
        text.grid(column=0, row=counter)