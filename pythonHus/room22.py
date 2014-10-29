from . import room
import easygui as eg
from time import sleep

def do():
	Enter = eg.ynbox(msg='There is a deep dark hole in the ground. Should you jump into it?', title='22')
	if Enter == 1:
		eg.msgbox("You jump in the hole.", ok_button="Continue")
		sleep(2)
		eg.msgbox("You are falling...", ok_button="Continue")
		sleep(2)
		eg.msgbox("It takes you 5 seconds to fall to your death.", ok_button="Shit")
		exit()
		#FUCKING TERMINATE THE PROGRAM HERE LATER HLYNUR.
		print("it no work")
	else:
		eg.msgbox("Good thing you are sane.", ok_button="Continue")
		eg.msgbox("You continue on to the room.", ok_button="Continue")
	
	

