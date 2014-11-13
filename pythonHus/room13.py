import turtle
import time
from tkinter import *
import tkinter.messagebox
import webbrowser
import turtle
text = "What is it?"
mechanic = ""
swurgur = "sunshine.png"
niggy = "sunnyday.png"
naggy = "sunnycat.png"
print("Velkominn í Herbergi 13.\n")
time.sleep(2)
print("Þú ert á fyrstu hæðinni.\n")
time.sleep(2)
print("Það eru þrjár hæðir í heild.\n")
time.sleep(2)
print("Þegar þú ferð á aðra hæðina byrjar völundarhúsið\n")
time.sleep(2)
swag = input("Viltu klifra upp stigan?\n")
sweg = swag.lower()
if sweg == 'já' or 'j' or 'y' or 'yes':
	turtle.speed(200)
	turtle.left(90)
	turtle.forward(400)
	turtle.left(180)
	turtle.forward(800)
	turtle.left(180)
	turtle.forward(20)
	for i in range(40):
		turtle.right(90)
		turtle.forward(70)
		turtle.left(90)
		turtle.forward(20)
		turtle.left(90)
		turtle.forward(70)
		turtle.right(90)
		turtle.right(360)
	turtle.bye()
	print("\nVelkominn í völundarhúsið\n")
	time.sleep(3)
	top = Tk()
	def DaStar():
		if mechanic == "open":
			golden = messagebox.askquestion( 'k', 'Það er stytta og kött úr skýra gulli, viltu taka hana?')
			if golden == 'yes':
				room.grunnur.items.append('Gullni Kötturinn')
			else:
				background_label.grid(row=2, column=2)
				B.grid(row=1, column=1)
				G.grid(row=1, column=2)
				C.grid(row=1, column=3)
		else:
			messagebox.askquestion( 'k', 'Þú þarft að opna fyrir lásinn í herbergi styrks')
			top = tkinter.Tk()
		pass
	def DaStrength():
		if "Skrítinn bolti" in room.grunnur.items:
			background_label.grid_forget()
			B.grid_forget()
			G.grid_forget()
			C.grid_forget()
			danger = messagebox.askquestion( 'k', 'þú sérð takka, viltu ýta á hann?')
			if danger == 'yes':
				messagebox.showinfo( 'k', 'þú heyrir hljóð eins og lás að opnast')
				global mechanic
				mechanic = "open"
				background_label.grid(row=2, column=2)
				B.grid(row=1, column=1)
				G.grid(row=1, column=2)
				C.grid(row=1, column=3)
			else:
				messagebox.showinfo( 'k', 'Þér vantar skrítna boltann úr herbergi 21')
				background_label.grid(row=2, column=2)
				B.grid(row=1, column=1)
				G.grid(row=1, column=2)
				C.grid(row=1, column=3)
			top = tkinter.Tk()
			
	def DaSorrow():
		window.destroy()
		ilikepie = input('viltu fara vestur, austur, norður eða suður?')
		if ilikepie == "vestur" or "v":
			room.grunnur[12]
		elif ilikepie == "austur" or "a":
			room.grunnur[14]
		elif ilikepie == "suður" or "s":
			room.grunnur[23]
		elif ilikepie == "norður" or "n":
			print('það er ekkert herbergi í þessa átt')
		else:
			print('veldu vestur, austur, norður eða suður')



			

	B = Button(top, text ="Enter", command=DaStrength)
	G = Button(top, text ="Enter", command=DaStar)
	C = Button(top, text ="Enter", command=DaSorrow)
	background_image=PhotoImage(file=swurgur)
	background_label = Label(image=background_image)
	background_label.photo = background_image
	background_label.grid(row=2, column=2)


	B.grid(row=1, column=1)
	G.grid(row=1, column=2)
	C.grid(row=1, column=3)
	top.mainloop()
else:
	ilikefly = input('viltu fara vestur, austur, norður eða suður?')
		if ilikefly == "vestur" or "v":
			room.grunnur[12]
		elif ilikefly == "austur" or "a":
			room.grunnur[14]
		elif ilikefly == "suður" or "s":
			room.grunnur[23]
		elif ilikefly == "norður" or "n":
			print('það er ekkert herbergi í þessa átt')
		else:
			print('veldu vestur, austur, norður eða suður')