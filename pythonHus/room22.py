import os
from . import room
def do():
    got_thing = False
    x = 30
    while x < 40:
        path = "C:\Python"+ str(x) +"\Lib\site-packages\easygui.py" #credit Hlynur
        path2 = "C:\Python"+ str(x) +"\Lib\easygui.py"
        cool = os.path.exists(path)
        cool2 = os.path.exists(path2)
        print(path)
        if cool == False and cool2 == False:
            print (x)
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
		fyrirUtan.go("w")	#credit Hlynur
	elif directionQ == "north" or directionQ == "n":
		fyrirUtan.go("n")
	elif directionQ == "south" or directionQ == "s":
		fyrirUtan.go("s")
	elif directionQ == "east" or directionQ == "e":
		fyrirUtan.go("e")
	else:
		leaveWOeg()
do()

import easygui as eg
import os
import time
from . import Basement
from random import randint
Monster_Alive = True
Alive = True
Damage = 0
Enemy_damage = 0
dead = False
Darkness = 0
steps = 0
 
DownChoice = ["Pick up knife","Open door", "Go towards the hole","Go back"]
fyrirUtan = room.grunnur(22)
fyrirUtan.info = "This looks fancy. I guess."
 
def dodo():
    eg.msgbox("Warning this room is incomplete! Check back soon for updates and fixes!")
    if dead == False:
        print("its true")
    elif dead == True:
        eg.msgbox("You feel darkness. You feel as you should not enter")
        print("Its false")
    else:
        pass
    enterQ = eg.ynbox("Do you want to enter?")
    if enterQ == 1:
        eg.msgbox("You continue on to the room.", ok_button="Continue", title=fyrirUtan.info)
        eg.msgbox("You open a large door.", ok_button="Continue", title=fyrirUtan.info)
        eg.msgbox("(Door opening sounds)", ok_button="Continue", title=fyrirUtan.info)
        mainRoom()
    else:
        eg.msgbox("Fine Then", ok_button="Continue", title=fyrirUtan.info)
        leave()
 
def mainRoom():
    updownmiddle = ["Down","Front","Up"]
    way = eg.buttonbox("You see 3 doors. One leading UP, one leading DOWN to the basement and one to the FRONT", choices=updownmiddle, title=fyrirUtan.info)
    if way == "Down":
        Down()
    if way == "Front":
        Middle()
    if way == "Up":
        Up()
 
def dead():
	dead = True
 
 
 
def leave():
	direction = ["West", "North", "South", "East"]
	directionQ = eg.buttonbox("Where do you want to go?", choices=direction)
	if directionQ == "West":
		fyrirUtan.go("w")
	elif directionQ == "North":
		fyrirUtan.go("n")
	elif directionQ == "South":
		fyrirUtan.go("s")
	else:
		fyrirUtan.go("e")



def Down():
    def downchoiceFunc():
        if "torch" in fyrirUtan.items:
            knifedoorhole = eg.buttonbox("You see a Knife, a door and a hole in the ground.", choices=DownChoice, title=fyrirUtan.info)
            if  knifedoorhole == "Pick up knife":
                eg.msgbox("You put the knife into your pocket", title=fyrirUtan.info)
                fyrirUtan.items.append("knife")
                del DownChoice[0]
                downchoiceFunc()
            elif knifedoorhole == "Open door":
                Basement.BDoor(22)
            elif knifedoorhole == "Go towards the hole":
                eg.msgbox("You walk to the hole and look down it.", title=fyrirUtan.info)
                time.sleep(0.5)
                eg.msgbox("You see light at the bottom. Looks safe enough to jump.", title=fyrirUtan.info)
                if  eg.ynbox("Jump in the hole?", title=fyrirUtan.info) == 1:
                    Basement.fall()
                else:
                    eg.msgbox("You decide not to jump", title=fyrirUtan.info)
                    downchoiceFunc()
            elif knifedoorhole == "Go back":
                eg.msgbox("You whent back up.", title=fyrirUtan.info)
                mainRoom()
 
            else:
                eg.msgbox("It sure is dar...", title=fyrirUtan.info)
                eg.msgbox("SHIT!", title=fyrirUtan.info)
                eg.msgbox("You fell into a hole.", title=fyrirUtan.info)
                time.sleep(0.75)
                Basement.fall()
    eg.msgbox("You walk down the stairs and open the door.", title=fyrirUtan.info)
    eg.msgbox("You walk into a dark room. There is a lit torch on the wall.", title=fyrirUtan.info)
    print (fyrirUtan.items)
    if "torch" not in fyrirUtan.items:
        if eg.ynbox("Do you want to take the torch?", title=fyrirUtan.info) == 1:
            eg.msgbox("You take it up", title=fyrirUtan.info)
            fyrirUtan.items.append("torch")
            if eg.ynbox("Do you want to go deeper?", title=fyrirUtan.info) == 1:
                eg.msgbox("You go in deeper", title=fyrirUtan.info)
                downchoiceFunc()
            else:
              eg.msgbox("You go back up.", title=fyrirUtan.info)
              mainRoom()	
        else:
            eg.msgbox("It sure is dark in here.", title=fyrirUtan.info)
    else:
        pass

 
def Middle():
    def Attack():
        global Monster_Alive
        global Alive
        global Damage
        global Enemy_damage
        while Damage < 5 and Enemy_damage < 7:
            def counter_Attack():
                global Damage
                global Enemy_damage
                counter_attack_Direction = randint(1,3)
                CA_Direction = ("Attack Left!", "Attack Middle!", "Attack Right!")
                if counter_attack_Direction == 1:
                    vulnerable = "Left"
                elif counter_attack_Direction == 2:
                    vulnerable = "Middle"
                else:
                    vulnerable = "Right"
                start_time = time.time()
                Counter_Attack = eg.buttonbox("The monster is vulnerable to attack from the "+ vulnerable +"!", choices=CA_Direction, title=fyrirUtan.info)
                total_time =time.time() - start_time
                print (total_time)
                print (vulnerable)
                print (Counter_Attack)
                if Counter_Attack == "Attack Left!" and vulnerable == "Left":
                    Enemy_Hit()
                elif Counter_Attack == "Attack Middle!" and vulnerable == "Middle":
                    Enemy_Hit()
                elif Counter_Attack == "Attack Right!" and vulnerable == "Right":
                    Enemy_Hit()
                     
                else:
                    eg.msgbox("You missed and the monster regained his strength!", title=fyrirUtan.info)
 
            def Enemy_Hit():
                global Enemy_damage
                if total_time < AttackTime:
                    eg.msgbox("You Attacked and hit the monster!", title=fyrirUtan.info)
                    Enemy_damage += 1
                    status("enemy")
                else:
                    eg.msgbox("You took too long so the monster regained his strength!", title=fyrirUtan.info)
 
            def status(damage):
                global Damage
                global Enemy_damage
                print (Damage)
                if damage == "enemy":
                    if damage == 1:
                        eg.msgbox("The monster barely flinches", title=fyrirUtan.info)
                    elif Enemy_damage == 3:
                        eg.msgbox("The monster shows signs of pain", title=fyrirUtan.info)
                    elif Enemy_damage == 5:
                        eg.msgbox("The monster is severly brused and is showing signs of major pain", title=fyrirUtan.info)
                    elif Enemy_damage == 7:
                        eg.msgbox("The monster fell down on its knees, looks up, then falls on his side.", title=fyrirUtan.info)
                        eg.msgbox("Breathing a few final breaths it finally gave up and exhaled slowly.", title=fyrirUtan.info)
                    else:
                        pass
                else:
                    print("Ran")
                    if Damage == 1:
                        eg.msgbox("My face got scratched up!", title=fyrirUtan.info)
                    elif Damage == 2:
                        eg.msgbox("I can feel the warmth of blood running along my clothes", title=fyrirUtan.info)
                    elif Damage == 4:
                        eg.msgbox("I can feel myself fading in and out. I can hear my blood dripping on the ground...", title=fyrirUtan.info)
                    elif Damage ==5:
                        eg.msgbox("The Pain is leaving. My Feelings are leaving...", title=fyrirUtan.info)
                        eg.msgbox("The light is dark.", title=fyrirUtan.info)
                        eg.msgbox("I am leaving.", title=fyrirUtan.info)
 
                        #finish here sometime
 
            leftright = ("Move Left", "Move Right")
            AttackType = randint(1,2);
            if AttackType == 1:
                AttackType = "Left"
            else:
                AttackType = "Right"
            AttackTime = 2
            start_time = time.time()
            dodge = eg.buttonbox("It looks like its about to attack from the "+AttackType.upper(), choices=leftright, title=fyrirUtan.info)
            total_time = time.time() - start_time
            print(Enemy_damage)
            print(Damage)
            if total_time < AttackTime:
                if dodge == "Move Left" and AttackType == "Left":
                    eg.msgbox("The monster hit you!", title=fyrirUtan.info)
                    Damage+=1
                    status("")
                elif dodge == "Move Right" and AttackType == "Right":
                    eg.msgbox("The monster hit you!", title=fyrirUtan.info)
                    Damage+=1
                    status("")
                else:
                    eg.msgbox("You dodged", title=fyrirUtan.info)
                    chance = randint(1,3)
                    if chance == 1:
                        Counter_Attack = counter_Attack()
            else:
                eg.msgbox("You took too long so the monster hit you!", title=fyrirUtan.info)
                Damage+=1
                status("")
        if Enemy_damage < 7:
            pass
        else:
            eg.msgbox("You notice a key on a string around the monsters neck.", title=fyrirUtan.info)
            eg.msgbox("You picked up the key", title=fyrirUtan.info)
            eg.msgbox("You leave the room leaving the monster laying on the ground.", title=fyrirUtan.info)
            fyrirUtan.items.append("Key22")
            mainRoom()
    if Enemy_damage == 7 or Damage == 5:
        eg.msgbox("The monster lies on the floor. Dead.", title=fyrirUtan.info)
        mainRoom()
    else:
        eg.msgbox("You enter a empty room.", title=fyrirUtan.info)
        eg.msgbox("You hear something.", title=fyrirUtan.info)
        eg.msgbox("It is a monster!", title=fyrirUtan.info)
        if "torch" in fyrirUtan.items:
            eg.msgbox("You drop the torch you were holding.", title=fyrirUtan.info)
        else:
            pass
        eg.msgbox("It attacks!", title=fyrirUtan.info)
        Attack()
 
def Up():
    def main():
        eg.msgbox("You go up the stairs.", title=fyrirUtan.info)



        fyrirUtan.items.append("Key22")
        fyrirUtan.items.append("torch")


        eg.msgbox("The door is locked. ", title=fyrirUtan.info)
        print(fyrirUtan.items)
        if "Key22" in fyrirUtan.items:
            eg.msgbox("You try the key.", title=fyrirUtan.info)
            eg.msgbox("it fits perfectly and the door opens.", title=fyrirUtan.info)
        else:
            eg.msgbox("I wonder if the key is somewhere in the room.", title=fyrirUtan.info)
            eg.msgbox("you go back", title=fyrirUtan.info)
            mainRoom()
        if "torch" in fyrirUtan.items:
            eg.msgbox("You walk in. There is a carpet leading down the middle of the room. Your torch lights up the room exluding the other side.", title=fyrirUtan.info)
        else:
            eg.msgbox("You walk in. There is a carpet leading down the middle of the room. Everything is dimly lit up with candles on either side.", title=fyrirUtan.info)
        eg.msgbox("Everything is quiet.", title=fyrirUtan.info)
        eg.msgbox("...", title=fyrirUtan.info)
        eg.msgbox("You walk along the carpet", title=fyrirUtan.info)
        eg.msgbox("You see a chair and a dark figure sitting in it.", title=fyrirUtan.info)
        eg.msgbox("It does not move.", title=fyrirUtan.info)
        if eg.ynbox("Do you want to go closer?", title=fyrirUtan.info):
            eg.msgbox("You decide to approach", title=fyrirUtan.info)
            eg.msgbox("AS you get closer the door slams shut and the figure starts moving.", title=fyrirUtan.info)
        else:
            eg.msgbox("You decide not to approach and turn around.", title=fyrirUtan.info)
            eg.msgbox("As you turn around you see the door slam shut and the figure starts moving.", title=fyrirUtan.info)
        one = ["...","I","Who are you!"]    
        time.sleep(0.5)
        one1 = eg.buttonbox("Who goes there!", choices=one)
    
        if one1 == "...":
            oneone = ["Fear","Stupidity","Braveness","..."]
            oneone1 = eg.buttonbox("Do you not speak out of Fear, Stupidity or Braveness", choices=oneone, title=fyrirUtan.info)
    
            if oneone1 == "Fear" or oneone1 == "...":
    
                if oneone == "...":
                    eg.msgbox("'Why do you Fear me?'", title=fyrirUtan.info)
                    if "torch" in fyrirUtan.items:
                        end_torch()
                    else:
                        end1()
            elif oneone1 == "Braveness":
                eg.msgbox("Brave huh?, More like stupidity for my room!", title=fyrirUtan.info)
                eg.msgbox("Il give you an chance to leave for your stupidity", title=fyrirUtan.info)
                Quick_leave = ["Leave!","Stay"]
                Quick_leaveQ =eg.buttonbox("Il give you 5 seconds to leave!", title=fyrirUtan.info)
    
            elif oneone1 == "Stupidity":
                eg.msgbox("'A stupid person does not know he is stupid.'", title=fyrirUtan.info)
                eg.msgbox("'Answer me this.'")
                riddle = eg.enterbox("You cannot see me, hear me, or touch me. I lie behind the stars and alter what is real, I am what you really fear. Close your eyes and I come near. What am I?", title=fyrirUtan.info)
                if riddle.lower() == "dark" or riddle.lower() == "darkness" or riddle.lower() == "you":
                    eg.msgbox("'Correct'")
                    eg.msgbox("'I will answer one question that you have for me.'", title=fyrirUtan.info)
                else:
                    eg.msgbox("Guess i was wrong.", title=fyrirUtan.info)
                    end1()
        elif one1 == "I":
            name = ["None of your business","First of Who are you?", "My name is..."]
            nameQ = eg.buttonbox("Who are you?", choices=name)
            if nameQ == "None of your business":
                eg.msgbox("Is it not? You walk into my room and disturbe me!")
                name2 = ["I sayd none of your business","First tell me who are you?","My name is..."]
                nameQ2 = eg.buttonbox("'Now tell me. Who are you'", choices=name2, title=fyrirUtan.info)
                if nameQ2 == "I sayd none of your business":
                    end1()
        elif one1 == "Who are you?":
            okno = ["Alright","No"]
            oknoQ =eg.buttonbox("First tell me who you are", choices=okno, title=fyrirUtan.info)
            if oknoQ == "Alright":
                Name = eg.enterbox("Now tell me, What is your name", title=fyrirUtan.info)
            else:
                eg.msgbox("Then you will not know my name", title=fyrirUtan.info)
                eg.msgbox("Yet you will know my power!", title=fyrirUtan.info)
                end1()
            eg.msgbox("I am Erebus. God of darkness.", title=fyrirUtan.info)
    def end1():
        if "torch" in fyrirUtan.items:
            end_torch()
        else:
            eg.msgbox("The figure fades into the darkness.", title=fyrirUtan.info)
            eg.msgbox("The room quickly becomes pitch dark.", title=fyrirUtan.info)
            eg.msgbox("You can feel the darkness surround you, pour into you, You can feel your mind getting dark.", title=fyrirUtan.info)
            eg.msgbox("You see darkness, You feel darkness", title=fyrirUtan.info)
            eg.msgbox("You see nothing, You feel nothing", title=fyrirUtan.info)
    def end2():
        eg.msgbox("You can feel the darkness surround you, pour into you, You can feel your mind getting dark.", title=fyrirUtan.info)
        eg.msgbox("You see darkness, You feel darkness", title=fyrirUtan.info)
        eg.msgbox("You see nothing, You feel nothing", title=fyrirUtan.info)
        dead()
    def end_torch():
        global Darkness
        global steps
        endtorch = ["No!", "Why?", "Yea"]
        eg.msgbox("The figure fades into the darkness.", title=fyrirUtan.info)
        eg.msgbox("The room, quickly becomes pitch dark excluding around your torch.", title=fyrirUtan.info)
        endtorchQ = eg.buttonbox("'Why dont you remove that torch?'", choices=endtorch)
        if endtorchQ == "No!":
            eg.msgbox("'I guess i can wait then.'", title=fyrirUtan.info)
        elif endtorchQ == "Why?":
            kill = ["Alright...(give up)", "Never!"]
            killQ = eg.buttonbox("So i can kill you quicker!", choices=kill, title=fyrirUtan.info)
            if killQ == "Alright...(give up)":
                eg.msgbox("You place the torch down. As soon as you do", title=fyrirUtan.info)
                end2()
            else:
                eg.msgbox("So be it.")
                End1()
        elif endtorchQ == "Yea":
            eg.msgbox("You put the torch on the ground.")
            eg.msgbox("As soon as you put it down you feel the darkness getting closer!", title=fyrirUtan.info)
            Start_time = time.time()
            pickup = ["Give up!", "Cant move.","Pick up torch!", "The pain...", "..."]
            pickupQ = eg.buttonbox("You can feel your soul, vison and thougts getting dark!, Pain is too much, I have got to get the darkness away! FAST!", choices=pickup)
            total_time = time.time() - Start_time
            if pickupQ == "Pick up torch!":
                if total_time > 1.5:
                    if total_time > 2:
                        if total_time > 2.5:
                            if total_time > 3.5:
                                eg.msgbox("You cannot find the strength or mind to pick up the torch.", title=fyrirUtan.info)
                                end2()
                            else:
                                eg.msgbox("You can feel the darkness removing some of your strength and mind as you raise the torch back up", title=fyrirUtan.info)
                                Darkness += 3
                        else:
                            eg.msgbox("You could feel the darkness in your mind, body and soul weakening them.", title=fyrirUtan.info)
                            Darkness += 2
                    else:
                        eg.msgbox("You could feel the darknes inside you for a second.", title=fyrirUtan.info)
                        Darkness += 1
                else:
                    eg.msgbox("You were able to pick up the torch before it was able to touch you.", title=fyrirUtan.info)
            else:
                eg.msgbox("The darkness is too much, You dont have the power or mind to pick up the torch!", title=fyrirUtan.info)

            whatnow = ["Stay still","Try to get out", "Move further in"]
            whatnowQ = eg.buttonbox("What now?", choices=whatnow)
            if whatnowQ == "Stay still":
                eg.msgbox("You stand still, While doing so the darkness attacks you!, You cant afford to stand still", title=fyrirUtan.info)
                Darkness += 1 
                whatnow2 = ["Try to get out","Move further in"]
                whatnow2Q = eg.buttonbox("You choose to...",choices=whatnow2)
                if whatnow2Q == "Try to get out":
                	eg.msgbox("You move back to the door, Try to open it but it is locked. While doing that the darkness attacks you!", title=fyrirUtan.info)
                	Darkness += 1
            elif whatnowQ == "Try to get out":
                eg.msgbox("You move back to the door, Try to open it but it is locked. While doing that the darkness attacks you!", title=fyrirUtan.info)
                Darkness += 1
                eg.msgbox("You choose to move to the chair", title=fyrirUtan.info)
                End_Attack
            elif whatnowQ == "Move further in":
                eg.msgbox("You move towards the chair", ok_button="Continue")
                End_Attack()
    def End_Attack():
        global Monster_Alive
        global Alive
        global Damage
        global Enemy_damage
        global Darkness
        global steps
        while Darkness < 5 and steps < 15:
            def End_status():
                global Darkness
                if Darkness == 1:
                    eg.msgbox("The darkness exsposes me.", title=fyrirUtan.info)
                elif Darkness == 2:
                    eg.msgbox("I can feel my mind getting dark, My memorys getting blanked and replaced with darkness", title=fyrirUtan.info)
                elif Darkness == 4:
                    eg.msgbox("I can feel my power getting smaller as the darkness Darkens my Life.", title=fyrirUtan.info)
                elif Darkness ==5:
                    eg.msgbox("My life, Is dark. My heart, Is dark,My Mind, is dark.", title=fyrirUtan.info)
                    eg.msgbox("The light is dark.", title=fyrirUtan.info)
                    eg.msgbox("My life is no longer mine, Its possessed by darkness.", title=fyrirUtan.info)
            leftright = ("Move torch Left","Move torch Front", "Move torch Right")
            AttackType = randint(1,3);
            if AttackType == 1:
                AttackType = "LEFT"
            elif AttackType == 2:
                AttackType = "MIDDLE"
            else:
                AttackType = "RIGHT"
            AttackTime = 2
            start_time = time.time()
            dodge = eg.buttonbox("The darkness gather to the "+AttackType, choices=leftright, title=fyrirUtan.info)
            total_time = time.time() - start_time
            if total_time < AttackTime:
                if dodge == "Move torch Left" and AttackType == "LEFT":
                    eg.msgbox("You light up the darkness before its able to attack!", title=fyrirUtan.info)
                    steps += 1
                elif dodge == "Move torch Front" and AttackType == "MIDDLE":
                    eg.msgbox("You light up the darkness before its able to attack!", title=fyrirUtan.info)
                    steps += 1
                elif dodge == "Move torch Right" and AttackType == "RIGHT":
                   eg.msgbox("You light up the darkness before its able to attack!", title=fyrirUtan.info)
                   steps += 1
                else:
                    eg.msgbox("", title=fyrirUtan.info)
                    eg.msgbox("The darkness enters your body!", title=fyrirUtan.info)
                    Darkness += 1
                    End_status()
            else:
                eg.msgbox("The darkness enters you before you are able to light it up!" , title=fyrirUtan.info)
                Darkness+=1
                End_status()
        if steps == 15:
            eg.msgbox("You make it up to the Chair and light it up", title=fyrirUtan.info)
            eg.msgbox("You see a man, A mummy like man sitting in the chair.", title=fyrirUtan.info)
            eg.msgbox("He looks up to you.", title=fyrirUtan.info)
            question = ("Why","I will","I know(give up)")
            questionQ = eg.buttonbox("'You will never excape'", choices=question)
            if questionQ == "why":
                eg.msgbox("Because Darkness will always fall. Eventually", title=fyrirUtan.info)
            elif questionQ == "I will":
                eg.msgbox("And how are you going to do that?", title=fyrirUtan.info)
            else:
                eg.msgbox("'Yes...'", title=fyrirUtan.info)
                eg.msgbox("While waiting the torch dies down. And as soon as it does.", title=fyrirUtan.info)
                end2()
            ending = ["hand","torch"]
            for x in fyrirUtan.items:
                if x == "knife":
                    ending.append("knife")
                elif x == ("revolver"):
                    ending.append("revolver")
                elif x == "stick":
                    ending.append("StickOfSlightConvenience")
                elif x == "gun":
                    ending.append("gun")
                elif x == +"torch":
                	ending.append("torch")
                else:
                	print("You broke this code")
                    
            endingQ = eg.buttonbox("End him with...", choices=ending)
            if endingQ == "knife":
                eg.msgbox("You take out your knife, Move it up to the Mans neck.")
                eg.msgbox("Cutting into the neck, He breathes in.")
                eg.msgbox("Then he exhales as you continue your cut, The air escapes through the cut you made.")
                eg.msgbox("Spewing small amount of blood onto your arm.")
                eg.msgbox("you then proceed to puncher the mans chest, directly into the heart. He flinches a little bit")
                eg.msgbox("As soon as he stops moving the Room lights up and all the darkness dissapates")
                eg.msgbox("The door opens, You leave the room.")
                laeve()
            elif endingQ == "revolver" or endingQ == "gun":
                eg.msgbox("You take out your gun, Point it at the mans head.")
                eg.msgbox("You Squeeze the trigger slowly")
                time.sleep(1)
                eg.msgbox("The gun goes off hitting the man in the head.")
                eg.msgbox("The Room lights up and all the darkness dissapates")
                eg.msgbox("The door opens, You leave the room.")
                leave()
            elif endingQ == "StickOfSlightConvenience":
                eg.msgbox("You gently tap his head with the stick.")
                eg.msgbox("He explodes into candy.")
                eg.msgbox("You eat it all and then leave.")
                leave()
            elif endingQ == "hand":
                eg.msgbox("You put your hands around the mans head, And in a quick motion you break his neck. He flinches a little.")
                eg.msgbox("You hear a little crack, As soon as he stops moving the Room lights up and all the darkness dissapates ")
                eg.msgbox("The door opens, You leave the room.")
                leave()
            else:
                pass
    main()
dodo()