from tkinter import *
import data

windowTk = None

def writeStudent(nField: str, aField: str):
    localData = []

    if (nField != "" and aField != ""):
        localData.append(nField)
        localData.append(aField)

        data.students.append(localData)

        print(data.students)
        windowTk.destroy()

def AddStudent(root):
    global windowTk

    if  windowTk is not None and windowTk.winfo_exists():
        print("NONMOOOONONOO ITS NOT NEED FOR U BROO")
        windowTk.lift()
    else: 
        windowTk = Toplevel(root)
        windowTk.title("Add student")

    nameField = Entry(windowTk, textvariable="enter name..")
    nameField.grid(column=0, row=0)

    ageField = Entry(windowTk, textvariable="enter age..")
    ageField.grid(column=0, row=1)

    addBtn = Button(windowTk, text="Add student",command=lambda: writeStudent(nameField.get(), ageField.get()))
    addBtn.grid(column=0, row=2)



