from random import randint
from . import room
import easygui as eg
from time import sleep
dice1 = randint(1,5)
dice2 = randint(1,4)
dice3 = dice2 - 1
sdice1 = str(dice1)
sdice2 = str(dice2)
sdice3 = str(dice3)
roomteleport = int(sdice1 + sdice3)
def roll():
	eg.msgbox("The dice rolls...")
	sleep(0.4)
	eg.msgbox("The first dice's number:"+sdice1)
	sleep(0.4)
	eg.msgbox("The second dice's number:"+sdice2)
	sleep(0.5)
	eg.msgbox("You get a tingly feeling as your body starts evaporating!")
	sleep(0.5)
	eg.msgbox("Your body reforms itself at room "+sdice1+sdice2+"!")
	fyrirUtan = room.grunnur(roomteleport)
	fyrirUtan.go('e')