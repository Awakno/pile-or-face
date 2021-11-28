from  tkinter import *
import random

app  =  Tk()
def pile_ou_face():
    list = ['pile','face']
    piece = random.choice(list)
    entry.delete(0,END)
    entry.insert(0,(piece))
app.geometry('300x300')
app.config(bg='green')


entry = Entry(bg='white',width=20)
entry.pack()
button = Button(app,bg='red',width=20,text='LANCEZZ!!!!!!',command=pile_ou_face)
button.pack(expand=YES)
app.mainloop()
