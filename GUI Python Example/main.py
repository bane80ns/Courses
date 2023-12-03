import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time
from datetime import datetime


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "test_1"
)

now = datetime.now()
mycursor = db.cursor()

def enter_data():
    accepted = accept_var.get()
    if accepted == "Accepted" :
        
        #User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()


            #Courses Info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print(f"Title: {title}, First name: {firstname}, Last name: {lastname}")
            print(f"Age: {age}, Nationality: {nationality}")
            print(f"# Courses: {numcourses}, # Semesters : {numsemesters}")
            print(f"Registration status: ", registration_status)
            print("----------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title = "Error", message = "You must enter First and Last Name")
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "You have not accepted the Terms and Conditions Agreement")



window = tkinter.Tk()
window.title("Data Entry Form")


frame = tkinter.Frame(window)
frame.pack()


# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)


first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row = 0, column = 0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid(row = 0, column = 1)


first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row = 1, column = 1)


title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["Mr.", "Ms.", ""])
title_label.grid(row = 0, column = 2)
title_combobox.grid(row = 1, column = 2)


age_label = tkinter.Label(user_info_frame, text = "Age")
age_label.grid(row = 2, column = 0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_ = 18, to = 105)
age_spinbox.grid(row = 3, column = 0)


nationality_label = tkinter.Label(user_info_frame, text = "Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Slovakian", "Serbian", "Hungarian", "Trinidad & Tobago", "Nigerian", "Italian", "Other"])
nationality_label.grid(row = 2, column = 2)
nationality_combobox.grid(row = 3, column = 2)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 12, pady = 7)


# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)


registered_label = tkinter.Label(courses_frame, text = "Registration Status")

reg_status_var = tkinter.StringVar(value = "Not Registered")
register_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered", variable = reg_status_var, onvalue = "Registered", offvalue = "Not Registered")
registered_label.grid(row = 0, column = 0)
register_check.grid(row = 1, column = 0)


numcourses_label = tkinter.Label(courses_frame, text = "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row = 1, column = 1)


numsemesters_label = tkinter.Label(courses_frame, text = "# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numsemesters_label.grid(row = 0, column = 2)
numsemesters_spinbox.grid(row = 1, column = 2)


for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 12, pady = 7)


# Accept Terms
accept_var = tkinter.StringVar(value = "Not Accepted")
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept the terms and conditions.", variable = accept_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0, column = 0)

button = tkinter.Button(frame, text = "Enter data", command = enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)





window.mainloop()
