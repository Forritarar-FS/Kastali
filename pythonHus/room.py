class grunnur():
	fra = 0 #segir hvaða herbergi notandinn úr
	items = [] #Ef þið viljið að notandinn finni einhverja hluti í herberginu ykkar
	def __init__(self, herbergi):
		self.nr = herbergi #Segir í hvaða herbergi ég er, setjið þetta inn þegar þið eintakið klasann
		self.info = "Það á enn eftir að skrifa upplýsingar um þetta herbergi" #Til þess að skrifa in upplýsingar um hegbergið ykkar eða leiðbeiningar til notandans
	def help(self):
		print(self.info) #prentar út upplýsingarnar eða leiðbeiningarnar
	def go(self, direction): #n = north, e = east, s = south, w = west
		
		if (direction in [ 'n', 'e', 's', 'w']):
			att = {
				'n': -10,
				'e': 1,
				's': 10,
				'w': -1 
				}
			grunnur.fra = att[direction] + self.nr
			exec("import pythonHus.room"+ str(grunnur.fra))
			eval("pythonHus.room"+ str(grunnur.fra)+ ".do()")
		else:
			raise SyntaxError("Það er ekki hægt að velja " + direction + " sem átt")


