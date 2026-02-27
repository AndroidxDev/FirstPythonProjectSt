from tkinter import *
import data

windowTk = None

def delSt(str):
    for i in data.students:
        if str == i[0]:
            data.students.remove(i)
            print(data.students)
        else:
            error = Tk()
            label = Label(error, text ="faailed to delete")
            label.grid(column=0,row=0)

def DeleteStudent(root):
    global windowTk
    if  windowTk is not None and windowTk.winfo_exists():
        print("NONMOOOONONOO ITS NOT NEED FOR U BROO xd4")
        windowTk.lift()
    else: 
        windowTk = Toplevel(root)
        windowTk.title("find students")

    name = Entry(windowTk)
    name.grid(column=0, row=0)

    delbtn = Button(windowTk, text="delete", command=lambda: delSt(name.get()))
    delbtn.grid(column=0, row=1)

