import tkinter
from tkinter import ttk
from datetime import date

window = tkinter.Tk()
window.title("Contact List")

frame = tkinter.Frame(window)
frame.pack()

#Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)


first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

relation_label = tkinter.Label(user_info_frame, text="Relation")
relation_combobox = ttk.Combobox(user_info_frame, values=["Friend", "Family", "Partner", "Buisness", "Acquaintance"])
relation_label.grid(row=0, column=2)
relation_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Date of Birth (MM/DD/YYYY)")
age_entry = tkinter.Entry(user_info_frame)
age_label.grid(row=2, column=0)
age_entry.grid(row=3, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
registered_label = tkinter.Label(courses_frame, text="Fiscal Status")
registered_check = tkinter.Checkbutton(courses_frame, text="Owes You Money")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

moneyamount_label = tkinter.Label(courses_frame, text="Amount owed in $")
moneyamount_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=5000000000)
moneyamount_label.grid(row=0, column=1)
moneyamount_spinbox.grid(row=1, column=1)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

notes_frame = tkinter.LabelFrame(frame)
notes_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

notes_label = tkinter.Label(notes_frame, text="Notes")
notes_label.grid(row=0, column=1)
notes_text = tkinter.Text(notes_frame, bg= "light gray", selectborderwidth=100)
notes_text.grid(row=1, column=1)

for widget in notes_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
#figure out horoscope 

button = tkinter.Button(frame, text="Add Contact")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()