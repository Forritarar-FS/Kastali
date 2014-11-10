# EIDUR GEIR VILHELMSSON

from . import room
import os
import sys
import turtle
import time


print ("You've aquired a broken key, Go to room 43 to reforge it idk man, do do somethin' wit it..")
time.sleep(2)
print ("Also go to room 43 and get my Sun Cream, It's hot in here!")
time.sleep(2)
print ("Welcome to Room 11. Shall we begin. (y/n)")
yes = set(['yes','y', 'ye', 'ja', 'j', ''])
no = set(['no','n', 'nope', 'neibb', 'nei', 'als ekki', 'aldrei', 'nope'])


room.grunnur.items.append('Sun Cream')
choice = input(">>> ").lower()

def do():	
	if choice in yes:
		cream()
	elif choice in no:
		print ("Too bad, We're starting anyways...")
		cream()
	else:
		sys.stdout.write("Please respond with 'yes' or 'no'")

def cream():
	if 'Sun Cream' in room.grunnur.items:
		print ("Let me check yo' shit...")
		time.sleep(2)
		print ("Cool You got my Sun Cream, Now lube your body with my sweetness before you go in.")
		time.sleep(3)
		turtlewn()
	else: 
		print ("Let me check yo' shit...")
		time.sleep(2)
		sys.stdout.write("You don't have my Sun Cream... gtfo")
		exitOnFail()



def turtlewn():
	# Turtle Animation Start
	wn = turtle.Screen()
	wn.bgcolor('blue')
	turt = turtle.Turtle()
	turt.color('blue')
	turt.hideturtle()
	turt.left(90)
	turt.forward(250)
	turt.right(90)
	turt.forward(150)
	turt.color('yellow')

	# Sun Color Fill and Animation
	turt.begin_fill()
	turt.fillcolor('yellow')
	for i in range(25):
		turt.forward(125)
		turt.right(75)

	turt.end_fill()

	# Turtle travel for grass.
	turt.color('yellow')
	turt.right(15)
	turt.forward(165)
	turt.color('blue')
	turt.forward(1125)
	turt.color('green')


	# Grass Color Fill
	turt.begin_fill()
	turt.fillcolor('green')

	# Grass animation
	turt.left(90)
	turt.forward(150)

	# Grass Box
	for x in range(3):
		turt.left(90)
		turt.forward(850)

	turt.end_fill()
	wn.mainloop()
	exitFunc()

def exitFunc():
	svar = input("Transaction Complete, Leave room?").lower()
	fyrirUtan = room.grunnur(11)
	fyrirUtan.info = "ERROR!!!, ERROR!!!, Can not compute...."
	if svar[0] in ['j', 'y']:
		fyrirUtan.go('s')
	else:
		raise ValueError(fyritUtan.info)


def exitOnFail():
	svar = input("Transaction Incomplete, Leave this room?").lower()
	fyrirUtan = room.grunnur(11)
	fyrirUtan.info = "ERROR!!!, ERROR!!!, Can not compute...."
	if svar[0] in ['j', 'y']:
		fyrirUtan.go('s')
	else:
		raise ValueError(fyritUtan.info)