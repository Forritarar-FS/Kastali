#!/usr/bin/python
import random
print("============|WELCOME TO ROOM 42|============")
print("1. Whats the meaning of life?")
print("2. A Random Fact that might just amuse you!")
print("3. Kill yourself!")
print("4. Break python")
print("============================================")

choice = input('Enter your choice [1-4] : ')
choice = int(choice)

## hérna er ég mest lista of strings(facts) 
facts = [
'The average life of a taste bud is 10 days.', 
'In 1980, a Las Vegas hospital suspended workers for betting on when patients would die.', 
'In 1980, a Las Vegas hospital suspended workers for betting on when patients would die.', 
'It was once against the law to have a pet dog in a city in Iceland.', 
'A B-25 bomber crashed into the 79th floor of the Empire State Building on July 28, 1945.',
'A giraffe can clean its ears with its 21-inch tongue!','In France, there’s a place called Y.',
'One in every 4 Americans has appeared on television at least once in their life.',
'In ancient Rome, when a man testified in court he would swear on his testicles.',
'The average human will shed 40 pounds of skin in a lifetime.',
'A Virginia law requires all bathtubs to be kept inside the house',
'Truck driving is the most dangerous occupation by accidental deaths (799 in 2001).',
'A group of toads is called a knot.'
'Illuminati Confirmed!'
]

## LEL
if choice == 1:
        print ("=============<|42|>=============")
        print("ALL BASK IN THE GLORY THAT IS 42")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░")
        print("░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░")
        print("░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░")
        print("░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░░")
        print("░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░░")
        print("█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█░")
        print("█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░")
        print("░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░")
        print("░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░")
        print("░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░░")
        print("░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░░")
        print("░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░")
        print("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░░")
        print("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░░")
        print("░░░░░░░░░░░░░░▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ")
        print("ALL BASK IN THE GLORY THAT IS 42")
        print ("=============<|42|>=============")
elif choice == 2:
        print(random.choice(facts))
elif choice == 3:
        print ("Well you just killed yourself!")
elif choice == 4:
	while 1 == 1:
   		print ("LELELEL")
else:    ## default ##
        print ("Invalid number. Try again...")
 