# ...............SPYCHAT Project................ #

# For not registered User #

from termcolor import colored

def no_reg():
    b=input(colored("Enter your name: ",'red'))
    d=input(colored("Enter your age: ",'blue'))
    while d.isnumeric() == False or int(d)<18 or int(d)>40:
        d=input(colored("Invalid age.\nEnter Valid age: ",'blue'))
    e=input(colored("Enter the password to enter in the SPYCHAT: ",'red'))
    while len(e)<8 or len(e)>18:
        e=input(colored("Invalid password length.\nEnter valid password length: ",'red'))
    f=input(colored("Enter your address: ",'green'))

# for registered user #

y1 = '123456'
def reg_user():
    b=input(colored("Enter your password: ",'blue'))
    while b != y1:
        b=input(colored("Enter Valid Password: ",'blue'))

def valid():
    a = input(colored("Are you an registered user on SPYCHAT?\nWrite y for YES and n for NO: ",'yellow'))
    if a == 'n':
        no_reg()

    elif a == 'y':
        reg_user()

    else:
        valid()
valid()
print("......You are welcome to the SPYCHAT......")

# tkinter window #

from stegano import lsb
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as mBox
import datetime
import re

root = Tk()
root.title("SPYCHAT")
root.geometry("400x400")
root.resizable(0,0)

tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)

tabcontrol.add(tab1 , text = "Encoding the image")
tabcontrol.add(tab2 , text = "Decoding the image")
tabcontrol.pack(expand = 1 , fill = "both")

                # for encoding #
def browse():
    filename = filedialog.askopenfilename()

    if re.search(r'\.png$', filename) or re.search(r'\.jpg$', filename):
        path_entry.config(text='Path to the file: ' + filename)
        path_entry.insert(0, filename)

    else:
        mBox.showinfo("Error","Your file is neither .jpg nor .png\nSo it cannot be choosen")


def image(path):
    print(path)

def clear(widget):
    widget.delete(0,END)

def hide_msg(path,message):
    hide = lsb.hide(path,message)
    message_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    hide.save('secret_pic'+message_time+'.jpg')
    mBox.showinfo("Saved","The image is saved with name secret_pic"+message_time+".jpg")

bbtn = Button(tab1,text = "Search Image",fg = 'powder blue',bg = 'black',width = 20,command = lambda: browse())
bbtn.place(relx = 0.25 , rely = 0.02)

path_entry = Entry(tab1, width = 40)
path_entry.place(relx = 0.15 , rely = 0.2)

reset = Button(tab1,text = "Clear",fg = 'powder blue',bg = 'black',command = lambda: clear(path_entry))
reset.place(relx = 0.0 , rely = 0.85)

sms = StringVar()
message = Label(tab1 , text = "Message",fg = 'powder blue',bg = 'black',font = ("",15)).place(relx = 0.35,rely = 0.35)
msg_entry = Entry(tab1 ,width = 40 ,textvariable = sms).place(relx = 0.15,rely = 0.45)

enc = Button(tab1,text = "Encode" ,fg = 'powder blue',bg = 'black',command = lambda: hide_msg(path_entry.get(),sms.get()))
enc.place(relx = 0.4,rely = 0.85)

upload_btn = Button(tab1 , text = "Upload",fg = 'powder blue',bg = 'black',command = lambda : image(path_entry.get()))
upload_btn.place(relx = 0.8 , rely = 0.85)

                # for decoding #

def browses():
    filename = filedialog.askopenfilename()
    if re.search(r'\.png$', filename) or re.search(r'\.jpg$', filename):
        path_entry2.config(text='Path to the file: ' + filename)
        path_entry2.insert(0, filename)

    else:
        mBox.showinfo("Error","Your file is neither .jpg nor .png\nSo it cannot be choosen")

def images(path):
    print(path)

def clears(widget):
    widget.delete(0,END)

def enco(path):
    print(path)
    sms = lsb.reveal(path)
    print(sms)

bbtn2 = Button(tab2,text = "Search Image",fg = 'powder blue',bg = 'black',width = 20,command = lambda: browses())
bbtn2.place(relx = 0.25 , rely = 0.02)

path_entry2 = Entry(tab2, width = 40)
path_entry2.place(relx = 0.15 , rely = 0.2)

reset2 = Button(tab2,text = "Reset",fg = 'powder blue',bg = 'black',command = lambda: clears(path_entry2),bd = 15)
reset2.place(relx = 0.4 , rely = 0.82)

def show_details():
    mBox.showinfo("Decoded","You are going to view the decoded message of the choosen image")
    toplevel = Toplevel(root)
    Label(toplevel,text = sms.get(),font = ("",15)).place(relx = 0.1,rely = 0.1)

msg = Button(tab2 , text = "View Message",fg = 'powder blue',bg = 'black', command = show_details).place(relx = 0.35,rely = 0.38)

root.mainloop()