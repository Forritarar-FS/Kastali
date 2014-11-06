# Halldór Jens Vilhjálmsson

from . import room
import random
import time
import turtle
import os

# Brotinn Lykill og Brotinn Lykill(43) Sun Cream -> Eidur

print("You are in room 43!")
time.sleep(1)
print("The first thing you see is a Treasure Goblin from Diablo 3")
room.grunnur.items.append(["Sun Cream"])
print("YOU HAVE OBTAINED SUN CREAM, PLEASE VISIT ROOM 11 LATER!")
time.sleep(1)

def turtledrawing():
	wn = turtle.Screen()
	wn.bgcolor('black')
	chestTurtle = turtle.Turtle()
	chestTurtle.begin_fill()
	chestTurtle.fillcolor('red')
	for i in range(10):
		chestTurtle.forward(50)
		chestTurtle.right(144)
	chestTurtle.end_fill()
	wn.mainloop()

def exitFunction():
	fyrirUtan = room.grunnur(43)
	fyrirUtan.info = "You've broken the system, congratulations!"
	y = input("Do you want to exit room 43?").lower()
	if y[0] in ['y', 'j']:
		i = input("Which direction do you want to head? (n,s,w,e)").lower()
		fyrirUtan.go(i[0])
	else:
		raise ValueError(fyrirUtan.info)

def do():
	print(room.grunnur.items)
	if ["DUCT TAPE(12)"] in room.grunnur.items:
		print("You see a locked chest in the corner of the room.")
		i = input("Do you want to open it?")
		if i[0] in ['y', 'j']:
			if ["Brotinn Lykill"] in room.grunnur.items:
				if ["Brotinn Lykill(43)"] in room.grunnur.items:
					print("You found a drawing!")
					room.grunnur.items.append(["MONOLIZAPAINTING"])
					x = input("Do you want to see your inventory?")
					if x[0] in ['y', 'j']:
						print(room.grunnur.items)
						turtledrawing()
				else:
					print("You need the other keypiece")
					exitFunction()
			else:
				print("You need both keypieces to open this chest!")
				exitFunction()
		else:
			print("Wat")
			exitFunction()
	else:
		respawn()
def goblinkamp():
	i = random.randrange(1,10)
	if i < 7:
		print("You kill the goblin and recieve DUCT TAPE")
		room.grunnur.items.append(["DUCT TAPE(12)"])
		do()
	else:
		os.system('cls')
		print("You kill the goblin but get no loot")
		print("The goblin will respawn soon")
		time.sleep(5)
		respawn()

def respawn():
	print("The goblin has spawned")
	svar = input("Do you want to kill it? (y/n) ")
	if svar[0] in ['y', 'j']:
		goblinkamp()
	else:
		print("OK")
		exitFunction()

respawn()