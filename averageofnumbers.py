print("Average of Numbers")

# open the file for reading
file = open("numbers.txt", "r")

numbersList = file.read() # read the file and set it as a variable
numbersList = numbersList.split() # turn the file into a list

count = 0 # set the count to 0
# this loop counts the number of numbers in the list
for number in numbersList:
    count += 1
    
total = 0 # set the sum to 0
# this loop takes each number in the list and adds it to the total
for number in numbersList:
    total += int(number) # change the numbers from a string to an integer

average = total/count #calculate the average
print(f"the average of numbers in numbers.txt is: {average:.2f}")
