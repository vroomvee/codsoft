from tkinter import *
import string                                                 
import random

def generator():
    passwordField.delete(0,END)
    sa=string.ascii_lowercase
    ca=string.ascii_uppercase
    ns=string.digits
    sc=string.punctuation

    all=sa+ca+ns+sc
    pl=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(sa+ca,pl))

    if choice.get()==2:
        passwordField.insert(0,random.sample(sa+ca+ns,pl))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,pl))
    if choice.get()==0:
        passwordField.insert(0,"Enter Strength")

root=Tk()
root.config(bg='deep pink')
root.title('Password Generator')
root.geometry('300x400')
choice=IntVar()
value=0
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='deep pink',fg='grey1')
passwordLabel.grid(pady=10)

passwordLabel=Label(root,text='Password Strength',font=Font,bg='deep pink',fg='grey1')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font,bg='hot pink',activebackground='deep pink')
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font,bg='hot pink',activebackground='deep pink')
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font,bg='hot pink',activebackground='deep pink')
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length',font=Font,bg='deep pink',fg='grey1')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator,bg='hot pink',activebackground='deep pink')
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=15)
root.mainloop()

