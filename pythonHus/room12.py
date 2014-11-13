import . from room

print ("Velkomin!")

def do():
	th = room.grunnur(12)
	th.go('n')
	print("Þú ert í  herbergi 12!")
	hlutur = input("Hér getur þú fundið Brotin Lykil merktur 43 vill þú taka hann?").lower()
	if (hlutur[0]==('j') or hlutur[0]==('y')):
		grunnur.items.append(['Brotin Lykil(43)'])
		print('Þú hefur tekið Lykilin')
	else:
		print ('Allt í lægi hann verður hér ef þér sníst hugur')
	hlutur2 = input('það er kista í horninu á herberginu viltu kíkja i hanna?').lower()
	if (hlutur2[0]==('j') or hlutur2[0]==('y')):
		print('þú opnar kistuna og finnur þar skó.')
		skór = input("Viltu taka skóna? ").lower
		if(skór[0]==('j') or skór[0]==('y')):
			print('þú tókst skóna')
			grunnur.items.append(['skór'])
		else:
			print ('Þú lokar kistuni án þess að taka skóna.')
	else:
		print('það er öruglega cool hlutir þarna en alltílægi')	
	pass
