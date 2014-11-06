from . import room
import webbrowser
import time

url1 = "http://upload.wikimedia.org/wikipedia/commons/5/54/WaterMill_Window_LymeRegis.jpg"
def do():
    pass
    print ("Velkominn í herbergi 34!")
    time.sleep(1)
    print ("Opnaðu internet glugga og færðu hann við hliðina á þessum glugga.")
    time.sleep(5)
    def herbergi():
        webbrowser.open("http://tigerligan.com/wp-content/uploads/2014/07/luxury-white-detail-of-affordable-bedroom-sets-with-luminous-wooden-floor-amusing-vanity-ornament-mesmerizing-large-glazing-window-marvelous-cabinet-and-interesting-simple-rug.jpg")
        spurning1 = input("Það er Gluggi(1), Rúm(2) og skápur(3). Hvert viltu fara? \n")
        if spurning1 == '1':
            webbrowser.open(url1)
            subspurning1 = input("glugginn er lokaður, viltu opna hann? (já/nei)\n") 
            if subspurning1.lower() == "já": 
                webbrowser.open("http://www.laurelkallenbach.com/lkblog/wp-content/uploads/2010/05/View-out-window.jpg")
                subspurning2 = input("Hvað sérðu út um gluggann?\n")
                if subspurning2.lower() == "sjó" or subspurning2.lower() == "tré" or subspurning2.lower() == "skí":
                    print ("frábært.")
                    time.sleep(1)
                    print ("Þú lokar glugganum.")
                    time.sleep(2)
                    herbergi()
                else:
                    print ("Nei...")
                    time.sleep(1)
                    print ("Þú lokar glugganum.")
                    time.sleep(2)
                    herbergi()
            else:
                herbergi()
        elif spurning1 == '2':
            spurning2 = input("Viltu fara að sofa? (já/nei)\n")
            if spurning2.lower() == "já":
                time.sleep(1)
                print ("Zzz")
                x = 0
                while x < 10:
                    dot = "."
                    print (dot)
                    time.sleep(1)
                    x = x + 1
                print ("Góðan daginn")
                time.sleep(1)
                herbergi()
            else:
                subspurning3 = input("Viltu kíkja undir rúmið? (já/nei)\n")
                if subspurning3.lower() == "já":
                    print ("Þú fannst kassa með spurningum utan á")
                    time.sleep(1)
                    subspurning4 = input("Viltu opna kassann með því að leysa dæmin? (já/nei)\n")
                    if subspurning4.lower() == "já":
                        def kassi():
                            #spurning 1
                            kassi1 = input("Hvað er 19 * 2?\n")
                            if kassi1.lower() == "38":
                                #spurning 2
                                kassi2 = input("Hvað er 9999 + 1111?\n")
                                if kassi2.lower() == "11110":
                                    #spurning 3
                                    kassi2 = input("Hvað er 2 + 5 * 4?\n")
                                    if kassi2.lower() == "22":
                                        print ("Kassinn opnast...")
                                        time.sleep(2)
                                        print ("Þú fannst sand!")
                                        webbrowser.open("http://www.chemistryland.com/CHM130S/07-Mole/SandInHand.jpg")
                                        room.grunnur.items.append("Sandur")

                                        time.sleep(1)
                                        print ("Þú gætir þurft að nota þennan sand einhverstaðar")
                                        time.sleep(2)
                                        herbergi()
                                    else:
                                        print ("nei...")
                                        time.sleep(1)
                                        retry1 = input("Viltu reyna aftur? (já/nei)\n")
                                        if retry1.lower() == "já":
                                            kassi()
                                        else:
                                            herbergi()
                                else:
                                    print ("nei...")
                                    time.sleep(1)
                                    retry1 = input("Viltu reyna aftur? (já/nei)\n")
                                    if retry1.lower() == "já":
                                        kassi()
                                    else:
                                        herbergi()
                            else:
                                print ("nei...")
                                retry1 = input("Viltu reyna aftur? (já/nei)\n")
                                if retry1.lower() == "já":
                                    kassi()
                                else:
                                    herbergi()
                        kassi()
        elif spurning1 == '3':
            webbrowser.open("http://www.thehomespun.com/wp-content/uploads/2012/06/closeup-wooden-cabinet1.jpg")
            skapur = input("Viltu opna skápinn? (já/nei)")
            if skapur.lower() == "já":
                print ("skápurinn er tómur")
                time.sleep(1)
                webbrowser.open("http://www.baronet4tibet.com/images/altars_large_2dr/C004-03/C004-03-frntdoors-open-web.jpg")
                time.sleep(4)
                herbergi()
            else:
                herbergi()



    herbergi()





