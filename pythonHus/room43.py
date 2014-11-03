# Halldór Jens Vilhjálmsson

from . import room
import random
import time

print("Du har indtastet værelse 43")
time.sleep(1)
print("Den første ting, du ser, er en skat trold fra Diablo 3")
time.sleep(1)

def goblinkamp():
	i = random.randrange(1,10)
	if i < 7:
		print("Du angriber og dræber nissen OG FEKKST X")
		respawn()
	else:
		print("Du angriber og dræber nissen en du fik ikke en dråbe!")
		print("Det vil respawn snart")
		time.sleep(15)
		respawn()

def respawn():
	print("Nissen er i live")
	svar = input("Ønsker du at angribe det? (ja/nej) ")
	if svar == "ja":
		goblinkamp()
	else:
		print("Oh alrigtig!")
		respawn()

respawn()