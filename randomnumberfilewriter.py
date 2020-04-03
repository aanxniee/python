print("Random Number File Writer")

# import random module to generate random numbers
import random

# open the file for reading
file = open("randomNumbers.txt", "w")

# ask the user for the number of numbers to generate
count = int(input("enter the number of random numbers the file will hold: "))

for i in range(count): # this loop runs until count is reached
    number = random.randint(1, 100) # generate random numbers between 1-100
    number = str(number) # turn the number from an integer to a string
    file.write(number+"\n") # add the number to the file

# close the file
file.close()
