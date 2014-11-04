from . import room
from tkinter import *
from tkinter import messagebox
import tkinter

print("Welcome to Mr.Bones Wild ride!!");
messagebox.showinfo("Mr.Bones","Welcome to Mr.Bones Wild ride!")

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
	messagebox.showinfo("Mr.Bones","You walk down a long hallway")
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
		if "A Fuck to give" in room.grunnur.items:
			messagebox.showerror("Mr.Bones","The given fuck Can open this door.")
			messagebox.showerror("Mr.Bones","You found a red cane!")
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
	Messagebox.showerror("Mr.Bones","Not all correct ways are to the right.")
	kb = Messagebox.askquestion("Mr.Bones","would you like to proceed?")
	if kb == "yes":
		messagebox.showerror("Mr.Bones","You tripped and died.")
		exec("GAME OVER")
	messagebox.showerror("Mr.Bones","Or...wait here.")
	messagebox.showerror("Mr.Bones","You walk forward regardless of your will")
	ko = messagebox.askquestion("Mr.Bones","You see a fork in the road. turn right?")
	if ko == "no":
		messagebox.showerror("Mr.Bones","You suddenly explode without reason.")
		exec("GAME OVER")
	kp = messagebox.askquestion("Mr.Bones","Strange. There is another fork in the rode you just chose...left?")
	if kp =="yes":
			billy()
	ja = messagebox.askquestion("Mr.Bones","Yet another fork. Go right?")
	if ja == "yes":
		messagebox.showinfo("Mr.Bones","You step on a landmine.")
		exec("GAME OVER BITCH!")
	hf= messagebox.askquestion("Mr.Bones","these 'forks' seem to go on endlessly. Left? Yes? No?")
	if hf =="yes":
			bobby()
	ge=messagebox.askquestion("Mr.Bones","Right?")
	if ge=="yes":
		asdf()
	gh=messagebox.askquestion("Mr.Bones","right again?")
	if gh =="yes":
	 	messagebox.showerror("Mr.Bones","WRONG!!!")
	 	exec("GAME OVER")
	gq=messagebox.askquestion("Mr.Bones","Left?")
	if gq=="yes":
	 	messagebox.showerror("Mr.Bones","You step forward not knowing that the roof just caved in on you.")
	 	exec("GAME OVER")
	messagebox.showerror("Mr.Bones","You turn and turn, after thoushands of left and rights you see a sign.")
	gf=messagebox.askquestion("Mr.Bones","Want to read it?")
	if gf=="yes":
	 	gj= messagebox.askquestion("Mr.Bones","It is a sign for the blind. Want to try reading it anyway?")
	 	if gj=="yes":
	 		messagebox.showinfo("Mr.Bones","It says 'Dead end bitch!'")
	 	else:
	 		messagebox.showerror("Mr.Bones","You choke on the sign.")
	else:
		messagebox.showinfo("Mr.Bones","you sit still. You sit still for a looooooong time.")
		messagebox.showinfo("Mr.Bones","Yup....waiting.")
		i = 0
		while i != 20:
			messagebox.showinfo("Mr.Bones","")
			i += 1
 	
		messagebox.showerror("Mr.Bones","You suddenly starve. I wonder why")
		exec("GAME OVER")

def billy():
	#Blue gem(green door)
	messagebox.showerror("Mr.Bones","Something is rolling towards you.")
	messagebox.showerror("Mr.Bones","LOOK OUT! YOUR MOM IS ROLLING TOWARDS YOU!")
	Stebbbi=messagebox.askquestion("Mr.Bones","Want to roll for your fat ass life?")
	if Stebbbi =="no":
		messagebox.showerror("Mr.Bones","You were crushed by your fat 'everything' mom.")
		exec("GAME OVER")
	messagebox.showinfo("Mr.Bones","You did it! you managed to roll to safety!")
	gd= messagebox.askquestion("Mr.Bones","You see a small door. Wanna look at it?")
	if gd=="yes":
		messagebox.showinfo("Mr.Bones","This door needs a key of strange shape.")
		if "Red Cane" in room.grunnur.items:
			messagebox.showinfo("Mr.Bones","You opened the door!")
			messagebox.showerror("Mr.Bones","It's a death trap!")
			exec("GAME OVER")
	gk = messagebox.askquestion("Mr.Bunes","Would you like to have sex with the devil?")
	if gk=="yes":
		messagebox.showerror("Mr.Bones","You have sex with the devil and get a blue gem for it!")
		messagebox.showerror("Mr.Bones","The devil, feeling satisfied. teleports you away!")
		asdf()
	else:
		messagebox.showerror("Mr.Bones","The devil anally raped you to death.")
		exec("666")

def asdf():
	#red door
	#teleporter(munch)
	#teleporter(tellypurter)
	messagebox.showinfo("Mr.Bones","You wake up infront of a big red door.")
	gb=messagebox.askquestion("Mr.Bones","Want to inspect the door?")
	if gb=="yes":
		messagebox.showinfo("Mr.Bones","This door opens with the gem the devil gave you.")
		messagebox.showerror("Mr.Bones","The door sucks you into itself like a chinese hooker begging for a job.")
		do()
	messagebox.showinfo("Mr.Bones","you see a fat man standing before you holding a cleaver.")
	gv=messagebox.askquestion("Mr.Bones","Will you greet the fat man?")
	if gv=="no":
		messagebox.showerror("Mr.Bones","You offended the fat man and he killed you.")
		exec("GAME OVER")
	messagebox.showinfo("Mr.Bones","The fat man high fives you with his cleaver and gives you some advice.")
	messagebox.showinfo("Mr.Bones","'Try to stay clear of Mr.Bones. Once he sees you, you'll never get out again unless he wants you to.")
	gj=messagebox.askquestion("Mr.Bones","You see two teleporters ahead. will you take the first one?")
	if gj=="yes":
		munch()
	else:
		messagebox.showinfo("Mr.Bones","You take the second teleporter.")
		tellypurter()
	
def bobby():
	#teleporter(reroll)
	messagebox.showerror("Mr.Bones","you realise that this room has only two ways.")
	gm=messagebox.askquestion("Mr.Bones","Will you go to the left?")
	if gm=="yes":
		messagebox.showinfo("Mr.Bones","Good.")
		do()
	else:
		reroll()
def munch():
	#dead end
	messagebox.showerror("Mr.Bones","you come to realise that all teleporters are one way.")
	messagebox.showerror("Mr.Bones","You also realise that you are standing in a small room with only the teleporter.")
	messagebox.showinfo("Mr.Bones","you sit still. You sit still for a looooooong time.")
	messagebox.showinfo("Mr.Bones","Yup....waiting.")
	i = 0
	while i != 20:
		messagebox.showinfo("Mr.Bones","")
		i += 1

	messagebox.showerror("Mr.Bones","You suddenly starve. I wonder why")
	exec("GAME OVER")

def reroll():
	#teleporter(beginning)
	messagebox.showinfo("Mr.Bones","you see just one teleporter besides the one you came out of.")
	op=messagebox.askquestion("Mr.Bones","Will you take the teleporter?")
	if op=="yes":
		messagebox.showinfo("Mr.Bones","You take the teleporter.")
		do()
	else:
		messagebox.showinfo("Mr.Bones","You take the teleporter anyway.")
		deadly()
def deadly():
	#dead end
	#teleporter(dead)
	messagebox.showinfo("Mr.Bones","you see what appears to be a long narrow path.")
	messagebox.showinfo("Mr.Bones","Like the idiot you are, you go right ahead.")
	messagebox.showwarning("Mr.Bones","you see a horny woman infront of you.")
	pq= messagebox.askquestion("Mr.Bones","will you talk to her?")
	if pq=="yes":
		messagebox.showerror("Mr.Bones","she stabs you with her horns")
		exec("GAME OVER")
	messagebox.showinfo("Mr.Bones","A teleporter appears before you")
	oz=messagebox.askquestion("Mr.Bones","Dare you take it?")
	if oz=="yes":
		messagebox.showinfo("Mr.Bones","You swish and poof away!")
		dead()
	else:
		messagebox.showinfo("Mr.Bones","You move on.")
		messagebox.showinfo("Mr.Bones","As you walk you begin to ponder")
		messagebox.showinfo("Mr.Bones","You wonder as to WHY Mr.Bones is doing this to you")
		messagebox.showwarning("Mr.Bones","As you ponder this Mr.Bones himself appears before you")
		messagebox.askyesno("Mr.Bones","Hey, do you know what im going to do?")
		messagebox.showwarning("Mr.Bones","Good.")
		messagebox.showwarning("Mr.Bones","Because now...")
		exec("YOU DEAD! ~Mr.Bones")
		


def tellypurter():
	#teleporter(vault)
	#teleporter(deadly)
	messagebox.showinfo("Mr.Bones","This place looks like a center station of some kind.")
	messagebox.showinfo("Mr.Bones","It seems that this is a teleporter center.")
	messagebox.showinfo("Mr.Bones","You see only two doors that arent locked.")
	messagebox.showinfo("Mr.Bones","One of them is marked with a badly painted red X")
	messagebox.showinfo("Mr.Bones","The other one has a sign above it which reads 'Vault'")
	jq= messagebox.askquestion("Mr.Bones","Will you enter the vault?")
	if jq=="yes":
		vault()
	else:
		deadly()
	
def vault():
	#door(break down)
	#monster filled vault
	messagebox.showinfo("Mr.Bones","What is this? you are in an office like room.")
	messagebox.showinfo("Mr.Bones","There! On the table! There is some equipment to escape with!")
	messagebox.showinfo("Mr.Bones","You cautiosly take the equipment. Nothing strange happens.")
	messagebox.showinfo("Mr.Bones","Could this be? Could this finally be an exit?")
	messagebox.showinfo("Mr.Bones","you see a old wooden door, Its barred and marked. 'there is no escape'")
	messagebox.showinfo("Mr.Bones","It looks like Mr.Bones wanted to hide this door from me....")
	lq= messagebox.askquestion("Mr.Bones","Will you break down the door?")
	if lq=="yes":
		paq= messagebox.askretrycancel("Mr.Bones","The door breaks a little, but not enough to open it.")
		if paq=="retry":
			messagebox.showinfo("Mr.Bones","The door breaks!")
			messagebox.showinfo("Mr.Bones","There is a big safe door in there with the sign 'Vault' on it.")
			oqa=messagebox.askquestion("Mr.Bones","Open the door?")
			if oqa=="yes":
				messagebox.showinfo("Mr.Bones","The door opens and you are blinded")
				messagebox.showinfo("Mr.Bones","It's sunlight! You did it! You escaped!")
				Messagebox.showerror("Mr.Bones","You were slaughtered by a horde of monsters.")
				exec("GAME OVER")
			else:
				messagebox.showinfo("Mr.Bones","The Vault suddenly opens.")
				messagebox.showinfo("Mr.Bones","Light suddenly shines on you, are you finally free?")
				Messagebox.showerror("Mr.Bones","nope. There was a horde of monsters in there.")
				Messagebox.showinfo("Mr.Bones","Artificial rooms sure are sweet huh?")
				exec("GAME OVER")

		else:
			messagebox.showinfo("Mr.Bones","You lay down and begin to cry.")
			messagebox.showinfo("Mr.Bones","You cried so much that you are dehydrated.")
			messagebox.showerror("Mr.Bones","You drowned in your own tears.")
			exec("GAME OVER")

	else:
		messagebox.showinfo("Mr.Bones","You take your equipment and go back.")
		messagebox.showerror("Mr.Bones","You bump into Mr.Bones!")
		messagebox.showwarning("Mr.Bones","You're not supposed to be here...")
		messagebox.showinfo("Mr.Bones","Mr.Bones impales you with his sharp cane.")
		exec("GAME OVER")

def dead():
	#teleporter(monster)
	messagebox.showinfo("Mr.Bones","You see some doors infront of you.")
	io=messagebox.askquestion("Mr.Bones","Want to enter the doors?")
	if io=="yes":
		i = 0
		while i != 20:
			messagebox.showinfo("Mr.Bones","You open the door and walk in.")
			i += 1
	
		messagebox.showerror("Mr.Bones","A magic portal appears before you.")
		messagebox.showwarning("Mr.Bones","The portal is sucking you in!")
		monster()
	


	else:
		messagebox.showerror("Mr.Bones","You sit down and wait for something to happen.")
		messagebox.showerror("Mr.Bones","A viking pops up and smashes your skull")
		exec("GAME OVER")
def monster():
	#monster(kills you)
	messagebox.showinfo("Mr.Bones","You hear noises as you walk")
	messagebox.showinfo("Mr.Bones","The noises keep comming closer")
	messagebox.showinfo("Mr.Bones","you feel a gentle breath on your neck")
	lz=messagebox.askquestion("Mr.Bones","Run?")
	if lz=="no":
		messagebox.showerror("Mr.Bones","You slowsly die inside the stomach of your mothers anal cavity")
	else:
		messagebox.showerror("Mr.Bones","you run like a black man stealing a bike.")
	messagebox.showinfo("Mr.Bones","you see a fork in the road. what do you do?")
	messagebox.askquestion("Mr.Bones","right?")
	messagebox.showerror("Mr.Bones","You chose poorly.")
	messagebox.showerror("Mr.Bones","As you run you forget to look infront of you and you slam into a wall.")
	messagebox.showerror("Mr.Bones","You have been eaten!")
	exec("GAME OVER")



#------------------------#
	#til að fara út
	#eitthvad = room.grunnur(23)
	#eitthvad.go("e")