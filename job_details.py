from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import credentials as cr
import pymysql


con = pymysql.connect(
    host=cr.host, user=cr.user, password=cr.password, database=cr.database)
# cur = con.cursor()
c = con.cursor()

window = Tk()
window.title("Question Page")
window.geometry("1200x800")


def submit():
    Designation = dest.get()
    Salary = saly.get()
    Place = plac.get()

    if Designation == '' or Salary == '' or Place == '':
        messagebox.showwarning('Warning', 'Please fill the boxes')
        return
    else:
        mysql2 = 'INSERT INTO job_details(Designation,Salary,Place)VALUES(%s, %s, %s)'
        c.execute(mysql2, (Designation, Salary, Place))
        con.commit()
        messagebox.showinfo('Congrulation', 'Data stored successful')


bg = ImageTk.PhotoImage(file='images/photo1.jpeg')
img = Label(window, image=bg)
img.pack()

frame = Frame(window, width=350, height=400, bg='mistyrose',
              highlightthickness='3', highlightbackground='black')
frame.place(x=400, y=100)

heading = Label(frame, text="Add Job Details", font=(
    'times new roman', 16, 'bold', 'underline'), bg='mistyrose', fg='deep sky blue4')
heading.place(x=100, y=10)

des = Label(frame, text='Designation', font=(
    'times new roman', 14, 'bold'), bg='mistyrose', fg='black')
des.place(x=50, y=50)

dest = Entry(frame, bd=2, width=24, font=('times new roman', 12, 'bold'), bg='mistyrose',
             highlightcolor='black', highlightthickness='3')
dest.place(x=50, y=80)

salary = Label(frame, text='Salary', font=(
    'times new roman', 14, 'bold'), bg='mistyrose', fg='black')
salary.place(x=50, y=130)

saly = Entry(frame, bd=2, width=24, font=('times new roman', 12, 'bold'), bg='mistyrose',
             highlightcolor='black', highlightthickness='3')
saly.place(x=50, y=180)

place = Label(frame, text='Place', font=(
    'times new roman', 14, 'bold'), bg='mistyrose', fg='black')
place.place(x=50, y=230)

plac = Entry(frame, bd=2, width=24, font=('times new roman', 12, 'bold'), bg='mistyrose',
             highlightcolor='black', highlightthickness='3')
plac.place(x=50, y=280)

sub_Butt = Button(frame, text="Submit", font='Arial 10 bold',
                  bd=3, activebackground='maroon4', cursor='hand2', bg='dark slate gray', command=submit)
sub_Butt.place(x=150, y=330)


window.mainloop()
