from . import room

def do():
	mystery = room.grunnur(14)
	mystery.info = "Something doesn't seem quite right here..."
	print("You stand in front of the Room of Mystery")
	reply = input("Do you go in?")
	if reply == "yes":
		print("you get mystified")
	else:
		o = 1
		while o == 1:	
			direction = input("Where do you wish to go?")
			if direction == "north":
				print("You can not go North!")
			elif direction == "east":
				print("You can not go East!")
			elif direction == "south":
				o = 0
				mystery.go("s")
			else:
				o = 0
				mystery.go("w")
