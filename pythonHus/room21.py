from . import room

import turtle
def do():
	th =room.grunnur(21)
	print("Velkominn í herbergi 21!  ")
	sweg =input('Viltu koma inní herbergið mitt? j/n  ')
	if sweg == "j" or sweg == "n":
		print("Velkominn \n      ")
	siggi = input("Hvað er 1+1?  ")
	if siggi == '2':
		for i in range(45):
			turtle.speed(11)
			turtle.circle(150)
			turtle.left(8)
		turtle.left(4)
		for h in range(45):
			turtle.speed(75)
			turtle.circle(150)
			turtle.left(8)
		turtle.left(2)
		for i in range(45):
			turtle.speed(75)
			turtle.circle(150)
			turtle.left(8)

		turtle.done()
	else:
		for i in range(50):
			print("Hálviti!")



