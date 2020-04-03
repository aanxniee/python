#Rock Paper Scissors Game
"""
1. prompt the player to throw their move
2. generate a random move for the computer
3. determine the outcome
"""
import random

#create list of moves that the computer can compute
moves = ['r', 'p', 's']

totalGames = 0
playerWins = 0
ties = 0

#create boolean variable to control the loop
done = False

while not done:
    
    #prompt the user to enter their move
    playerMove = input("enter your move: ")

    #validate player's input
    while playerMove != 'r' and\
          playerMove != 'R' and\
          playerMove != 's' and\
          playerMove != 'S' and\
          playerMove != 'p' and\
          playerMove != 'P':
        print("invalid move")
        
        playerMove = input("enter your move (valid inputs are r/R, p/P, s/S): ")
    
    #generate the computer move 
    compMove = random.choice(moves)
    
    #determine the outcome
    if playerMove == compMove:
        print("player's move: ", playerMove)
        print("computer's move: ", compMove)
        print("it is a tie")
        
        #increment the ties
        ties += 1
        
    elif playerMove == 'r' and compMove == 's'\
         or playerMove == 'p' and compMove == 'r'\
         or playerMove == 's' and compMove == 'p':
        
        print("player's move: ", playerMove)
        print("computer's move: ", compMove)
        print("player wins!!!")    
        
        #increment the player wins
        playerWins += 1
    
    else:
        print("player's move: ", playerMove)
        print("computer's move: ", compMove)
        print("player loses ):")  
        
    #increment the number of games by one
    totalGames += 1
    
    #ask the user if they would like to play again
    response = input("\nto play again, press enter (any other key to quit): ")
    if response != "":
        done = True
        print("thank you for playing")
        
print("\n==============================================")
print("                   Game Stats                   ")
print("total number of games played: ", totalGames)
print("player's wins               : ", playerWins)
print("ties                        : ", ties)

losses = totalGames - ties - playerWins
print("number of losses            : ", losses)

if playerWins > losses:
    print("player is the winner")
elif playerWins == ties:
    print("there are no winners")
else:
    print("player is the loser")
print("================================================")
