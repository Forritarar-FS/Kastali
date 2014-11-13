from . import room
from tkinter import *
from tkinter import messagebox
import threading

print('Welcome to Room 24!')

class stebbi():
    Tk = None
    
    fps = 0
    fpc = 1
    fucks = 0
    totfucks = 0

    fpcup = 0
    fpcupcost = 1000
    
    texti = 0
    fpstexti = 0
    fpctexti = 1
    morefpctexti = None

    metexti = 20
    cattexti = 150
    anontexti = 750
    humantexti = 2000
    illumtexti = 5000
    valvetexti = 10000
    gabentexti =50000

    meamt = 0
    catamt = 0
    anonamt = 0
    humanamt = 0
    illumamt = 0
    valveamt = 0
    gabenamt = 0

    mecost = 20
    catcost = 150
    anoncost = 750
    humancost = 2000
    illumcost = 5000
    valvecost = 10000
    gabencost = 50000

    D = room.grunnur(24)

    def __init__(self):
        pass
    def display(self):
        stebbi.Tk = Tk()

        stebbi.Tk.resizable(width=FALSE, height=FALSE)
        stebbi.Tk.minsize(width=150, height=150)
        stebbi.Tk.attributes("-toolwindow", 1)
        stebbi.Tk.title("Fuck Giver")

        stebbi.D.info = ("Click the 'Give a Fuck' button to gain fucks.\nUse the fucks in the Store which you can find in the menubar.")
        print(stebbi.D.info)

        menubar = Menu(stebbi.Tk)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=stebbi.about)
        helpmenu.add_command(label="Help", command=stebbi.help)
        helpmenu.add_command(label="Statistics", command=stebbi.stats)
        menubar.add_cascade(label="Help", menu=helpmenu)

        storemenu = Menu(menubar, tearoff=0)

        storemenu.add_command(label="Store", command=stebbi.store)
        storemenu.add_command(label="Upgrades", command=stebbi.upgrades)
        menubar.add_cascade(label="Store", menu=storemenu)
        
        stebbi.Tk.config(menu=menubar)
        
        fucksgiven = Label(stebbi.Tk, text="Fucks given:")
        
        stebbi.texti = StringVar()
        stebbi.texti.set(stebbi.fucks)
        clickamt = Label(stebbi.Tk, textvariable=stebbi.texti)
        
        b = Button(stebbi.Tk, text="Give a Fuck", command=stebbi.click)

        fpsLabel = Label(stebbi.Tk, text="Fucks Per Second(FPS):")

        stebbi.fpstexti = StringVar()
        stebbi.fpstexti.set(stebbi.fps)
        dispfps = Label(stebbi.Tk, textvariable=stebbi.fpstexti)

        fpcLabel = Label(stebbi.Tk, text="Fucks Per Click(FPC):")

        stebbi.fpctexti = StringVar()
        stebbi.fpctexti.set(stebbi.fpc)
        dispfpc = Label(stebbi.Tk, textvariable=stebbi.fpctexti)
        
        fucksgiven.pack()
        clickamt.pack()
        b.pack()
        fpsLabel.pack()
        dispfps.pack()
        fpcLabel.pack()
        dispfpc.pack()

        stebbi.autofps()
        messagebox.showinfo('Welcome!', 'Welcome to Room24. \nHere you will be clicking A LOT. \nThe only way to get out of here is to gather enough fucks. \nAnd with those fucks you will be able to buy upgrades and stuffs. \nEventually you will have enough to buy one of the three "Exit" upgrades and get out of here. \nIf you need help just click the Help dropdown menu and then click Help \nHappy clicking and have fun! \nMade by Stebbbi')

        error = messagebox.askquestion('Error?', 'Is there a error in the console?')
        if error == 'yes':
            print('Hello')
            stebbi.Tk.destroy()
            do()

        mainloop()
    
    def click():
            stebbi.fucks += stebbi.fpc
            print(stebbi.fucks)
            stebbi.texti.set(stebbi.fucks)


    def mefun():
        if stebbi.fucks >= stebbi.mecost:
            stebbi.meamt += 1
            stebbi.fucks -= stebbi.mecost
            stebbi.mecost = stebbi.mecost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.mecost = round(stebbi.mecost)
            stebbi.fps += 0.1
            stebbi.texti.set(stebbi.fucks)
            stebbi.metexti.set(stebbi.mecost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")

    def catfun():
        if stebbi.fucks >= stebbi.catcost:
            stebbi.catamt += 1
            stebbi.fucks -= stebbi.catcost
            stebbi.catcost = stebbi.catcost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.catcost = round(stebbi.catcost)
            stebbi.fps += 1
            stebbi.texti.set(stebbi.fucks)
            stebbi.cattexti.set(stebbi.catcost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")
        
    def anonfun():
        if stebbi.fucks >= stebbi.anoncost:
            stebbi.anonamt += 1
            stebbi.fucks -= stebbi.anoncost
            stebbi.anoncost = stebbi.anoncost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.anoncost = round(stebbi.anoncost)
            stebbi.fps += 5
            stebbi.texti.set(stebbi.fucks)
            stebbi.anontexti.set(stebbi.anoncost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")
        

    def humanfun():
        if stebbi.fucks >= stebbi.humancost:
            stebbi.humanamt += 1
            stebbi.fucks -= stebbi.humancost
            stebbi.humancost = stebbi.humancost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.humancost = round(stebbi.humancost)
            stebbi.fps += 15
            stebbi.texti.set(stebbi.fucks)
            stebbi.humantexti.set(stebbi.humancost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")
        
    def illumfun():
        if stebbi.fucks >= stebbi.illumcost:
            stebbi.illumamt += 1
            stebbi.fucks -= stebbi.illumcost
            stebbi.illumcost = stebbi.illumcost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.illumcost = round(stebbi.illumcost)
            stebbi.fps += 50
            stebbi.texti.set(stebbi.fucks)
            stebbi.illumtexti.set(stebbi.illumcost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")
        
    def valvefun():
        if stebbi.fucks >= stebbi.valvecost:
            stebbi.valveamt += 1
            stebbi.fucks -= stebbi.valvecost
            stebbi.valvecost = stebbi.valvecost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.valvecost = round(stebbi.valvecost)
            stebbi.fps += 200
            stebbi.texti.set(stebbi.fucks)
            stebbi.valvetexti.set(stebbi.valvecost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")
        
    def gabenfun():
        if stebbi.fucks >= stebbi.gabencost:
            stebbi.gabenamt += 1
            stebbi.fucks -= stebbi.gabencost
            stebbi.gabencost = stebbi.gabencost * 1.1
            stebbi.fucks = round(stebbi.fucks, 1)
            stebbi.gabencost = round(stebbi.gabencost)
            stebbi.fps += 1000
            stebbi.texti.set(stebbi.fucks)
            stebbi.gabentexti.set(stebbi.gabencost)
            stebbi.fpstexti.set(stebbi.fps)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")

    def autofps():
        stebbi.fucks += stebbi.fps
        stebbi.fucks = round(stebbi.fucks, 1)
        stebbi.texti.set(stebbi.fucks)
        threading.Timer(1, stebbi.autofps).start()
        
    def item():
        stebbi.D.items.append("A Single Fuck")
            
    def about():
        messagebox.showinfo('About', 'This is a clicker game made by Stebbbi')
        
    def help():
        messagebox.showinfo('Help', stebbi.D.info)

    def stats():
        stebbi.stat = Tk()

        Label(stebbi.stat, text="Statistics").pack()

    def morefpc():
        if stebbi.fucks >= stebbi.fpcupcost:
            stebbi.fucks -= stebbi.fpcupcost
            stebbi.fpc = stebbi.fpc * 2
            stebbi.fpcupcost *= 2
            stebbi.fpcup += 1
            stebbi.fpctexti.set(stebbi.fpc)
            stebbi.texti.set(stebbi.fucks)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")

    def exit():
        def room14():
            stebbi.Tk.destroy()
            stebbi.D.go('n')

        def room23():
            stebbi.Tk.destroy()
            stebbi.D.go('w')

        def room34():
            stebbi.Tk.destroy()
            stebbi.D.go('s')

        if stebbi.fucks >= 250000:
            exitwin = Toplevel()

            Label(exitwin, text='Which room do you want to go to?').grid(row=0, column=0)
            Button(exitwin, text='Room 14', command=room14).grid(row=1)
            Button(exitwin, text='Room 23', command=room23).grid(row=2)
            Button(exitwin, text='Room 34', command=room34).grid(row=3)
        else:
            messagebox.showerror("FUCK!", "Not enough Fucks to give!!!")






    def upgrades():
        stebbi.upgrades = Toplevel()

        stebbi.upgrades.resizable(width=FALSE, height=FALSE)
        stebbi.upgrades.minsize(width=150, height=150)
        stebbi.upgrades.attributes("-toolwindow", 1)
        stebbi.upgrades.title("Upgrades")

        Label(stebbi.upgrades, text="Upgrades!").pack()
        if stebbi.fpcup < 11:
            if stebbi.fpcup == 0:
                fpcupt = "More FPC"
            elif stebbi.fpcup == 1:
                fpcupt = "Even More FPC!"
            elif stebbi.fpcup == 2:
                fpcupt = "A Lot of FPC!!"
            elif stebbi.fpcup == 3:
                fpcupt = "A LOT OF FPC!!!"
            elif stebbi.fpcup == 4:
                fpcupt = "Shitloads of FPC!!!!"
            elif stebbi.fpcup == 5:
                fpcupt = "Shittons of FPC!!!!!"
            elif stebbi.fpcup == 6:
                fpcupt = "OMG FPC!!!!!!"
            elif stebbi.fpcup == 7:
                fpcupt = "GODLIKE FPC!!!!!!!"
            elif stebbi.fpcup == 8:
                fpcupt = "UNSTOPPABLE FPC!!!!!!!!"
            elif stebbi.fpcup == 9:
                fpcupt = "GG FPC!!!!!!!!!"
            elif stebbi.fpcup == 10:
                fpcupt = "LORD GABEN FPC!!!!!!!!!!"
            stebbi.morefpctexti = StringVar()
            stebbi.morefpctexti.set(fpcupt)
            Button(stebbi.upgrades, textvariable=stebbi.morefpctexti, command=stebbi.morefpc).pack()

            Button(stebbi.upgrades, text="Exit", command=stebbi.exit).pack()



        mainloop()


    def store():
        stebbi.stores = Toplevel()

        stebbi.stores.resizable(width=FALSE, height=FALSE)
        stebbi.stores.minsize(width=150, height=150)
        stebbi.stores.attributes("-toolwindow", 1)
        stebbi.stores.title("Store")
        
        menubar = Menu(stebbi.stores)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=stebbi.about)
        helpmenu.add_command(label="Help", command=stebbi.help)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        stebbi.stores.config(menu=menubar)
        
        stebbi.metexti = StringVar()
        stebbi.metexti.set(stebbi.mecost)
        Label(stebbi.stores, text="Cost: ").grid(row=0, column=1)
        Label(stebbi.stores, textvariable=stebbi.metexti).grid(row=0, column=2)
        Button(stebbi.stores, text="Me", command=stebbi.mefun).grid(row=0)


        stebbi.cattexti = StringVar()
        stebbi.cattexti.set(stebbi.catcost)
        Label(stebbi.stores, text="Cost: ").grid(row=1, column=1)
        Label(stebbi.stores, textvariable=stebbi.cattexti).grid(row=1, column=2)
        Button(stebbi.stores, text="Cat", command=stebbi.catfun).grid(row=1)

        
        stebbi.anontexti = StringVar()
        stebbi.anontexti.set(stebbi.anoncost)
        Label(stebbi.stores, text="Cost: ").grid(row=2, column=1)
        Label(stebbi.stores, textvariable=stebbi.anontexti).grid(row=2, column=2)
        Button(stebbi.stores, text="Anonymous", command=stebbi.anonfun).grid(row=2)


        stebbi.humantexti = StringVar()
        stebbi.humantexti.set(stebbi.humancost)
        Label(stebbi.stores, text="Cost: ").grid(row=3, column=1)
        Label(stebbi.stores, textvariable=stebbi.humantexti).grid(row=3, column=2)
        Button(stebbi.stores, text="Humans", command=stebbi.humanfun).grid(row=3)


        stebbi.illumtexti = StringVar()
        stebbi.illumtexti.set(stebbi.illumcost)
        Label(stebbi.stores, text="Cost: ").grid(row=4, column=1)
        Label(stebbi.stores, textvariable=stebbi.illumtexti).grid(row=4, column=2)
        Button(stebbi.stores, text="Illuminati", command=stebbi.illumfun).grid(row=4)


        stebbi.valvetexti = StringVar()
        stebbi.valvetexti.set(stebbi.valvecost)
        Label(stebbi.stores, text="Cost: ").grid(row=5, column=1)
        Label(stebbi.stores, textvariable=stebbi.valvetexti).grid(row=5, column=2)
        Button(stebbi.stores, text="Valve", command=stebbi.valvefun).grid(row=5)


        stebbi.gabentexti = StringVar()
        stebbi.gabentexti.set(stebbi.gabencost)
        Label(stebbi.stores, text="Cost: ").grid(row=6, column=1)
        Label(stebbi.stores, textvariable=stebbi.gabentexti).grid(row=6, column=2)
        Button(stebbi.stores, text="Lord Gaben", command=stebbi.gabenfun).grid(row=6)

        mainloop()
        
        
    
def do():
    kalli = stebbi()
    kalli.display()