from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Calculator")
#root.iconbitmap("C:\\Users\\eshwar\\GUI projects\\calcicon.ico")
bframe1=Frame(root)
text_frame1=Frame(root)
text_frame1.pack()
l=Label(text_frame1,text="result",style='W.TButton',background="red",foreground="black")
bframe1.pack()
style=Style()
style.configure('W.TButton',font=('sans-serif',20,'bold',),fg='black',bg="pink")
style.map('W.TButton', foreground = [('active', '!disabled', 'black')],
                     background = [('active', 'black')])

t=Text(text_frame1,font=("sans-serif",20),width=47,height=3,background="lightseagreen",foreground="black")
t.pack()
l.pack(side=RIGHT)
def one():
    t.insert(END,"1")
def two():
    t.insert(END,"2")
def three():
    t.insert(END,"3")
def four():
    t.insert(END,"4")
def five():
    t.insert(END,"5")
def six():
    t.insert(END,"6")
def seven():
    t.insert(END,"7")
def eight():
    t.insert(END,"8")
def nine():
    t.insert(END,"9")
def zero():
    t.insert(END,"0")


def add():
    t.insert(END,"+")
def min():
    t.insert(END,"-")
def div():
    t.insert(END,"/")
def mod():
    t.insert(END,"%")

def mul():
    if(t.get(END)!='+'):
        t.insert(END,'*')
            
def show():
    output=t.get(0.0,"end-1c")
    res=eval(output)
    #t.insert(0.0,res)
    l.config(text=res)  
def clear():
    t.delete(0.0,END)
def delete():
    t.delete("end-2c")
        
              
one=Button(bframe1,text="1",style='W.TButton',command=one)
two=Button(bframe1,text="2",style='W.TButton',command=two)
three=Button(bframe1,text="3",style='W.TButton',command=three)
four=Button(bframe1,text="4",style='W.TButton',command=four)
five=Button(bframe1,text="5",style='W.TButton',command=five)
six=Button(bframe1,text="6",style='W.TButton',command=six)
seven=Button(bframe1,text="7",style='W.TButton',command=seven)
eight=Button(bframe1,text="8",style='W.TButton',command=eight)
nine=Button(bframe1,text="9",style='W.TButton',command=nine)
zero=Button(bframe1,text="0",style='W.TButton',command=zero)
plus=Button(bframe1,text="+",style='W.TButton',command=add)
minus=Button(bframe1,text="-",style='W.TButton',command=min)
division=Button(bframe1,text="/",style='W.TButton',command=div)
multiplication=Button(bframe1,text="*",style='W.TButton',command=mul)
modulus=Button(bframe1,text="%",style='W.TButton',command=mod)
show1=Button(bframe1,text="=",style='W.TButton',command=show)
clearbutton=Button(bframe1,text="clear",style='W.TButton',command=clear)
deleteButton=Button(bframe1,text="Delete",style='W.TButton',command=delete)


one.grid(row=0,column=1)
two.grid(row=0,column=2)
three.grid(row=0,column=3)
four.grid(row=1,column=1)
five.grid(row=1,column=2)
six.grid(row=1,column=3)
seven.grid(row=2,column=1)
eight.grid(row=2,column=2)
nine.grid(row=2,column=3)
zero.grid(row=3,column=2)
plus.grid(row=0,column=4)
minus.grid(row=1,column=4)
division.grid(row=2,column=4)
multiplication.grid(row=3,column=3)
modulus.grid(row=3,column=1)
show1.grid(row=3,column=4)
clearbutton.grid(row=4,column=4)
deleteButton.grid(row=4,column=3)






root.mainloop()
