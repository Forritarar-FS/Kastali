from . import room


def do():
	svar = input("Villtu fara inn í kastalann").lower()
	fyrirUtan = room.grunnur(52)
	fyrirUtan.info = "ERROR!!!, ERROR!!!, Can not compute...."
	if(svar[0]=='j' or svar[0]=='y'):
		fyrirUtan.go('n')
	else:
		raise ValueError(fyritUtan.info)
