from . import room
from tkinter import *
from tkinter import messagebox

print('Welcome to Room 24!')

fucks = 0
inc = 1
auto = 0

def do():
    def help():
        messagebox.showinfo('Help', D.info)
    
    def click():
        global fucks
        fucks += inc
        print(fucks)
        texti.set(fucks)
    
    root = Tk()
        
    D = room.grunnur(24)
    D.info = ("Welcome to my clicker game. You gotta click until you can click no more! Or atleast until you have bought all the stuffs!")
    print(D.info)
    
    menubar = Menu(root)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="Help", command=help)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    root.config(menu=menubar)
    
    fucksgiven = Label(root, text="Fucks given:")
    texti = StringVar()
    texti.set(fucks)
    clickamt = Label(root, textvariable=texti)
    
    b = Button(root, text="Hello", command=click)
    upgradeB = Button(root, text="Upgrades", command=upgrades)
    
    fucksgiven.pack()
    clickamt.pack()
    b.pack()
    upgradeB.pack()
    
    mainloop()
    
def upgrades():
    upgrades = Tk()
    
    menubar = Menu(upgrades)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="Help", command=help)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    upgrades.config(menu=menubar)
    
    cat = Button(upgrades, text="Cat", command=catfun)
    upgrade2 = Button(upgrades, text="Upgrade2", command=upgradefun2)
    upgrade3 = Button(upgrades, text="Upgrade3", command=upgradefun3)
    upgrade4 = Button(upgrades, text="Upgrade4", command=upgradefun4)
    upgrade5 = Button(upgrades, text="Upgrade5", command=upgradefun5)
    upgrade6 = Button(upgrades, text="Upgrade6", command=upgradefun6)
    upgrade7 = Button(upgrades, text="Upgrade7", command=upgradefun7)
    
    cat.pack()
    upgrade2.pack()
    upgrade3.pack()
    upgrade4.pack()
    upgrade5.pack()
    upgrade6.pack()
    upgrade7.pack()
    
    mainloop()
    
def catfun():
    catamt += 1
    
def upgradefun2():
    upgrade2amt += 1
    
def upgradefun3():
    upgrade3amt += 1

def upgradefun4():
    upgrade4amt += 1
    
def upgradefun5():
    upgrade5amt += 1
    
def upgradefun6():
    upgrade6amt += 1
    
def upgradefun7():
    upgrade7amt += 1
    
def item():
    D.items.append("Clicker Item")
        
def about():
    messagebox.showinfo('About', 'message')