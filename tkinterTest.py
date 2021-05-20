from tkinter import  *
import random


playlist = []


playlist = []
myRolls = []

top = Tk(className='Python Examples - Window Color')
# set window size
top.geometry("400x200")

#set window color
top['background']='light blue'
#gui.configure(background='yellow')

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

def ClearWindow():
    for widget in top.winfo_children():
        widget.destroy()
def mainMenu():
    ClearWindow()
    LMain = Label(top, text = "Block 5 Gui Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text= "Week 1", bg= "white", command = week1)
    B1Main.grid(column= 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "White",command = week2)
    B2Main.grid(column= 0, row = 3)
    B3Main = Button(text = "Week 3", bg = "White")
    B3Main.grid(column= 0, row = 4)
def week1():
    ClearWindow()
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
   
    """
    if int(chosen_element) == 1:
        print('Adding a Customer!!!')
    elif int(chosen_element) == 2:
        print('Searching a Customer!!!')
    elif int(chosen_element) == 3:
        print('Update Customers!!!')
    elif int(chosen_element) == 4:
        print('Delete a Customer!!!')
    elif int(chosen_element) == 5:
        sys.exit()
    else:
        print('Sorry, the value entered must be a number from 1 to 5, then try again!')
     """   
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

    Bexit = Button(text = "Main menu", bg = "red", command = mainMenu)
    Bexit.grid(column = 1, row = 4)
    
def week2():
        def rollDice():
            dieType = E2Week2.get()
            rollTimes = E1Week2.get()
            #clear window after updateing veriables 
            ClearWindow()
            for x in range(0, int(rollTimes)):
                myRolls.append(random.randint(1, int(dieType)))
            #build the results window
            L4Week2 = Label(top, text = "Here's your rolls!")
            L4Week2.grid(column= 0, row= 1)
            
            L5Week2 = Label(top, text= "{}".format(myRolls))
            L5Week2.grid(column= 0, row=2)
            
            B2Week2 = Button(text="Main Menu", bg= "yellow", command= mainMenu)
            B2Week2.grid(column= 0, row=3)

        
        ClearWindow()
        B1Week2 = Button(text= "Roll em!" , bg="yellow", command = rollDice)
        B1Week2.grid(column = 2, row= 4)
        
        L1Week2 = Label(top, text= "Dice Roller App")
        L1Week2.grid(column= 2, row= 1)
        
        L2Week2 = Label(top, text= "# of Rolls")
        L2Week2.grid(column= 0, row= 2)
                        
        L3Week2 = Label(top, text= "# of Slides")
        L3Week2.grid(column= 3, row= 2)
        
        E1Week2 = Entry(top, bd = 5)
        E1Week2.grid(column= 0, row = 3)

        E2Week2 = Entry(top, bd = 5)
        E2Week2.grid(column= 3, row = 3)


# Open window having dimension 200x100
top.geometry('200x100')
	
# Create a Button
button = Button(top, text = 'Submit', bg='blue').pack()



if __name__ == "__main__":
    mainMenu()
    top.mainloop()
    
