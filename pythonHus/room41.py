from . import room


def do():
	th = room.grunnur(41)
	print ("Velkomin/nn í herbergið mitt :)")

import turtle
wn = turtle.Screen()
wn.bgcolor("black")
ræfill = turtle.Turtle()
ræfill.color("green")
ræfill.right(90)
ræfill.left(3600)
ræfill.right(-90)
ræfill.speed(10)
ræfill.left(3600)
ræfill.speed(0)
ræfill.left(3645)
ræfill.forward(-100)      

wn.mainloop()


	#svar = input("Villtu fara inn í kastalann").lower()
	#fyrirUtan = room.grunnur(52)
	#fyrirUtan.info = "ERROR!!!, ERROR!!!, Can not compute...."
	#if(svar[0]=='j' or svar[0]=='y'):
		#fyrirUtan.go('n')
	#else:
		#raise ValueError(fyritUtan.info)