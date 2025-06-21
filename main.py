from tkinter import *

def click(event):
    global input
    value = event.widget.cget("text")
    if value == "=":
        if input.get().isdigit():
            text = int(input.get())
        else:
            text = eval(input.get())
            
        input.set(text)
        entry.update()

    elif value == "Clear":
        input.set("")
        entry.update()
    else:
        input.set(input.get() + value)
        entry.update()

window = Tk()
window.geometry("510x700")
window.config(background="black")

input = StringVar()
input.set("")

entry = Entry(
    window,
    textvariable=input,
    font="Arial 40 bold",

)
entry.pack(fill=X,padx=10,pady=10,ipadx=8)  

frame = Frame(window,background="black")
frame.pack()

clear = Button(window,text="Clear",font="Arial 20 bold",padx=18,pady=12)
clear.pack(padx=18,pady=12)
clear.bind("<Button-1>", click)

btn7 = Button(frame,text="7",font="Arial 30 bold",padx=18,pady=12)
btn7.grid(row=0,column=0,padx=18,pady=12)
btn7.bind("<Button-1>", click)

btn8 = Button(frame,text="8",font="Arial 30 bold",padx=18,pady=12)
btn8.grid(row=0,column=1,padx=18,pady=12)
btn8.bind("<Button-1>", click)

btn9 = Button(frame,text="9",font="Arial 30 bold",padx=18,pady=12)
btn9.grid(row=0,column=2,padx=18,pady=12)
btn9.bind("<Button-1>", click)

plus = Button(frame,text="+",font="Arial 30 bold",padx=18,pady=12)
plus.grid(row=0,column=3,padx=18,pady=12)
plus.bind("<Button-1>", click)

btn4 = Button(frame,text="4",font="Arial 30 bold",padx=18,pady=12)
btn4.grid(row=1,column=0,padx=18,pady=12)
btn4.bind("<Button-1>", click)

btn5 = Button(frame,text="5",font="Arial 30 bold",padx=18,pady=12)
btn5.grid(row=1,column=1,padx=18,pady=12)
btn5.bind("<Button-1>", click)

btn6 = Button(frame,text="6",font="Arial 30 bold",padx=18,pady=12)
btn6.grid(row=1,column=2,padx=18,pady=12)
btn6.bind("<Button-1>", click)

minus = Button(frame,text="-",font="Arial 30 bold",padx=23,pady=12)
minus.grid(row=1,column=3,padx=18,pady=12)
minus.bind("<Button-1>", click)

btn1 = Button(frame,text="1",font="Arial 30 bold",padx=18,pady=12)
btn1.grid(row=2,column=0,padx=18,pady=12)
btn1.bind("<Button-1>", click)

btn2 = Button(frame,text="2",font="Arial 30 bold",padx=18,pady=12)
btn2.grid(row=2,column=1,padx=18,pady=12)
btn2.bind("<Button-1>", click)

btn3 = Button(frame,text="3",font="Arial 30 bold",padx=18,pady=12)
btn3.grid(row=2,column=2,padx=18,pady=12)
btn3.bind("<Button-1>", click)

multiply = Button(frame,text="*",font="Arial 30 bold",padx=21.2,pady=12)
multiply.grid(row=2,column=3,padx=18,pady=12)
multiply.bind("<Button-1>", click)

btn0 = Button(frame,text="0",font="Arial 30 bold",padx=18,pady=12)
btn0.grid(row=3,column=0,padx=18,pady=12)
btn0.bind("<Button-1>", click)

decimal = Button(frame,text=".",font="Arial 30 bold",padx=23,pady=12)
decimal.grid(row=3,column=1,padx=18,pady=12)
decimal.bind("<Button-1>", click)

divide = Button(frame,text="/",font="Arial 30 bold",padx=24,pady=12)
divide.grid(row=3,column=2,padx=18,pady=12)
divide.bind("<Button-1>", click)

equal = Button(frame,text="=",font="Arial 30 bold",padx=18,pady=12)
equal.grid(row=3,column=3,padx=18,pady=12)
equal.bind("<Button-1>", click)

window.mainloop()