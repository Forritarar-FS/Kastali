from . import room
from tkinter import *
from tkinter import messagebox

print('Welcome to Room 24!')

class stebbi():
    Tk = None
    
    fucks = 0
    
    texti = None
    cattexti = None
    
    inc = 1
    auto = 0
    
    catamt = 0
    anonamt = 0
    
    costcat = 20

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
            stebbi.texti.set(stebbi.fucks)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks given!!!")
        
    def anonfun():
        if stebbi.fucks >= 100:
            stebbi.anonamt += 1
            stebbi.fucks -= 100
            stebbi.texti.set(stebbi.fucks)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks given!!!")
        
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
        
        catcost = Label(stebbi.upgrades, textvariable=stebbi.cattexti)
        
        cat = Button(stebbi.upgrades, text="Cat", command=stebbi.catfun)
        anoncost = Label(stebbi.upgrades, text="Cost:")
        anonymous = Button(stebbi.upgrades, text="Anonymous", command=stebbi.anonfun)
        upgrade3 = Button(stebbi.upgrades, text="Upgrade3", command=stebbi.upgradefun3)
        upgrade4 = Button(stebbi.upgrades, text="Upgrade4", command=stebbi.upgradefun4)
        upgrade5 = Button(stebbi.upgrades, text="Upgrade5", command=stebbi.upgradefun5)
        upgrade6 = Button(stebbi.upgrades, text="Upgrade6", command=stebbi.upgradefun6)
        upgrade7 = Button(stebbi.upgrades, text="Upgrade7", command=stebbi.upgradefun7)
        
        catcost.pack()
        cat.pack()
        anoncost.pack()
        anonymous.pack()
        #cost.pack()
        upgrade3.pack()
        #cost.pack()
        upgrade4.pack()
        #cost.pack()
        upgrade5.pack()
        #cost.pack()
        upgrade6.pack()
        #cost.pack()
        upgrade7.pack()
        
        mainloop()
        
        
    
def do():
    kalli = stebbi()
    kalli.display()