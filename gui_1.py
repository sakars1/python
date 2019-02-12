from tkinter import *

win = Tk()
win.resizable(0,0)
# win.geometry("500x500")
# title = (win,text="Calculator", font=("",20))
# title.grid(row=0,column=0)

scr = ""
def pass_val(p_val):

    global scr
    scr += str(p_val)
    str_var.set(scr)

def clr_val():

    global scr
    scr = ""
    str_var.set(scr)

def res():
    re = eval(scr)
    str_var.set(re)

str_var = StringVar()

screen = Entry(win, text="", borderwidth=2, relief="solid", font=("", 16), textvariable=str_var)
screen.grid(rowspan=3,columnspan=4,pady=10)
btn1 = Button(win, text="1", width=5,font=("",15), command=lambda:pass_val(1))
btn1.grid(row=4,column=0)
btn2 = Button(win, text="2", width=5,font=("",15), command=lambda:pass_val(2))
btn2.grid(row=4,column=1)
btn3 = Button(win, text="3", width=5,font=("",15), command=lambda:pass_val(3))
btn3.grid(row=4,column=2)

btn4 = Button(win, text="4", width=5,font=("",15), command=lambda:pass_val(4))
btn4.grid(row=5,column=0)
btn5 = Button(win, text="5", width=5,font=("",15), command=lambda:pass_val(5))
btn5.grid(row=5,column=1)
btn6 = Button(win, text="6", width=5,font=("",15), command=lambda:pass_val(6))
btn6.grid(row=5,column=2)

btn7 = Button(win, text="7", width=5,font=("",15), command=lambda:pass_val(7))
btn7.grid(row=6,column=0)
btn8 = Button(win, text="8", width=5,font=("",15), command=lambda:pass_val(8))
btn8.grid(row=6,column=1)
btn9 = Button(win, text="9", width=5,font=("",15), command=lambda:pass_val(9))
btn9.grid(row=6,column=2)

pls = Button(win, text="+", width=5,font=("",15), command=lambda:pass_val("+"))
pls.grid(row=7,column=0)
btn0 = Button(win, text="0", width=5,font=("",15), command=lambda:pass_val(0))
btn0.grid(row=7,column=1)
clr = Button(win, text="CLR", width=5,font=("",15), background="red", command=lambda:clr_val())
clr.grid(row=6,column=3)
mns = Button(win, text="-", width=5,font=("",15), command=lambda:pass_val("-"))
mns.grid(row=7,column=2)
eql = Button(win, text="=", width=5,font=("",15), command=lambda:res())
eql.grid(row=7,column=3)
# Label(win,text="Enter First Number").pack()
u_name = StringVar()
u_age = StringVar()
name=Entry(win,textvariable=u_name)
# name.pack(padx=(10),pady=(10))
# Label(win,text="Enter Second Number").pack()
age=Entry(win,textvariable=u_age)
# age.pack(padx=(10),pady=(10))
out=Label(win,text=" ")
# out.pack()

def btn_click():
    sum = int(u_name.get()) + int(u_age.get())
    out.config(text="the sum is: "+ str(sum), font=("helvetica",15))
sub=Button(win,text="submit",command=btn_click)
# sub.pack(padx=(10),pady=(10))
win.mainloop()