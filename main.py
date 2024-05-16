import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Contact List")

frame = tkinter.Frame(window)
frame.pack()

#Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="first Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)


first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

relation_label = tkinter.Label(user_info_frame, text="Relation")
relation_combobox = ttk.Combobox(user_info_frame, values=["Friend", "Family", "Buisness", "Acquaintance"])
relation_label.grid(row=0, column=2)
relation_combobox.grid(row=1, column=2)

window.mainloop()