from . import room
import easygui as eg
from time import sleep
from random import randint

def fall():
	random1 = randint(1,5)
	if random1 == 5:
		random2 = randint(1,2)
		if random2 == 2:
			random2 = 4
		else:
			pass
	else:
		random2 = randint(1,4)
	Roomminus10 = random1 * 10
	Roomminus10 = Roomminus10 + random2
	Roomminus10 = Roomminus10 - 10
	random1S = str(random1)
	random2S = str(random2)
	eg.msgbox("you suddenly find yourself in  room" + random1S +random2S)
	sleep(0.5)
	print (Roomminus10)
	fyrirUtan = room.grunnur(Roomminus10)
	fyrirUtan.go("s")





def BDoor(roomFrom):
	eg.msgbox("You enter a room with multiple doors.")
	Doors = ["Back", "Door 33","Door 14"]
	WhatDoor = eg.buttonbox("They all have numbers on them", choices=Doors)
	if WhatDoor == "Back":
		eg.msgbox("You went back")
		pass
	elif WhatDoor == "Door 33":
		eg.msgbox("You opened door number 33")
		fyrirUtan = room.grunnur(23)
		fyrirUtan.do("s")
	elif WhatDoor == "Door 14":
		eg.msgbox("You opened door number 14")
		fyrirUtan = room.grunnur(4)
		fyrirUtan.do("s")
	else:
		print("This code will never run away.")


