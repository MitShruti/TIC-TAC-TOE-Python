from tkinter import*
from tkinter import messagebox

win=Tk()
win.maxsize(600,600)
win.minsize(600,600)
win.title("TIC TAC TOE")
win["bg"]="blue"

frame=Frame(win)
frame.pack()

def Reset():
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    t8.set("")
    t9.set("")


mylist=["X","O","X","O","X","O","X","O","X"]

var=IntVar()
var.set(0)
def game(textvariable):
  if(var.get()==0):
   textvariable.set("X")
   var.set(1)
  else:
    textvariable.set("O")
    var.set(0)

  if(t1.get()==t2.get()==t3.get()):
     if(t1.get()!=""):
      messagebox.showinfo("Message","You Win the game")
      Reset()
  elif(t1.get()==t4.get()==t7.get()):
      if(t1.get()!=""):
       messagebox.showinfo("Message","You Win the game")
       Reset()
  elif(t1.get()==t5.get()==t9.get()):
     if(t1.get()!=""):
      messagebox.showinfo("Message","You Win the game")
      Reset()
  
  elif(t2.get()==t5.get()==t8.get()):
    if(t2.get()!=""):
     messagebox.showinfo("Message","You Win the game")
     Reset()
  elif(t3.get()==t6.get()==t9.get()):
    if(t3.get()!=""):
     messagebox.showinfo("Message","You Win the game")
     Reset()
  elif(t3.get()==t5.get()==t7.get()):
    if(t3.get()!=""):
     messagebox.showinfo("Message","You Win the game")
     Reset()
  elif(t4.get()==t5.get()==t6.get()):
    if(t4.get()!=""):
     messagebox.showinfo("Message","You Win the game")
     Reset()
  elif(t7.get()==t8.get()==t9.get()):
    if(t7.get()!=""):
     messagebox.showinfo("Message","You Win the game")
     Reset()
  else:
    if(t1.get()!=""and t2.get()!=""and t3.get()!=""and t4.get()!="" and t5.get()!="" and t6.get()!=""and t7.get()!="" and t8.get()!="" and t9.get()!=""):
     messagebox.showinfo("Message","You Lose the game")
     Reset()
    
    
    


  

  






lb1=Label(win,text="TIC TAC TOE",font=("ALGERIAN",50),bg="blue",fg="white")
lb1.place(x=40,y=20,height=50,width=500)


t1=StringVar()


bt1=Button(win,font=("Algerian",40),textvariable=t1,command=lambda:game(t1))
bt1.place(x=120,y=120,height=100,width=100)


t2=StringVar()
bt2=Button(win,font=("Algerian",40),textvariable=t2,command=lambda:game(t2))
bt2.place(x=220,y=120,height=100,width=100)


t3=StringVar()
bt3=Button(win,font=("Algerian",40),textvariable=t3,command=lambda:game(t3))
bt3.place(x=320,y=120,height=100,width=100)

t4=StringVar()
bt4=Button(win,font=("Algerian",40),textvariable=t4,command=lambda:game(t4))
bt4.place(x=120,y=220,height=100,width=100)

t5=StringVar()
bt5=Button(win,font=("Algerian",40),textvariable=t5,command=lambda:game(t5))
bt5.place(x=220,y=220,height=100,width=100)

t6=StringVar()
bt6=Button(win,font=("Algerian",40),textvariable=t6,command=lambda:game(t6))
bt6.place(x=320,y=220,height=100,width=100)

t7=StringVar()
bt7=Button(win,font=("Algerian",40),textvariable=t7,command=lambda:game(t7))
bt7.place(x=120,y=320,height=100,width=100)

t8=StringVar()
bt8=Button(win,font=("Algerian",40),textvariable=t8,command=lambda:game(t8))
bt8.place(x=220,y=320,height=100,width=100)

t9=StringVar()
bt9=Button(win,font=("Algerian",40),textvariable=t9,command=lambda:game(t9))
bt9.place(x=320,y=320,height=100,width=100)

entv1=StringVar()
entv1.set("RESET")
btreset=Button(win,font=("Algerian",20),textvariable=entv1,command=Reset)
btreset.place(x=180,y=450,height=50,width=150)
win.mainloop()
