from . import room

def do():
	leid = room.grunnur(44)
	print("Velkominn í herbergi 44.")
	print("")
	svar = input("Viltu fara í annað herbergi? [Y/N] ").lower()
	if(svar[0]=='y'):
		print("")
		herbVal = input("Viltu fara í herbergi: 43,34 eða 54?")
		if(herbVal=="43"):
			leid.go("w")
		elif(herbVal=="34"):
			leid.go("n")
		elif(herbVal=="54"):
			leid.go("s")
	elif(svar[0]=='n')
		