import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox
import tkinter.messagebox
import sqlite3


def add_contact():
    firstname = add_page.first_name_entry.get()
    lastname = add_page.last_name_entry.get()
    relation = add_page.relation_combobox.get()
    dob = add_page.age_entry.get()
    phone = add_page.number_entry.get()
    fiscal = add_page.reg_status_var.get()
    moneyamount = add_page.moneyamount_spinbox.get()
    notes = add_page.notes_text.get("1.0", 'end-1c')

    fullname_added = firstname + " " + lastname  + " Added!"

    tkinter.messagebox.showinfo(title="Contact Status", message=fullname_added)

    conn = sqlite3.connect('contacts.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS Contacts 
            (firstname TEXT, lastname TEXT, relation TEXT, date_of_birth DATE,
            phone_number TEXT, fiscal_status TEXT, ammount_owed TEXT, notes TEXT)
            '''
    conn.execute(table_create_query)

    data_insert_query = '''INSERT INTO Contacts (
                        firstname,
                        lastname, 
                        relation,
                        date_of_birth, 
                        phone_number, 
                        fiscal_status, 
                        ammount_owed, 
                        notes) VALUES (?,?,?,?,?,?,?,?)'''
    data_insert_tuple = (firstname, lastname, relation, dob, phone, fiscal, moneyamount,
                         notes)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()

def fetch_contacts():
    conn = sqlite3.connect('Contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT firstname, lastname, fiscal_status, ammount_owed FROM Contacts')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def delete_contact(phone):
    conn = sqlite3.connect('Contacts.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Contacts WHERE phone = ?', (phone,))
    conn.commit()
    conn.close()

def update_contact(new_first, new_last, new_relation, new_dob,
                   new_fiscal, new_moneyammount, new_notes, phone):
    conn = sqlite3.connect('Contacts.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Contacts SET first = ?, last = ?, relation = ?, dob = ?, fiscal = ?, moneyamount = ? notes = ?", (new_first, new_last, new_relation, new_dob,
                   new_fiscal, new_moneyammount, new_notes, phone))
    conn.commit()
    conn.close()

def phone_exists(phone):
    conn = sqlite3.connect('Contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Contacts WHERE phone = ?', (phone,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0



#---------Pages-------------#
def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.pack(pady=20)
    contacts_label = tk.Label(home_frame, text='Contacts', font=('Bold', 30))
    contacts_label.pack()    
    tree = ttk.Treeview(home_frame, columns= ('First Name', 'Last Name', 'Owe Money', 'Amount'))
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('First Name', anchor=tk.CENTER, width=170)
    tree.column('Last Name', anchor=tk.CENTER, width=170)
    tree.column('Owe Money', anchor=tk.CENTER, width=170)
    tree.column('Amount', anchor=tk.CENTER, width=170)

    tree.heading('First Name', text='First Name')
    tree.heading('Last Name', text='Last Name')
    tree.heading('Owe Money', text='Owe Money')
    tree.heading('Amount', text='Amount ($)')

    def add_to_treeview():
        contacts = fetch_contacts()
        tree.delete(*tree.get_children())
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

    
    add_to_treeview()
    tree.pack()
    

    

def add_page():
    user_info_frame = tk.LabelFrame(main_frame, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    first_name_label = tk.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tk.Label(user_info_frame, text="Last Name")
    last_name_label.grid(row=0, column=1)


    add_page.first_name_entry = tk.Entry(user_info_frame)
    add_page.last_name_entry = tk.Entry(user_info_frame)
    add_page.first_name_entry.grid(row=1, column=0)
    add_page.last_name_entry.grid(row=1, column=1)

    relation_label = tk.Label(user_info_frame, text="Relation")
    add_page.relation_combobox = ttk.Combobox(user_info_frame, values=["Friend", "Family", "Partner", "Buisness", "Acquaintance"])
    relation_label.grid(row=0, column=2)
    add_page.relation_combobox.grid(row=1, column=2)

    age_label = tk.Label(user_info_frame, text="Date of Birth (MM/DD/YYYY)")
    add_page.age_entry = tk.Entry(user_info_frame)
    age_label.grid(row=2, column=0)
    add_page.age_entry.grid(row=3, column=0)

    number_label = tk.Label(user_info_frame, text="Phone Number")
    add_page.number_entry = tk.Entry(user_info_frame)
    number_label.grid(row=2, column=1)
    add_page.number_entry.grid(row=3, column=1)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #saving money related Info
    money_frame = tk.LabelFrame(main_frame)
    money_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
    fiscal_label = tk.Label(money_frame, text="Fiscal Status")

    add_page.reg_status_var = tk.StringVar(value="Debt-free")
    registered_check = tk.Checkbutton(money_frame, text="You owe Money",
                                        variable=add_page.reg_status_var, onvalue="Debt",
                                        offvalue= "Debt-free")

    fiscal_label.grid(row=0, column=0)
    registered_check.grid(row=1, column=0)

    moneyamount_label = tk.Label(money_frame, text="Amount owed in $")
    add_page.moneyamount_spinbox = tk.Spinbox(money_frame, from_=0, to=5000000000)
    moneyamount_label.grid(row=0, column=1)
    add_page.moneyamount_spinbox.grid(row=1, column=1)

    for widget in money_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    notes_frame = tk.LabelFrame(main_frame)
    notes_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    notes_label = tk.Label(notes_frame, text="Notes")
    notes_label.grid(row=0, column=1)
    add_page.notes_text = tk.Text(notes_frame, bg= "light gray", selectborderwidth=100)
    add_page.notes_text.grid(row=1, column=1)

    for widget in notes_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = tk.Button(main_frame, text="Add Contact", command= add_contact)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

def update_page():
    update_frame = tk.Frame(main_frame)
    lb = tk.Label(update_frame, text='Update Page\n\nPage:3', font=('Bold', 30))
    lb.pack()
    update_frame.pack(pady=20)

def delete_page():
    delete_frame = tk.Frame(main_frame)
    lb = tk.Label(delete_frame, text='Delete Page\n\nPage:4', font=('Bold', 30))
    lb.pack()
    delete_frame.pack(pady=20)

def exit_page():
    exit_frame = tk.Frame(main_frame)
    lb = tk.Label(exit_frame, text='Exit Page\n\nPage:5', font=('Bold', 30))
    lb.pack()
    exit_frame.pack(pady=20)
#---------Pages-------------#

#---------Pages-------------#
def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    add_indicate.config(bg='#c3c3c3')
    update_indicate.config(bg='#c3c3c3')
    delete_indicate.config(bg='#c3c3c3')
    exit_indicate.config(bg='#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()



#---------Pages-------------#

root = tk.Tk()
root.geometry('800x715')
root.title('Pages Hub')
#----------------------------------------------------------



#-----------------------------------------------------------
options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn = tk.Button(options_frame, text='  Home ', font=('Bold', 15),
                     fg='#158aff', bd=0, command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=50)
home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3,y=50, width=5,height=25)


add_btn = tk.Button(options_frame, text='   Add   ', font=('Bold', 15),
                     fg='#158aff', bd=0, command=lambda: indicate(add_indicate, add_page))
add_btn.place(x=10, y=100)
add_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
add_indicate.place(x=3,y=100, width=5,height=25)


update_btn = tk.Button(options_frame, text='Update', font=('Bold', 15),
                     fg='#158aff', bd=0, command=lambda: indicate(update_indicate, update_page))
update_btn.place(x=10, y=150)
update_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
update_indicate.place(x=3,y=150, width=5,height=25)


delete_btn = tk.Button(options_frame, text=' Delete ', font=('Bold', 15),
                     fg='#158aff', bd=0, command=lambda: indicate(delete_indicate, delete_page))
delete_btn.place(x=10, y=200)
delete_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
delete_indicate.place(x=3,y=200, width=5,height=25)


exit_btn = tk.Button(options_frame, text='    Exit   ', font=('Bold', 15),
                     fg='#158aff', bd=0, command=lambda: indicate(exit_indicate, exit_page))
exit_btn.place(x=10, y=250)
exit_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
exit_indicate.place(x=3,y=250, width=5,height=25)






options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100,height=900)


main_frame = tk.Frame(root, highlightbackground='black',
                      highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=800,height=900)




root.mainloop()