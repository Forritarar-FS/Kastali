from . import room
import random
import webbrowser
import turtle


def do():
	pass
	print ("Velkominn í Herbergi 31")
	do1();
	skapur();

def do1():
	lykill=0
	svar1 = input("Má bjóða þér að svara nokkrum einföldum spurningum?\n ")
	if(svar1[0]=='j'):
		svar2 = input("Hvað er 10 + 9?\n ")
		if(svar2=='19'):
			svar3 = input("Hvað er 71 + 3696?\n ")
			if(svar3=='3767'):
				svar4 = input("Hvað er 9299 + 8686?\n ")
				if(svar4=='17.985'):
					svar5 = input("Hvað er annað nafn Kristofers Breka?\n ")
					if(svar5=='Breki'):	
						webbrowser.open("http://www.clker.com/cliparts/R/3/A/t/s/n/olde-key-hi.png")
						lykill=lykill+1


def skapur():						
	print("Voo! Þú fannst lykill og fékkst aðgang að þessu herbergi!")
	print("Þú labbar inn í herbergið og þú sérð skáp og rúm")
	svarsvar1= input("Hvort viltu opna skápinn með lyklinnum eða kíkja undir rúmið?(opna skáp/undir rúm)")
	if(svarsvar1=='opna skáp'):
		breki = turtle.Turtle()
		breki.speed(10)
		for i in range(10):
			breki.forward(100)
			breki.right(30)
			breki.forward(20)
			breki.left(60)
			breki.forward(50)
			breki.right(30)

			breki.penup()
			breki.setposition(0, 0)
			breki.pendown()
			
			breki.right(2)
		turtle.bye()
		turtle.bye()
		svarsvar1=input("Jey! þú fannst hlutinn! labba út eða kíkja undir rúmið?(labba út/kíkja undir rúm")
		if svarsvar1=="labba út":
			pass

	if(svarsvar1=='kíkja undir rúm'):
		print("Þú gramsar undir rúminnu og finnur hlutinn úr herbergi 34!")


