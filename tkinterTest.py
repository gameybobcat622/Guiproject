from tkinter import  *

top = Tk()

def results():
    result = E1.get()
    print(result)
    print(type(result))

#this is a label widget
L1 = Label(top, text="Hello, world!")
L1.grid(column= 0, row= 1)

#this is a entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)


#This is a button widget
B1 = Button(text = "    Get Data    ", bg="red", command= results)
B1.grid(column= 0, row= 3)

top.mainloop()
