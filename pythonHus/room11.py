from . import room
import os
import sys
import turtle


print ("Welcome to Room 11. Shall we begin. (y/n)")
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])

choice = input().lower()

def do():	
	if choice in yes:
		print ("Good choice")
		return True
	elif choice in no:
		print ("Too bad, We're starting anyways...")
		return True
	else:
		sys.stdout.write("Please respond with 'yes' or 'no'")




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

turt.begin_fill()
turt.fillcolor('yellow')
for i in range(25):
	turt.forward(125)
	turt.right(75)

turt.end_fill()

turt.color('blue')
turt.right(15)
turt.forward(150)

wn.mainloop()