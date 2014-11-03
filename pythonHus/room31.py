from . import room
import turtle
from tkinter import *
import random
turtle.speed(10)

def hexagon(angle,size):
 
	angle=60	
 
	for i in range(6):
 
		turtle.forward(size)
 
		turtle.left(angle)
 
 
 
def drawing(size):
 
	for i in range(6):
 
		print(hexagon(60,size))
 
		turtle.left(60)
 
 
 
while(1):
 
	print (drawing(random.randint(40,100)))
 
	turtle.color(random.randint(0,1),random.randint(0,1),random.randint(0,1))
 
	turtle.width(random.randint(0,3))
 
 
 
turtle.exitonclick()

def do():
	pass
	print ("This is Room 31!")