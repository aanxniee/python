print("*****Dice Game*****")

# import random module to generate 2 dice numbers
import random
# set original number of points to 1000
points = 1000
# set boolean variable to control the loop
play = True
# set boolean variable to control win or loss
win = True

# this loop runs until play is set to False
while play == True:

    print(f"You have {points} points")
    #ask the user the number of points they would like to stake
    stake = int(input("Points to risk: "))

    # generate two random dice numbers
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    # define function called rolls that calculates
    # whether the sum is even or odd
    def rolls():
        
        # if sum is even, win gets set as False
        if (dice1 + dice2) % 2 == 0:
            print("You lose")
            global win
            win = False

        # if sum is odd, win remains True
        else:
            print("You win")
            win = True

    # invoke the function to display whether the play won or lost    
    print(f"Roll is {dice1} and {dice2}")
    rolls()

    # ask the user if they would like to play again
    keepGoing = input("Play again? ")
    print()

    # if the player inputs 'N', set play as false
    # break the loop
    if keepGoing == 'N' or\
       keepGoing == 'n':
        play = False

    # calculate the new amount of points
    if win == True: # if player won, points + stake * 2
        points += stake * 2

    if win == False: # if player lost, points - stake
        points -= stake

# display final score
print(f"Final score: {points}")
