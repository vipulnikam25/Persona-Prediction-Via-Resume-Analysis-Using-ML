from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import credentials as cr
from tkinter import messagebox
import pymysql
import tkinter.font as font


con = pymysql.connect(
    host=cr.host, user=cr.user, password=cr.password, database=cr.database)
# cur = con.cursor()
c = con.cursor()

window = Tk()
window.title("Login Page")
window.geometry("1250x800+0+0")
window.iconbitmap('images/login.ico')


def login():
    Email_Id = user_entry.get()
    Password = password_entry.get()

    if Email_Id == "" or Password == "":
        messagebox.showwarning("Warning!", "Please fill up all the box")
        return
    if Email_Id == "admin" or Password == "admin":
        window.destroy()
        import admin

    else:

        mysql = "SELECT * FROM register_details WHERE Email= %s and Password= %s"
        c.execute(mysql, (Email_Id, Password))
        row = c.fetchall()
        con.commit()

        if row == None:
            messagebox.showerror("Error!", "Invalid Email_Id & Password")
            return
        else:
            messagebox.showinfo("Success", "Welcome to Login Page")
            from main import train_model


def forgot():
    Email_Id = user_entry.get()
    if Email_Id == "":
        messagebox.showerror("Error!", "Please enter your Email Id")
        return
    else:
        mysql = "SELECT * FROM register_details WHERE Email_Id= '%s' "
        c.execute(mysql, (Email_Id))
        con.close()
        import admin


def create_account():
    window.destroy()
    import register


# =======Background Image============#
bg = ImageTk.PhotoImage(file='images/photo1.jpeg')
img = Label(window, image=bg)
img.pack()

frame = Frame(window, width=300, height=400, bg='mistyrose',
              highlightthickness='3', highlightbackground='black')
frame.place(x=500, y=100)

bg1 = ImageTk.PhotoImage(file='images/login_image.jpg')
img1 = Label(frame, image=bg1)
img1.place(x=100, y=10)

heading = Label(frame, text="Login", font=('times new roman',
                18, 'bold'), bg='mistyrose', fg='deep sky blue4')
heading.place(x=120, y=100)

user = Label(frame, text="Username", font=(
    'times new roman', 16, 'bold'), bg='mistyrose', fg='cyan3')
user.place(x=100, y=140)

user_entry = Entry(frame, bd=2, width=30, font=(
    'times new roman', 12, 'bold'), fg="gray")
user_entry.place(x=28, y=170)

password = Label(frame, text="Password", font=(
    'times new roman', 16, 'bold'), bg='mistyrose', fg='cyan3')
password.place(x=100, y=200)

password_entry = Entry(frame, bd=2, width=30, font=(
    'times new roman', 12, 'bold'), fg="gray")
password_entry.place(x=28, y=230)

# forgot_pass = Button(frame, text="Forgotton Password", font=("times new roman", 12, "bold"), bd=0,
#                      cursor="hand2", bg="mistyrose", fg="indian red", activebackground='mistyrose',
#                      activeforeground='indian red', command=forgot)
# forgot_pass.place(x=90, y=260)

button = Button(frame, text='Login', font=('times new roman', 12, 'bold'), fg='black', activebackground='maroon',
                bg='springgreen3', activeforeground='yellow', cursor="hand2", command=login)
button.place(x=120, y=300)

createButton = Button(frame, text='Create New Account', font=('times new roman', 10, 'bold'), fg='black', activebackground='maroon',
                      bg='springgreen3', activeforeground='yellow', cursor="hand2", command=create_account)
createButton.place(x=80, y=340)


window.mainloop()
