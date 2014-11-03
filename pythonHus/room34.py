from . import room
import turtle

def do():
	pass
	print ("Velkominn í herbergi 34!")

	step = 1000
	length = 100
	angle = 50    
	turtle.speed(50)
	def drawSquare(length,turn):
		for i in range (0,step):
			for b in range (0,2):
				turtle.forward(length+i*2)
				turtle.right(angle+b)
		for i in range (0,step):
			for b in range (0,2):
				turtle.forward(length+i*2)
				turtle.left(angle+b)
		sleep(10) 
	drawSquare(5,10)
