print("*****Compute the Hypotenuse*****")

# import math module for square root
import math

# define function named triangle with parameters sideOne and sideTwo
def triangle(sideOne, sideTwo):

    # calculate the hypotenuse using pythagorean theorem
    hypotenuse = math.sqrt(sideOne * sideOne + sideTwo * sideTwo)

    # return the hypotenuse
    return hypotenuse

# ask the user to input the two side lengths of the right triangle
sideOne = int(input("enter side a: "))
sideTwo = int(input("enter side b: "))

# invoke the function and set it as h
h = triangle(sideOne, sideTwo)
print(f"the hypotenuse is: {h:.2f}")
