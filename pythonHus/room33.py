import os
from . import room
from time import sleep
import easygui as eg
import sys
revolver = "Byssa frá öðru herbergi"
fyrirUtan = room.grunnur(33)
fyrirUtan.info = "Ef þú gast ýtt á þetta þá getur þú alveg ýtt á hina takkana líka."

def check4eg():
	got_thing = False
	x = 30
	while x < 40:
		path = "C:\Python"+ str(x) +"\Lib\site-packages\easygui.py" #credit Hlynur
		path2 = "C:\Python"+ str(x) +"\Lib\easygui.py"
		cool = os.path.exists(path)
		cool2 = os.path.exists(path2)
		print(path)
		if cool == False and cool2 == False:
			print ()
		else:
			got_thing = True
		x += 1
	if got_thing == False:
		easy = input("Are you sure you have Easygui installed?  Y/N").lower()
		if easy == "y" or easy == "yes":
			pass
		else:
			print("You should install it before entering the room")
			leaveWOeg()
def leaveWOeg():
		directionQ = input("Where do you want to go? (west, north, South, east)").lower()
		if directionQ == "w" or directionQ == "west":
				fyrirUtan.go("w")       #credit Hlynur
		elif directionQ == "north" or directionQ == "n":
				fyrirUtan.go("n")
		elif directionQ == "south" or directionQ == "s":
				fyrirUtan.go("s")
		elif directionQ == "east" or directionQ == "e":
				fyrirUtan.go("e")
		else:
				leaveWOeg()
check4eg()

def do():
	eg.msgbox("Þú gengur inn í herbergi sem virðist tómt.")
	choosing1()

def choosing1():
	msg1 ="Hvað vilt þú gera?"
	title1 = " "
	choices1 = ["Byrja að syngja 'Walking on Sunshine'", "Skoða herbergið nánar", "Ekkert", "!HJÁLP!"]
	choice1 = eg.choicebox(msg1, title1, choices1)

	if choice1 == "Byrja að syngja 'Walking on Sunshine'":
		eg.msgbox("Þú byrjar að syngja og heyrir eitthvað hljóð frá einu horni herbergisins")
		eg.msgbox('"Umm... er einhver leið að fá þig til að hætta?"')
		spookyGhost()
	elif choice1 == "Skoða herbergið nánar":
		eg.msgbox("Þú lítur nánar í kringum herbergið og sérð eitthvað fljótandi í einu horninu.")
		eg.msgbox("Þú ferð beint upp við hvað sem það er...")
		sleep(3)
		eg.msgbox('"Gaur, þú ert sko alveg BEINT framan í mér. Gætirðu fært þig?"')
		spookyGhost()
	elif choice1 == "Ekkert":
		eg.msgbox("Þú stendur á sama stað og starir bara á vegginn. Spennandi.")
		eg.msgbox('"Er, umm... er allt í lagi með þig? Ha, kallin, ertu ennþá með okkur hérna?"')
		spookyGhost()
	else:
		eg.msgbox(fyrirUtan.info)
		choosing1()

def spookyGhost():
	eg.msgbox('"Já, ókei, flott, hæ. Ég er draugur falskra leikmanna-valmöguleika. Ég er með prik sem þú mátt fá, viltu?"')
	if revolver in room.grunnur.items:
		eg.msgbox('"Óh, flott byssa."')
		choosing2()
	else:
		choosing2()

def choosing2():
	msg2 = "Tekur þú við prikinu?"
	title2 = ""
	choices2 = ["Já", "Nei", "!HJÁLP!"]
	choice2 = eg.choicebox(msg2, title2, choices2)

	if choice2 == "Já":
		eg.msgbox('"Frábært, glæsilegt, hérna."')
		stickGet()
	elif choice2 == "Nei":
		eg.msgbox('"Jú, svona, taktu bara prikið"')
		stickGet()
	else:
		eg.msgbox(fyrirUtan.info)
		choosing2()

def stickGet():
	StickOfSlightConvenience = "Mögulega glæsilegasta prik sem þú hefur einhvern tíman séð... samt bara prik, svo ekkert rosalegt."
	room.grunnur.items.append(StickOfSlightConvenience)
	goAway()

def goAway():
	eg.msgbox('"Heyrðu, ég er eiginlega orðinn svoldið þreyttur á þér svo... þú veist, farðu. Ég skal í alvörunni leyfa þér að velja núna."')
	choosing3()

def choosing3():
	msg3 = "Hvert viltu fara?"
	title3 = ""
	choices3 = ["Norður", "Vestur", "Austur", "Suður", "!HJÁLP!"]
	choice3 = eg.choicebox(msg3, title3, choices3)

	if choice3 == "Vestur":
		fyrirUtan.go("w")
	elif choice3 == "Norður":
		fyrirUtan.go("n")
	elif choice3 == "Suður":
		fyrirUtan.go("s")
	elif choice3 == "Austur":
		fyrirUtan.go("e")
	else:
		eg.msgbox(fyrirUtan.info)
		choosing3()
do()