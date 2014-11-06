from . import room
from random import randint
import turtle
def do():
	th = room.grunnur(41)
	print ("Velkomin/nn í herbergið mitt :)")


board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Viltu spila Battleship!?")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(100):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print ("Til hamingju þú drapst skipið mitt!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Langt í burtu!")
        elif(board[guess_row][guess_col] == "X"):
            print ("Þú hefur giskað á þennan áður!")
        else:
            print ("Reyndu aftur!.")
            board[guess_row][guess_col] = "X"

    print (turn + 1) 
    print_board(board)
if input("viltu fara í næsta herbergi?")[0] == 'j':
    th = room.grunnur(41)
    th.go('s')
else:
    wn = turtle.Screen()
    ninja = turtle.Turtle()

    ninja.speed(1000)

    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)
        
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        
        ninja.right(2)

    for i in range(180):
        ninja.forward(100)
        ninja.right(40)
        ninja.forward(30)
        ninja.left(70)
        ninja.forward(60)
        ninja.right(40)
        
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        
        ninja.right(4)
        
    turtle.exitonclick()     

    wn.mainloop()

    

	