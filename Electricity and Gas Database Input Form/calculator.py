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




def calculate():
        # Coresponding variable definitions and getting their data from data input form:
    date_year_var = date_year_combobox.get()
    date_month_var = date_month_combobox.get()
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


    table_name = "work1"
    condition_year = "entrydate_year"
    condition_month = "entrydate_month"


    current_month_query = f"SELECT gas FROM {table_name} WHERE {condition_year} = %s AND {condition_month} = %s"
    mycursor.execute(current_month_query, (date_year_var, date_month_integer))

    gas_counter_current = mycursor.fetchone()
    print(date_year_var, date_month_integer)
    print(gas_counter_current[0])

    if date_month_integer == 1:
        previous_date_month_integer = 12
        previous_date_year_var = int(date_year_var) - 1
    else:
        previous_date_month_integer = date_month_integer - 1
        previous_date_year_var = date_year_var
    
    
    previous_month_query = f"SELECT gas FROM {table_name} WHERE {condition_year} = %s AND {condition_month} = %s"
    mycursor.execute(previous_month_query, (previous_date_year_var, previous_date_month_integer))
    
    
    gas_counter_previous = mycursor.fetchone()
    print(previous_date_year_var, previous_date_month_integer)
    print(gas_counter_previous[0])
    potrosnja_gasa = gas_counter_current[0] - gas_counter_previous[0]

    print(f"Potrosnja gasa za mesec {date_month_var} je: {potrosnja_gasa} m3")

    


#    previous_month_query = f"SELECT {column_to_select} FROM {table_name} WHERE {condition_column1} = %s AND {condition_column2} = %s"
#    mycursor.execute(previous_month_query, (condition_value1, condition_value2))
#    previous_cell_data = mycursor.fetchone()













window = tkinter.Tk()
window.title("Electricity and Gas consumption Calculator")
frame = tkinter.Frame(window)
frame.pack()


# Main Title is Main title, first frame for form description and some style
main_title_frame = tkinter.LabelFrame(frame, text = "ELECTRICITY AND GAS CONSUMPTION CALCULATOR", labelanchor = "n", bd = 4, padx = 15, pady = 12)
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




button = tkinter.Button(frame, text = "Calculate", command = calculate)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)




window.mainloop()

"""
column_to_select = "gas"
table_name = "work1"
condition_column1 = "entrydate_year"
condition_value1 = "2023"
condition_column2 = "entrydate_month"
condition_value2 = "3"


if int(con)

prev_condition_column1 = "entrydate_year"
condition_value1 = "2023"
condition_column2 = "entrydate_month"
condition_value2 = "3"

current_month_query = f"SELECT {column_to_select} FROM {table_name} WHERE {condition_column1} = %s AND {condition_column2} = %s"
mycursor.execute(current_month_query, (condition_value1, condition_value2))
single_cell_data = mycursor.fetchone()
# print(single_cell_data[0])


previous_month_query = f"SELECT {column_to_select} FROM {table_name} WHERE {condition_column1} = %s AND {condition_column2} = %s"
mycursor.execute(previous_month_query, (condition_value1, condition_value2))
previous_cell_data = mycursor.fetchone()
"""






