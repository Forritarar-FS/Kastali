#!/usr/bin/python
import random
from . import room

def do():
        th = room.grunnur(42)
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
        'At any given time, there are at least 1,800 thunderstorms in progress over the earth’s atmosphere.', 
        'In 1980, a Las Vegas hospital suspended workers for betting on when patients would die.', 
        'It was once against the law to have a pet dog in a city in Iceland.', 
        'A B-25 bomber crashed into the 79th floor of the Empire State Building on July 28, 1945.',
        'A giraffe can clean its ears with its 21-inch tongue!','In France, there’s a place called Y.',
        'One in every 4 Americans has appeared on television at least once in their life.',
        'In ancient Rome, when a man testified in court he would swear on his testicles.',
        'The average human will shed 40 pounds of skin in a lifetime.',
        'A Virginia law requires all bathtubs to be kept inside the house',
        'Truck driving is the most dangerous occupation by accidental deaths (799 in 2001).',
        'A group of toads is called a knot.',
        'Illuminati Confirmed!',
        'The top butterfly flight speed is 12 miles per hour. Some moths can fly 25 miles per hour!',
        "More than 30 prosent of the people in the world have never made or received a telephone call.",
        'Termites have been known to eat food twice as fast when heavy metal music is playing.',
        'All female bees in a given hive are sisters',
        'Owls are the only birds that can see the color blue.',
        'The Automated Teller Machine (ATM) was introduced in England in 1965.',
        'Cats have over 100 vocal sounds; dogs only have 10.',
        'It was discovered on a space mission that a frog can throw up.',
        'Mailing an entire building has been illegal in the U.S. since 1916 when a man mailed a 40,000-ton brick house across Utah to avoid high freight rates.',
        'A shark is the only fish that can blink with both eyes.',
        'Johnny Appleseed planted apples so that people could use apple cider to make alcohol.',
        'City with the most Roll Royces per capita: Hong Kong.',
        'The past-tense of the English word “dare” is “durst”',
        'Almonds are a member of the peach family.',
        'Humans use a total of 72 different muscles in speech.',
        'Baby robins eat 14 feet of earthworms every day'
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
                th.go("e")
        elif choice == 2:
                print(random.choice(facts))
                th.go("e")
        elif choice == 3:
                print ("Well you just killed yourself!")
                th.go("e")
        elif choice == 4:
            while 1 == 1:
                print ("LELELEL")
                th.go("e")
        else:    ## default ##
                print ("Invalid number. Try again...")