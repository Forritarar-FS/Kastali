from . import room
from tkinter import *
from tkinter import messagebox
import tkinter

print("Welcome to Mr.Bones Wild ride!!");

def do():
	th = room.grunnur(23)
	th.info = "There is no escaping Mr.Bones Wild ride!"
	print (th.info)
		
	
	gg = messagebox.askquestion("Mr.Bones", "Want to go for a ride?")
	if gg == "no":
		messagebox.showerror("Mr.Bones","There is no getting off Mr.Bones wild ride.")
	kk = messagebox.askquestion("Mr.Bones","Would you like to go left?")
	if kk == "yes":
		kok(kk)
	else:
		messagebox.showerror("Mr.Bones","To the Right it is!")
	kl = messagebox.askquestion("Mr.Bones","Something is shining on the floor. Want to pick it up?")
	if kl == "yes":
		messagebox.showerror("Mr.Bones","It turned out to be a death trap and you fell for it.")
		exec("GAME OVER")
	jj = messagebox.askquestion("Mr.Bones","You see a blue door. Want to inspect it?")
	if jj == "yes":
		messagebox.showerror("Mr.Bones","The door needs a key.")		
	bb = messagebox.askquestion("Mr.Bones","Want to go to the Left?")
	if bb == "yes":
		bob()
	else:
		messagebox.showerror("Mr.Bones","You're right. The RIGHT way is ALWAYS to the RIGHT!")
	yo = messagebox.askquestion("Mr.Bones","You've stumbled upon a faintly glowing object. want to take it?")
	if yo == "yes":
		messagebox.showerror("Mr.Bones","You found a glowing dagger. It MUST have SOME use later. right?")
		room.grunnur.items.append("Glowing Dagger")
		#if "Glowing Dagger" in room.grunnur.items
		# to see if person has item.

	jk = messagebox.askquestion("Mr.Bones","You see a teleporter. Want to use it?")
	if jk == "yes":
		messagebox.showerror("Mr.Bones","You use the teleporter and find yourself at the beginning.")
		do()
	else:
		messagebox.showerror("Mr.Bones","You sit down and slowly starve to death.")
		exec("GAME OVER")

def kok(svar):
	#add code later, teleporter to stebbba
	uu = messagebox.askquestion("Mr.Bones","You walk down a long hallway")
	asd = messagebox.askquestion("Mr.Bones","you see something. want to investigate?")
	if asd =="yes":
		messagebox.showerror("Mr.Bones","It turned out to be a trap for the curious. You have died.")
		exec("GAME OVER")
	tt = messagebox.askquestion("Mr.Bones","You look behind yourself and see something following you. Run?")
	if tt == "no":
		messagebox.showerror("Mr.Bones","You have been eaten by a wild piglet")
		exec("GAME OVER")
	hh=messagebox.showerror("Mr.Bones","You run as fast as you can. but you cant catch the gingerbread man")
	kl=messagebox.askquestion("Mr.Bones","Do you want to run after the gingerbread man?")
	if kl =="yes":
		messagebox.showerror("Mr.Bones","You stopped to go after the gingerbread man and the monster chasing you killed you.")
		exec("GAME OVER")
	lp = messagebox.askquestion("Mr.Bones","that thing is still chasing you. want to hide?")
	if lp == "no":
		messagebox.showerror("Mr.Bones","You run as fast as you can. but the monster catches up to you and eats you.")
		exec("GAME OVER")
	jl = messagebox.showerror("Mr.Bones","You hid yourself and see a crazed piglet run past you.")
	
	ba = messagebox.askquestion("Mr.Bones","Want to go out of hiding?")
	if ba =="no":
		messagebox.showerror("Mr.Bones","The piglet sniffed you out and ate you slowly.")
		exec("GAME OVER")
	he = messagebox.showerror("Mr.Bones","You dash out of hiding and run away with fear in your mind and tears in your eyes. Coward.")
	hj= messagebox.askquestion("Mr.Bones","You see two paths ahead of you. will you take the right one?")
	if hj == "no":
		messagebox.showerror("Mr.Bones","You took the left path and bumped into the piglet which began eating you ever so gently.")
		exec("GAME OVER")
	pp=messagebox.askquestion("Mr.Bones","you see a teleporter ahead. want to use it?")
	if pp == "yes":
		messagebox.showerror("Mr.Bones","You find yourself in another room.")
		eitthvad = room.grunnur(23)
		eitthvad.go("e")
	else: 
		messagebox("Mr.Bones","You turn around to see the piglet infront of you. You were eaten with BBQ sauce.")
		exec("GAME OVER")




def bob():
	#add green door
	ll = messagebox.askquestion("Mr.Bones","Would you like to wander about aimlessly?")
	if ll == "yes":
		messagebox.showerror("Mr.Bones","You stumbled upon a trap by falling into it.")
		exec("GAME OVER")
	lk = messagebox.askquestion("Mr.Bones","You see something in the distance. want to check it out?")
	if lk == "yes":
		messagebox.showerror("Mr.Bones","You see a green door. it needs a key of some kind.")
	messagebox.showerror("Mr.Bones","after twists and turns you see a straight path.")

	bg = messagebox.askquestion("Mr.Bones","Will you turn right?")
	if bg == "yes":
		dod()
	else:
		messagebox.showerror("Mr.Bones","You DARE take a left?!?")
	hg = messagebox.askquestion("Mr.Bones","A scary scary scarecrow stands before you. Will you dare to poke it?")
	if hg == "no":
		messagebox.showerror("Mr.Bones","You walk forward and the walls close on you. Killing you instantly.")
		exec("GAME OVER")
	messagebox.showerror("Mr.Bones","The scarecrow screaches unholy screams of terror that send chills down your spine.")
	ki=messagebox.askquestion("Mr.Bones","Will you shit your pants?")
	if ki == "no":
		messagebox.showerror("Mr.Bones","You shat them anyway.")
	bananaleave = room.grunnur(23)
	bananaleave.go("s")

def dod():
	#leads to billy,bobby,asdf
	#dead end


def billy():
	#if svar == "yes"
	#Blue gem(green door)
	pass
def bobby():
	#if svar == "yes"
	#red door, Red cane(blue door)
	pass
def asdf():
	#if svar == "yes"
	#dead end
	pass
#def ():
	#if svar == "yes"
	#dead end
#def ():
	#if svar == "yes"
	#dead end
#def ():
	#if svar == "yes"
	#dead end
#def ():
	#if svar == "yes"
	#teleporter(beginning)
#def ():
	#if svar == "yes"
	#dead end
#def ():
	#if svar == "yes"
	#teleporter()
#def ():
	#if svar == "yes"
	#door(break down)
	#monster filled vault
#def ():
	#if svar == "yes"
	#dead end
#def ():
	#if svar == "yes"
	#monster(kills you)



#------------------------#
	#til að fara út
	#eitthvad = room.grunnur(23)
	#eitthvad.go("e")