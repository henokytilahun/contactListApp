import tkinter as tk

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='Home Page\n\nPage:1', font=('Bold', 30))
    lb.pack()
    home_frame.pack(pady=20)

def add_page():
    add_frame = tk.Frame(main_frame)
    lb = tk.Label(add_frame, text='Add Page\n\nPage:2', font=('Bold', 30))
    lb.pack()
    add_frame.pack(pady=20)

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


root = tk.Tk()
root.geometry('500x400')
root.title('Pages Hub')


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
options_frame.configure(width=100,height=400)


main_frame = tk.Frame(root, highlightbackground='black',
                      highlightthickness=1)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=500,height=400)




root.mainloop()