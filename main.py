from tkinter import *
import AddStudent
import ShowAllStudents
import FindStudent
import DeleteStudent

window = Tk()
window.title("Students app")
#window.geometry("400x250")

def btnAddSt(): AddStudent.AddStudent(window)
def btnShowSt(): ShowAllStudents.ShowAllStudents(window)
def btnfindSt(): FindStudent.FindStudent(window)
def btnDelSt(): DeleteStudent.DeleteStudent(window)

addStudent = Button(window, text="Add student to db", command=btnAddSt)
addStudent.grid(column=0, row=0)

showAllstudents =  Button(window, text="Show all students", command=btnShowSt)
showAllstudents.grid(column=1, row=0)

findStudent = Button(window, text="Find student", command=btnfindSt)
findStudent.grid(column=2, row=0)

deleteStudent = Button(window, text="Delete student", command=btnDelSt)
deleteStudent.grid(column=3, row=0)

window.mainloop()