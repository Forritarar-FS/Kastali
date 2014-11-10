from . import room
import turtle
import time
import tkinter
from tkinter import messagebox
import webbrowser
import turtle
Inventory = ()

def do():
	th = room.grunnur(13)
	print("Velkominn í Herbergi 13.\n")
	time.sleep(2)
	print("Þú ert á fyrstu hæðinni.\n")
	time.sleep(2)
	print("Það eru þrjár hæðir í heild.\n")
	time.sleep(2)
	print("Þegar þú ferð á aðra hæðina byrjar völundarhúsið\n")
	time.sleep(2)
	swag = input("Viltu klifra upp stigan?\n")
	sweg = swag.lower()
	if sweg == 'já' or 'j' or 'y' or 'yes':
		turtle.speed(200)
		turtle.left(90)
		turtle.forward(400)
		turtle.left(180)
		turtle.forward(800)
		turtle.left(180)
		turtle.forward(20)
		for i in range(40):
			turtle.right(90)
			turtle.forward(70)
			turtle.left(90)
			turtle.forward(20)
			turtle.left(90)
			turtle.forward(70)
			turtle.right(90)
		turtle.right(360)
		turtle.bye()
		print("\nVelkominn í völundarhúsið\n")
		time.sleep(3)
		
	else:
		swaggy = input("Then where do you want to go?")