from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import pymysql
import credentials as cr

con = pymysql.connect(
    host=cr.host, user=cr.user, password=cr.password, database=cr.database)
# cur = con.cursor()
c = con.cursor()

window = Tk()

window.title("Sign Up")
window.geometry("1350x800+0+0")
window.iconbitmap("images/resgister.ico")


def signup():
    Firstname = firstname_Entry.get()
    Lastname = lastname_Entry.get()
    Email_Id = email_Entry.get()
    Password = password_Entry.get()
    Address = address_Entry.get()
    Contact = contact_Entry.get()
    City = city_Entry.get()

    if Firstname == '' or Lastname == '' or Email_Id == '' or Password == '' or Address == '' or Contact == '' or City == '':
        messagebox.showerror("Error", "Fill up all the boxes")
        return
    elif term.get() == 0:
        messagebox.showerror(
            "Error!", "Please Agree with our Terms & Conditions")
        return
    else:
        try:
            Email_Id == email_Entry.get()
            mysql = "SELECT * FROM register_details WHERE Email= %s"
            c.execute(mysql, (Email_Id))
            # c.commit()
            row = c.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error!", "The email id is already exists, please try again with another email id")
                return
            else:
                mysql = "INSERT INTO register_details(Firstname,Lastname,Email,Password,Address,Contact,City) VALUES( %s, %s, %s, %s, %s, %s, %s)"
                c.execute(mysql, (Firstname, Lastname, Email_Id,
                          Password, Address, Contact, City))
                con.commit()
                c.close()
                messagebox.showinfo("Congratulations!", "Register Successful")
                reset_field()
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")


def reset_field():
    firstname_Entry.delete(0, END)
    lastname_Entry.delete(0, END)
    email_Entry.delete(0, END)
    password_Entry.delete(0, END)
    address_Entry.delete(0, END)
    city_Entry.delete(0, END)
    contact_Entry.delete(0, END)

    window.destroy()
    import login


bg_image = ImageTk.PhotoImage(file="images/background.jpg")
image_back = Label(window, image=bg_image).pack()

frame = Frame(window, bg="misty rose")
frame.place(x=500, y=100, width=450, height=500)

heading = Label(frame, text="Sign Up", font=(
    'Times new roman', 20, 'bold'), bg='misty rose')
heading.place(x=150, y=10)

firstname = Label(frame, text='Firstname', font=(
    'times new roman', 16, 'bold'), bg='misty rose')
firstname.place(x=10, y=70)

firstname_Entry = Entry(frame, bd=3, width=20,
                        font=('times new roman', 12, 'bold'))
firstname_Entry.place(x=130, y=73)

lastname = Label(frame, text='Lastname', font=(
    'times new roman', 16, 'bold'), bg='misty rose')
lastname.place(x=10, y=120)

lastname_Entry = Entry(frame, bd=3, width=20,
                       font=('times new roman', 12, 'bold'))
lastname_Entry.place(x=130, y=123)

email = Label(frame, text='Email-Id',
              font=('times new roman', 16, 'bold'), bg='misty rose')
email.place(x=10, y=170)

email_Entry = Entry(frame, bd=3, width=22, font=(
    'times new roman', 12, 'bold'))
email_Entry.place(x=130, y=173)

password = Label(frame, text='Password', font=(
    'times new roman', 16, 'bold'), bg='misty rose')
password.place(x=10, y=220)

password_Entry = Entry(frame, show='*', bd=3, width=20,
                       font=('times new roman', 12, 'bold'))
password_Entry.place(x=130, y=223)

address = Label(frame, text='Address', font=(
    'times new roman', 16, 'bold'), bg='misty rose')
address.place(x=10, y=270)

address_Entry = Entry(frame, bd=3, width=20,
                      font=('times new roman', 12, 'bold'))
address_Entry.place(x=130, y=273)

contact = Label(frame, text='Contact No.', font=(
    'times new roman', 16, 'bold'), bg='misty rose')
contact.place(x=10, y=320)

contact_Entry = Entry(frame, bd=3, width=20,
                      font=('times new roman', 12, 'bold'))
contact_Entry.place(x=130, y=323)

city = Label(frame, text='City', font=(
    'times new roman', 16, 'bold'), bg='misty rose')
city.place(x=10, y=370)

city_Entry = Entry(frame, bd=3, width=20, font=('times new roman', 12, 'bold'))
city_Entry.place(x=130, y=373)


term = IntVar()
term_and_con = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=term,
                           onvalue=1, offvalue=0, bg="misty rose", font=("times new roman", 12))
term_and_con.place(x=10, y=420)

sign_Butt = Button(frame, text="Sign Up", font='Arial 10 bold', bd=3,
                   activebackground='maroon4', cursor='hand2', bg='dark slate gray', command=signup)
sign_Butt.place(x=220, y=470)


window.mainloop()
