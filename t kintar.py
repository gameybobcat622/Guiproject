from tkinter import  *

top = Tk()
playlist = []

def results():
    result = E1.get()
    playlist.append(result)
    E1.delete(0, END)
    
def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
    for item in list:
        f.write("%s/n" % item)
    
#this is a label widget
L1 = Label(top, text="Playlist generator")
L1.grid(column= 0, row= 1)

#this is a entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)


#This is a button widget
B1 = Button(text = " + ", bg="red", command= results)
B1.grid(column= 1, row= 3)

B2 = Botton(text = " print",bg =b"light blue", command= results
B2.grid(column= 2, row= 2)

top.mainloop()
