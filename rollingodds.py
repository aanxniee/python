print("*****rolling odds*****")

#import random
import random

print("let's roll some dice!")

#set variables to keep track of the number of rolls, odds and evens
times = 0
consecutiveO = 0
consecutiveE = 0

#this loop runs until three consecutive odds are rolled
while consecutiveO != 3:

    #generate random number as a roll
    number = random.randint(1,6)
    print("you rolled a", number)

    #keeps track of the consecutive odds
    if number == 1 or number == 3 or number == 5:
        consecutiveO += 1
        consecutiveE = 0

    
    if number == 2 or number == 4 or number == 6:
        consecutiveE += 1
        #consecutive odds gets set to 0 when an even is rolled
        consecutiveO = 0

    #update the number of times rolled
    times += 1
    
print(f"three in a row in {times} rolls")
