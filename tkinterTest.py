from tkinter import  *

top = Tk()
playlist = []

top = Tk()
playlist = []
myRolls = []

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
    B2Main = button(text = "Week 2", bg = "White",command = week2)
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
        def rollDice():
            dieType = E2Week2.get()
            rollTimes = E1Week2.get()
            #clear window after updateing veriables 
            clearwindow()
            for x in range(0, int(rollTimes)):
                myRolls.append(random.randint(1, int(dieType)))
            #build the results window
            L4Week2 = Lable(top, text = "Here's your rolls!")
            L4Week2.grid(column= 0, row= 1)
            
            L5Week2 = Lable(top, text= "{}".format(myRolls))
            L5Week2.grid(column= 0, row=2)
            
            B2Week2 = Botton(text="Main Menu", bg= "yellow", command= mainMenu)
            B2Week2.grid(column= 0, row=3)

        
        clearWindow()
        B1Week2 = Button(text= "Roll em!" , bg="yellow")
        B1Week2.grid(column = 2, row= 4)
        
        L1Week2 = Label(top, text= "Dice Roller App")
        L1Week2.grid(column= 2, row= 1)
        
        L2Week2 = Label(top, text= "# of Rolls")
        L2Week2.grid(column= 0, row= 2)
                        
        L3Week2 = Label(top, text= "# of Slides")
        L3Week2.grid(column= 3, row= 2)
        
        E1Week2 = Entry(Top, bd = 5)
        E1Week2.grid(column= 0, row = 3)

        E2Week2 = Entry(Top, bd = 5)
        E2Week2.grid(column= 3, row = 3)


# Open window having dimension 200x100
top.geometry('200x100')
	
# Create a Button
button = Button(top,
				text = 'Submit',
				bg='blue').pack()



if __name__ == "__main__":
    mainMenue()
    top.mainloop()
