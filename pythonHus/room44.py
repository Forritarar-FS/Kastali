from . import room
from tkinter import *
def do():
	leid = room.grunnur(44)
	print("Velkominn í herbergi 44.")
	print("")
	svar = input("Viltu fara í annað herbergi? [j/n] ").lower()
	if(svar[0]=='j'):
		print("")
		herbVal = input("Í hvaða herbergi viltu fara: 43,34 eða 54? ")
		if(herbVal=="43"):
			leid.go("w")
		elif(herbVal=="34"):
			leid.go("n")
		elif(herbVal=="54"):
			print("Hurðinn er læst")
	elif(svar[0]=='n'):
		print("")
		print("Flott, þú horfir í kringum þig og sérð ekkert nema myndir á veggjunum.")
		print("Það er eitthvað skrítið við eina myndina svo þú labbar upp að henni og skoðar hana nánar")
		print("")
		cont = input("Ýttu á k til að halda áfram. ")
		if(cont[0]=='k'):
			master = Tk()

			w = Canvas(master, width=200, height=100)
			w.pack()

			w.create_line(0, 0, 200, 100)
			w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

			w.create_rectangle(50, 25, 150, 75, fill="blue")

			mainloop()

			
			print("")
			cont2 = input("Ýttu á k til að halda áfram. ")
			if(cont2[0]=='k'):
				print("")
				print("Farðu inn í annað herbergi!")
				print("")
				herbVal2 = input("Í hvaða herbergi viltu fara: 43,34 eða 54? ")
				if(herbVal2=="43"):
					leid.go("w")
				elif(herbVal2=="34"):
					leid.go("n")
				elif(herbVal2=="54"):
					print("Hurðinn er læst")