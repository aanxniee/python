print("*****Sum Range*****")

# define function called sumRange with parameters a, b
# a and b are the numbers of the range
def sumRange(a, b):

    # set total to 0
    total = 0

    # this loop runs from a to b 
    for i in range(a, b+1):

        # calculate the sum of the range
        total += i

    # return the total
    return total
    
# ask the user for the range
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

# invoke the function and set it as s
s = sumRange(a, b)
print(f"the sum of numbers from {a} to {b} is: {s}")
