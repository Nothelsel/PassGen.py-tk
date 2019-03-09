#coding:utf-8
from tkinter import *
from tkinter.messagebox import *
from passgen import generate_password
import passgen

app = Tk()
#app.geometry("500x400+400+400")
app.resizable(width=False, height=False)
app.title("Apps Launcher")

#color_main = "#%02x%02x%02x" % (88, 98, 211)
color_menu = "#%02x%02x%02x" % (42, 62, 211)

#app.grid_rowconfigure(0, weight=6)
#app.grid_columnconfigure(0, weight=6)
#app.configure(bg=color_main)


def leave():
    if askyesno("Leave ?", "Are you sure to leave ?"):
        app.destroy()


def generation():
    nbr_pass = int(number_password.get())
    len_pass = int(password_len.get())
    generate_password(nbr_pass, len_pass)
    passwords_list = passgen.passwords
    for passwords in passwords_list:
        affiche_pass.insert(INSERT, '{}\n'.format(passwords))


def cleartext():
    affiche_pass.delete(1.0, END)


value_nbr = IntVar
value_len = IntVar
pass_all = StringVar

###### MENU BAR ######
menubar = Menu(app, tearoff=0)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label='New')
menu1.add_command(label='Edit')
menu1.add_separator()
menu1.add_command(label='Quit', command=app.quit())
menubar.add_cascade(label='File', menu=menu1)
app.config(menu=menubar)
########################

label_nbrPass = Label(app, text="Number Of Password :")
label_nbrPass.grid(column=1, row=1)
number_password = Entry(app, textvariable=value_nbr, width=30)


label_lenPass = Label(app, text="Length Of Password :")
label_lenPass.grid(column=1, row=3)
password_len = Entry(app, textvariable=value_len, width=30)


bouton_gen = Button(app, text="Generate", command=generation)


frame_pass = LabelFrame(app, text="Passwords :")
frame_pass.grid(column=1, row=6)


affiche_pass = Text(frame_pass, padx=10, pady=40, relief=GROOVE)
affiche_pass.grid(column=1, row=6)


#   /   END   \
bouton2 = Button(app, text="clear", command=cleartext)
bouton2.grid(column=1, row=100, sticky=SE)

bouton1 = Button(app, text="leave", command=leave)
bouton1.grid(column=2, row=100, sticky=SE)

number_password.grid(column=1, row=2)
password_len.grid(column=1, row=4)
bouton_gen.grid(column=1, row=5)

app.mainloop()
