from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="registerdb")
cursordb = connectiondb.cursor()


def login():
    global root3
    root3 = Toplevel(root)
    root3.title("Account Login")
    root3.geometry("450x300")
    root3.config(bg="white")
    global user_verification
    global pass_verification
   # global registeration

    Label(root3, text='Please Enter your Account Details', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white",
          bg="green", width=300).pack()
    user_verification = StringVar()
    pass_verification = StringVar()
    Label(root3, text="").pack()
    Label(root3, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root3, textvariable=user_verification).pack()
    Label(root3, text="").pack()
    Label(root3, text="Password:", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root3, textvariable=pass_verification, show="*").pack()
    Label(root3, text="").pack()

    Button(root3, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=login_verification).pack()
    Label(root3, text="")

def logged_destroy():
    logged_message.destroy()
    root3.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root3)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome  to HIDS{} ".format(user_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def login_verification():
    username_verification = user_verification.get()
    password_verification = pass_verification.get()
    sql = "select * from 'registerdb' where 'user'='%s' and 'pass'='%s'"
    cursordb_execute(sql, [(username_verification), (password_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    Label(root, text='Welcome to HIDS  Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
          bg="blue", width=300).pack()
    Label(root, text="").pack()
    Button(root, text='Log In', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=login).pack()
    Label(root, text="").pack()
    Button(root, text='SIGNUP', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
              bg="blue").pack()
    Label(root, text="").pack()
    Button(root, text='EXIT', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=Exit).pack()
    Label(root, text="").pack()


main_display()
root.mainloop()


