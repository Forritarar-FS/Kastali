"""

This game requires the module "rolldice.py" and EasyGui to be
installed. You can find out how to download EasyGui at:
http://easygui.sourceforge.net/download/version_0.96/index.html
Have fun!


"""




import easygui as eg
from . import rolldice
from random import randint
from time import sleep
from . import room
global leftroomencounter
leftroomencounter = 0
mysteryinv = []
def do():
	global mystery
	global leftroomencounter
	leftroomencounter = 0
	mystery = room.grunnur(14)
	mystery.info = "This room takes user inputs for actions. You will write text to make certain actions. At any given point, you can 'look around' to get a better view of your surroundings."
	eg.msgbox("You stand in front of the Room of Mystery")
	reply = eg.buttonbox("Do you go in?", choices=["Yes","No"])
	if reply == "Yes":
		eg.msgbox("Something doesn't seem right here...")
		eg.msgbox(mystery.info)
		entry()
	else:
		leaving()
def leaving():
	sense_of_direction = 0
	while sense_of_direction == 0:	
		direction = eg.buttonbox("Where do you wish to go?",choices=["North", "East", "South", "West"])
		if direction == "North":
			eg.msgbox("You can not go North!")
		elif direction == "East":
			eg.msgbox("You can not go East!")
		elif direction == "South":
			sense_of_direction = 1
			mystery.go("s")
		else:
			sense_of_direction = 1
			mystery.go("w")
def entry():
	global choices
	sense_of_direction = 0
	
	while sense_of_direction == 0:
		choices = eg.enterbox("You enter an empty room. the walls are bare and the room itself is unfurnished.").lower()
		if choices == "look" or choices == "look around" or choices == "examine room" or choices == "examine":
			eg.msgbox("There are doors to the left and to the right of you. Nothing but a wall stands in front of you.")
			if "gun" in mysteryinv:
				pass
			else:
				eg.msgbox("On closer inspection, there appears to be a gun on the floor.")
		elif choices == "go left" or choices == "left" or choices == "west" or choices == "go west":
			if leftroomencounter == 1:
				sense_of_direction = 1
				leftroom2()
			else:
				sense_of_direction = 1
				leftroom()
		elif choices == "go right" or choices == "right" or choices == "east" or choices == "go east":
			sense_of_direction = 1
			rightroom()
		elif choices == "front" or choices == "forward" or choices == "go forward" or choices == "north" or choices == "middle":
			eg.msgbox("There's nothing but a wall in front of you. Despite that, you walk into it and bump your head.")
			eg.msgbox("Idiot.")
		elif choices == "pick up gun" or choices == "take gun" or choices == "gun":
			if "gun" in mysteryinv:
				eg.msgbox("You already took the gun.")
			else:
				eg.msgbox("Reluctantly picked up the gun. It has a strange aura surrounding it, you feel like you won't be able to take it with you outside of this room.")
				mysteryinv.append("gun")
		elif choices == "shoot self" or choices == "kill self" or choices == "suicide":
			if "gun" in mysteryinv:
				suicide()
			else:
				puzzled()
		elif choices == "go back" or choices == "back":
			sense_of_direction = 1
			do()
		elif choices == "help":
			eg.msgbox(mystery.info)
		elif choices == "leave":
			sense_of_direction = 1
			leaving()
		else:
			puzzled()
			entry()
def leftroom():
	global leftroomencounter
	if leftroomencounter == 1:
		leftroom2()
	else:
		choices = eg.enterbox("Wow, it's dark in here. Can't see a thing.")
		if choices == "look" or choices == "look around" or choices == "examine room" or choices == "examine":
			eg.msgbox("The whole room is pitch black. There's a light switch next to you, though.")
			leftroom()
		elif "light" in choices or "lightswitch" in choices or "lights" in choices:
			eg.msgbox("You flick the lightswitch on.")
			eg.msgbox("You turn around to look at the newly lit room and OH GOD THERE'S A MONSTER IN HERE")
			choices = eg.enterbox("Quick! What do you do?! Do you have any weapons on you?")
			if choices == "stab monster" or choices == "kill monster" or choices == "knife monster" or choices == "use knife on monster":
				if "knife" in room.grunnur.items:
					sense_of_direction = 1
					eg.msgbox("You equip your knife and start sprinting towards the monster.")
					eg.msgbox("Uh oh! He managed to grab you before you got around to stabbing him.")
					eg.msgbox("You contemplate life choices as you can feel your head being crushed by his massive hands. Maybe if you had a ranged weapon, you could have stood a chance.")
					eg.msgbox("Your body disintegrates and re-forms itself elsewhere...")
					do()
				else:
						eg.msgbox("You don't have a knife!")
						eg.msgbox("The monster rushes you while you think about what to eat for dinner.. Uh oh! He starts tearing you apart limb from limb. RIP.")
						eg.msgbox("Your body disintegrates and re-forms itself elsewhere...")
						do()
			elif choices == "throw knife" or choices == "throw knife at monster":
					if "knife" in room.grunnur.items:
						eg.msgbox("Huh. Guess that works too.")
						eg.msgbox("The knife lands right between the monsters' eyeballs! He plops down to the ground, dead.")
						leftroomencounter = 1
						leftroom2()
					else:
						eg.msgbox("You don't have a knife!")
						eg.msgbox("The monster rushes you while you think about what to eat for dinner.. Uh oh! He starts tearing you apart limb from limb. RIP.")
						eg.msgbox("Your body disintegrates and re-forms itself elsewhere...")
						do()
			elif choices == "shoot monster" or choices == "shoot" or choices == "gun":
				if "gun" in mysteryinv:
					eg.msgbox("Good thinking. You whip out your gun, do a 360 and headshot the monster. Take that!")
					eg.msgbox("The monster is very dead.")
					leftroomencounter = 1
					leftroom2()
				else:
					eg.msgbox("You don't even have a gun!")
					eg.msgbox("The monster rushes you while you think idiotic thoughts to yourself. Uh oh! There goes your head. He took your head.")
					eg.msgbox("Your body disintegrates and re-forms itself elsewhere...")
					do()
			elif choices == "go back" or choices == "back" or choices == "run away" or choices == "dodge" or choices == "leave":
				eg.msgbox("You try your best to run away, but to no avail. He catches you and immediately starts eating you. Yum!")
				eg.msgbox("Your torn body disintegrates and re-forms itself elsewhere...")
				do()
			else:
				puzzled()
				eg.msgbox("Looks like you took too long! He noticed you and has now started preparing some nefarious torture methods. Yikes!")
				eg.msgbox("You end up being drowned in boiling oil. At least you'll be a crispy treat!")
				eg.msgbox("Your crispy, yet tasty body disintegrates and re-forms itself elsewhere...")
				do()
		else:
			puzzled()
			leftroom()
def leftroom2():
	sense_of_direction = 0
	while sense_of_direction == 0:
		choices = eg.enterbox("You stand in a room with a dead monster.")
		if choices == "look" or choices == "look around" or choices == "examine room" or choices == "examine" or choices == "look monster" or choices == "look at monster" or choices == "examine monster":
			eg.msgbox("The monster lays on the ground, dead.")
			if "revolver" in room.grunnur.items:
				pass
			else:
				eg.msgbox("You see the barrel of what appears to be a revolver sticking out from underneath the monstrosity's body.")
		elif choices == "take gun" or choices == "take revolver" or choices == "gun" or choices == "pick up gun" or choices == "pick up revolver" or choices == "revolver":
			if "revolver" in room.grunnur.items:
				eg.msgbox("You've already taken the revolver.")
			else:
				room.grunnur.items.append("revolver")
				sense_of_direction = 1
				eg.msgbox("You pick up the revolver. Feels like nothing's restricting you from using it in other rooms!")
				eg.msgbox("Looks like there's nothing else to do in here, you go back to the previous room.")
				entry()
		elif choices == "go back" or choices == "back" or choices == "south":
			sense_of_direction = 1
			entry()
		elif choices == "leave":
			sense_of_direction = 1
			leaving()
		else:
			puzzled()
def rightroom():
	sense_of_direction = 0
	while sense_of_direction == 0:
		choices = eg.enterbox("This room looks very odd...").lower()
		if choices == "look" or choices == "look around" or choices == "examine room" or choices == "examine":
			eg.msgbox("This room, unlike the previous one, has a table in it. Other than that, it's also pretty much empty.")
			eg.msgbox("No doors other than the one you entered with, either.")
		elif choices == "go back" or choices == "back":
			sense_of_direction = 1
			entry()
		elif choices == "leave":
			leaving()
		elif choices == "look at table" or choices == "examine table" or choices == "look table" or choices == "table":
			eg.msgbox("You examine the table. It looks like there's a pair of modified dice on it. There's no 6 on these dice.")
			diceroll = eg.buttonbox("Roll the dice?", choices=["Yes","No"])
			if diceroll == "Yes":
				sense_of_direction = 1
				rolldice.roll()
			else:
				rightroom()
		else:
			puzzled()
def suicide():
	mysteryinv.remove("gun")
	eg.msgbox("You ready the gun, put it up to your head and shoot.")
	sleep(1)
	eg.msgbox("You get a weird feeling as your body disintegrates and re-forms itself elsewere...")
	sleep(0.3)
	do()
def puzzled():
	unknown = randint(1, 5)
	if unknown == 1:
		eg.msgbox("I do not know how to do that.")
	elif unknown == 2:
		eg.msgbox("What's that supposed to mean?")
	elif unknown == 3:
		eg.msgbox("Sorry, don't know what that's supposed to mean.")
	elif unknown == 4:
		eg.msgbox("That phrase isn't in my vocabulary.")
	elif unknown == 5:
		eg.msgbox("Sorry, didn't quite understand that.")