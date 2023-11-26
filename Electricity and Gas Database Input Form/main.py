import tkinter
from tkinter import ttk
from tkinter import messagebox




def enter_data():
    approved = areyousure_var.get()
    print(approved)
    if approved == "Sure":
        
        date_year_var = date_year_combobox.get()
        date_month_var = date_month_combobox.get()
        high_tarrif_var = consumption_ht_frame_entry.get()
        low_tarrif_var = consumption_lt_frame_entry.get()
        gas_var = consumption_gas_frame_entry.get()

        print("_________________________________")
        print(f"Consumption for {date_month_var} / {date_year_var}")
        print(f"Electricity High Tarrif: {high_tarrif_var} kwh")
        print(f"Electricity Low Tarrif: {low_tarrif_var} kwh")
        print(f"Gas {gas_var} m3")
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


date_year_label = tkinter.Label(main_title_frame, text = "Day:")
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