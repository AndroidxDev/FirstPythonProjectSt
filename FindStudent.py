from tkinter import *
import data

windowTk = None

def onChange(nameF, label: Label):
    for i in data.students:
        if nameF.get() == i[0]:
            label.configure(text="Name: " + i[0] + ", Age: " + i[1])
            break
        else:
            label.configure(text ="Not fing this student")

def FindStudent(root):
    global windowTk
    if  windowTk is not None and windowTk.winfo_exists():
        print("NONMOOOONONOO ITS NOT NEED FOR U BROO xd3")
        windowTk.lift()
    else: 
        windowTk = Toplevel(root)
        windowTk.title("find students")


    sv = StringVar()
    name = Entry(windowTk, textvariable=sv)
    name.grid(column=0, row=0)

    label = Label(windowTk, text="nothing")
    label.grid(column=0, row=1)

    sv.trace_add("write", lambda *args: onChange(sv, label))
