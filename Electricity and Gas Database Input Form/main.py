# IMPORTS
# tkinter is import for making GUI form
# mysql.connector is import for connecting to database
# time is import for time
# datetime is import for date and time

import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time
from datetime import datetime

# Using database "test_1"
# Using table with name "work1" with coresponding data:
                                                        # "gas" - for Gas counter, integer
                                                        # "ht" - for High Tarrif EL. counter, integer
                                                        # "lt" - for Low Tarrif EL. counter, integer
                                                        # "entrydate" - for entrydate string in format year_month)
                                                        # "entrydate_month" - integer
                                                        # "entrydate_year" - integer
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "test_1"
)


now = datetime.now()
mycursor = db.cursor()


def enter_data():
    approved = areyousure_var.get()
    print(approved)
    if approved == "Sure":
        # Coresponding variable definitions and getting their data from data input form:
        date_year_var = date_year_combobox.get()
        date_month_var = date_month_combobox.get()
        high_tarrif_var = consumption_ht_frame_entry.get()
        low_tarrif_var = consumption_lt_frame_entry.get()
        gas_var = consumption_gas_frame_entry.get()
        date_year_month_string = date_year_var + "_" + date_month_var
        
        if date_month_var == "January":
            date_month_integer = 1
        if date_month_var == "February":
            date_month_integer = 2
        if date_month_var == "March":
            date_month_integer = 3
        if date_month_var == "April":
            date_month_integer = 4
        if date_month_var == "May":
            date_month_integer = 5
        if date_month_var == "June":
            date_month_integer = 6
        if date_month_var == "July":
            date_month_integer = 7
        if date_month_var == "August":
            date_month_integer = 8
        if date_month_var == "September":
            date_month_integer = 9
        if date_month_var == "October":
            date_month_integer = 10
        if date_month_var == "November":
            date_month_integer = 11
        if date_month_var == "December":
            date_month_integer = 12


        # Query if "entry" already exists in database
        query = f"SELECT entrydate FROM work1 WHERE entrydate = '{date_year_month_string}'"
        mycursor.execute(query)
        result_fetch = mycursor.fetchall()
        
        # Updating or enetering new query into database
        if any(date_year_month_string in item for item in result_fetch):
            print(f"Entry za {date_year_month_string} vec postoji.")

            update_db = "UPDATE work1 SET gas = %s, ht = %s, lt = %s, entrydate = %s, entrydate_year = %s, entrydate_month = %s WHERE entrydate = %s"
            data_to_update = (gas_var, high_tarrif_var, low_tarrif_var, date_year_month_string, date_year_var, date_month_integer, date_year_month_string)
            mycursor.execute(update_db, data_to_update)
            db.commit()
        else:
            enter_db = "INSERT INTO work1 (gas, ht, lt, entrydate, entrydate_year, entrydate_month) VALUES (%s, %s, %s, %s, %s, %s)"
            data_to_enter = (gas_var, high_tarrif_var, low_tarrif_var, date_year_month_string, date_year_var, date_month_integer)
            mycursor.execute(enter_db, data_to_enter)
            db.commit()


        print("_________________________________")
        print(f"Electricity and Gas counters for date: {date_month_var} / {date_year_var}")
        print(f"Electricity High Tarrif counter status: {high_tarrif_var}")
        print(f"Electricity Low Tarrif counter status: {low_tarrif_var}")
        print(f"Gas counter status: {gas_var}")
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "You must approve entering data")


    
    
window = tkinter.Tk()
window.title("Electricity and Gas Database Input Form")
frame = tkinter.Frame(window)
frame.pack()


# Main Title is Main title, first frame for form description and some style
main_title_frame = tkinter.LabelFrame(frame, text = "ELECTRICITY AND GAS DATABASE INPUT FORM", labelanchor = "n", bd = 4, padx = 15, pady = 12)
main_title_frame.grid(row = 0, column = 0)


date_monthday_label = tkinter.Label(main_title_frame, text = "Choose Year and Month:")
date_monthday_label.grid(row = 1, column = 0, sticky = "ew", padx = 15, pady = 12)


date_month_label = tkinter.Label(main_title_frame, text = "Month:")
date_month_label.grid(row = 3, column = 0)
date_month_combobox = ttk.Combobox(main_title_frame, values = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
date_month_combobox.grid(row = 4, column = 0)



date_year_label = tkinter.Label(main_title_frame, text = "Year:")
date_year_label.grid(row = 3, column = 1)
date_year_combobox = ttk.Combobox(main_title_frame, values = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028])
date_year_combobox.grid(row = 4, column = 1)




# Consumption frames, and data are for consumption style input, and calculations
consumption_frame = tkinter.LabelFrame(frame, text = "Enter Counter Statuses for Electricity and Gas", labelanchor = "n")
consumption_frame.grid(row = 1, column = 0, padx = 15, pady = 12)


consumption_ht_frame_label = tkinter.Label(consumption_frame, text = "High Tariff")
consumption_ht_frame_label.grid(row = 0, column = 0)
consumption_lt_frame_label = tkinter.Label(consumption_frame, text = "Low Tariff")
consumption_lt_frame_label.grid(row = 0, column = 1)
consumption_gas_frame_label = tkinter.Label(consumption_frame, text = "Gas")
consumption_gas_frame_label.grid(row = 0, column = 2)


consumption_ht_frame_entry = tkinter.Entry(consumption_frame)
consumption_ht_frame_entry.grid(row = 1, column = 0)
consumption_lt_frame_entry = tkinter.Entry(consumption_frame)
consumption_lt_frame_entry.grid(row = 1, column = 1)
consumption_gas_frame_entry = tkinter.Entry(consumption_frame)
consumption_gas_frame_entry.grid(row = 1, column = 2)


for widget in consumption_frame.winfo_children():
    widget.grid_configure(padx = 15, pady = 12)


# Accept Terms
areyousure_var = tkinter.StringVar(value = "Not Sure")
terms_frame = tkinter.LabelFrame(frame, text = "Approval")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)
terms_check = tkinter.Checkbutton(terms_frame, text = "I am sure to enter new data to database.", variable = areyousure_var, onvalue = "Sure", offvalue = "Not Sure")
terms_check.grid(row = 0, column = 0)



button = tkinter.Button(frame, text = "Enter data", command = enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)




window.mainloop()