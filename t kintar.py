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

def clearwindow():
    for widget in top.winfo_children():
        widgets.destroy()
def mainMenu():
    clerwindow()
    LMain = Label(top, text = "Block 5 Gui Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = button(text= "Week 1", bg= "white", comand = week1)
    B1Main.grid(column= 0, row = 2)
    B2Main = button(text = "Week 2", bg = "White")
    B2Main.grid(column= 0, row = 3)
    B3Main = button(text = "Week 3", bg = "White")
    B3Main.grid(column= 0, row = 4)
def week1():
    clearWindow()
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
    
    #this is a label widget
    L1 = Label(top, text="Playlist generator")
    L1.grid(column= 0, row= 1)

    #this is a entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)


    #This is a button widget
    B1 = Button(text = " + ", bg="red", command= results)
    B1.grid(column= 1, row= 3)

    B2 = Button(text = " Print ", bg = "light blue", command = printList)
    B2.grid(column= 2, row= 2)

    B3 = Button(text = "Export List", bg = "#B4FFCD", command = results)
    B3.grid(column = 0, row = 3)

    Bexit = button(text = "Main menu", bg = "red", command = mainMenu)
    Bexit.grid(column = 1, row = 3)
    
    def week2():
        clearWindow()
        B1Week2 = Button()
        L1Week2 = Label()
        L2Week2 = Label()
        L3Week2 = Label()
        E1Week2 = Entry()
        E2Week2 = Entry()
    
    
    
    
    
    
    
if__name__ == "__main__":
    mainMenue()
top.mainloop()
