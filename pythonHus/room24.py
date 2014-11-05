from . import room
from tkinter import *
from tkinter import messagebox

print('Welcome to Room 24!')

class stebbi():
    Tk = None
    
    fps = 0
    fucks = 0
    
    texti = None
    cattexti = 20
    anontexti = 100
    
    inc = 1
    auto = 0
    
    catamt = 0
    anonamt = 0
    
    costcat = 20
    anoncost = 100

    def __init__(self):
        pass
    def display(self):
        stebbi.Tk = Tk()
            
        D = room.grunnur(24)
        D.info = ("Welcome to my clicker game. You gotta click until you can click no more! Or atleast until you have bought all the stuffs!")
        print(D.info)
        
        menubar = Menu(stebbi.Tk)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=stebbi.about)
        helpmenu.add_command(label="Help", command=stebbi.help)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        stebbi.Tk.config(menu=menubar)
        
        fucksgiven = Label(stebbi.Tk, text="Fucks given:")
        
        stebbi.texti = StringVar()
        stebbi.texti.set(stebbi.fucks)
        clickamt = Label(stebbi.Tk, textvariable=stebbi.texti)
        
        b = Button(stebbi.Tk, text="Hello", command=stebbi.click)
        upgradeB = Button(stebbi.Tk, text="Upgrades", command=stebbi.upgrades)
        
        fucksgiven.pack()
        clickamt.pack()
        b.pack()
        upgradeB.pack()
        
        mainloop()
    
    def click():
            stebbi.fucks += stebbi.inc
            print(stebbi.fucks)
            stebbi.texti.set(stebbi.fucks)


    def catfun():
        if stebbi.fucks >= stebbi.costcat:
            stebbi.catamt += 1
            stebbi.fucks -= stebbi.costcat
            stebbi.costcat = stebbi.costcat * 1.1
            stebbi.fps += 0.1
            stebbi.texti.set(stebbi.fucks)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks given!!!")
        
    def anonfun():
        if stebbi.fucks >= stebbi.anoncost:
            stebbi.anonamt += 1
            stebbi.fucks -= stebbbi.anoncost
            stebbi.anoncost = stebbbi.anoncost * 1.1
            stebbi.fps += 0.5
            stebbi.texti.set(stebbi.fucks)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks given!!!")
        
    def upgradefun3():
        pass
    
    def upgradefun4():
        upgrade4amt += 1
        
    def upgradefun5():
        upgrade5amt += 1
        
    def upgradefun6():
        upgrade6amt += 1
        
    def upgradefun7():
        upgrade7amt += 1
        
    def item():
        D.items.append("A Single Fuck")
            
    def about():
        messagebox.showinfo('About', 'message')
        
    def help():
        messagebox.showinfo('Help', D.info)




    def upgrades():
        stebbi.upgrades = Tk()
        
        menubar = Menu(stebbi.upgrades)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=stebbi.about)
        helpmenu.add_command(label="Help", command=stebbi.help)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        stebbi.upgrades.config(menu=menubar)
        
        stebbi.cattexti = StringVar()
        stebbi.cattexti.set(stebbi.costcat)
        Label(stebbi.upgrades, text="Cost: ").grid(row=0, column=1)
        Label(stebbi.upgrades, textvariable=stebbi.cattexti).grid(row=0, column=2)
        Button(stebbi.upgrades, text="Cat", command=stebbi.catfun).grid(row=0)
        
        stebbi.anontexti = StringVar()
        stebbi.anontexti.set(stebbi.anoncost)
        Label(stebbi.upgrades, text="Cost: ").grid(row=1, column=1)
        Label(stebbi.upgrades, textvariable=stebbi.anontexti).grid(row=1, column=2)
        Button(stebbi.upgrades, text="Anonymous", command=stebbi.anonfun).grid(row=1)
        
        Label(stebbi.upgrades, text="Cost:").grid(row=2, column=1)
        Button(stebbi.upgrades, text="Upgrade3", command=stebbi.upgradefun3).grid(row=2)
        Label(stebbi.upgrades, text="Cost:").grid(row=3, column=1)
        Button(stebbi.upgrades, text="Upgrade4", command=stebbi.upgradefun4).grid(row=3)
        Label(stebbi.upgrades, text="Cost:").grid(row=4, column=1)
        Button(stebbi.upgrades, text="Upgrade5", command=stebbi.upgradefun5).grid(row=4)
        Label(stebbi.upgrades, text="Cost:").grid(row=5, column=1)
        Button(stebbi.upgrades, text="Upgrade6", command=stebbi.upgradefun6).grid(row=5)
        Label(stebbi.upgrades, text="Cost:").grid(row=6, column=1)
        Button(stebbi.upgrades, text="Upgrade7", command=stebbi.upgradefun7).grid(row=6)
        
        mainloop()
        
        
    
def do():
    kalli = stebbi()
    kalli.display()