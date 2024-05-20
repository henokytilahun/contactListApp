import tkinter
from tkinter import ttk
from datetime import date
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

def add_contact():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    relation = relation_combobox.get()
    dob = age_entry.get()
    fiscal = reg_status_var.get()
    moneyamount = moneyamount_spinbox.get()
    notes = notes_text.get("1.0", 'end-1c')

    fullname_added = firstname + " " + lastname  + " Added!"

    tkinter.messagebox.showinfo(title="Contact Status", message=fullname_added)

    conn = sqlite3.connect('contacts.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS Contacts 
            (firstname TEXT, lastname TEXT, relation TEXT, date_of_birth DATE,
            fiscal_status TEXT, ammount_owed TEXT, notes TEXT)
            '''
    conn.execute(table_create_query)

    data_insert_query = '''INSERT INTO Contacts (firstname, lastname, relation,
                        date_of_birth, fiscal_status, ammount_owed, notes) VALUES
                        (?,?,?,?,?,?,?)'''
    data_insert_tuple = (firstname, lastname, relation, dob, fiscal, moneyamount,
                         notes)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()

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

number_label = tkinter.Label(user_info_frame, text="Phone Number")
number_entry = tkinter.Entry(user_info_frame)
number_label.grid(row=2, column=1)
number_entry.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving money related Info
money_frame = tkinter.LabelFrame(frame)
money_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
fiscal_label = tkinter.Label(money_frame, text="Fiscal Status")

reg_status_var = tkinter.StringVar(value="Debt-free")
registered_check = tkinter.Checkbutton(money_frame, text="You owe Money",
                                        variable=reg_status_var, onvalue="Debt",
                                        offvalue= "Debt-free")

fiscal_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

moneyamount_label = tkinter.Label(money_frame, text="Amount owed in $")
moneyamount_spinbox = tkinter.Spinbox(money_frame, from_=0, to=5000000000)
moneyamount_label.grid(row=0, column=1)
moneyamount_spinbox.grid(row=1, column=1)

for widget in money_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

notes_frame = tkinter.LabelFrame(frame)
notes_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

notes_label = tkinter.Label(notes_frame, text="Notes")
notes_label.grid(row=0, column=1)
notes_text = tkinter.Text(notes_frame, bg= "light gray", selectborderwidth=100)
notes_text.grid(row=1, column=1)

for widget in notes_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = tkinter.Button(frame, text="Add Contact", command= add_contact)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)






window.mainloop()