#Coin Flip Stimulation
"""
1. generate heads or tails
2. count the number of flips needed to get HHH or TTT
3. calculate the average number of flips needed
"""
import random

#create list of moves that the computer can compute
moves = ['H', 'T']

#times is the number of times the stimulation will run
times = 0
#sum_of_flips is the sum of the number of flips it took
sum_of_flips = 0

#this loop runs the stimulation 10 times
while times < 10:

    #assign variables 
    totalFlips = 0
    consecutiveH = 0
    consecutiveT = 0

    #this loop runs until 3 consective heads or tails are flipped
    while consecutiveH != 3 and consecutiveT != 3:

        #generate heads or tails
        flip = random.choice(moves)
        print(flip, end = " ")

        #count consecutives for heads
        if flip == 'H':
            consecutiveH += 1
            #if heads is flipped, consecutive of tails is set to 0
            consecutiveT = 0
        #count consecutive for tails
        if flip == 'T':
            consecutiveT += 1
            #if tails is flipped, consecutive of heads is set to 0
            consecutiveH = 0

        #update the number of flips
        totalFlips += 1
    #update the sum of the total number of flips
    sum_of_flips += totalFlips
    print(f"({totalFlips} flips)")

    times += 1

#calculate the average number of flips it takes to reach 2 consecutives
average = sum_of_flips / 10
print(f"on average, {average:.1f} flips were needed")

