print("*****perimeter of a polygon*****")

#import math module 
from math import sqrt

#assign variables
perimeter = 0

#read the coordinate of the first point entered from the user
firstX = float(input("enter the x-coordinate of the point: "))
firstY = float(input("enter the y-coordinate of the point: "))

previousX = firstX
previousY = firstY

line = input("enter the x-coordinate of the point (blank to quit): ")
while line != "":
    #convert the x value from a string to a float
    x = float(line)
    y = float(input("enter the y-coordinate of the point: "))
    
    #apply the distance formula to calculate the distance from one point to the other
    distance = sqrt((previousX - x) ** 2 + (previousY - y) ** 2)
    perimeter += distance

    #update the previous x and y coordinates for the next loop
    previousX = x
    previousY = y

    #update LCV and validate user to continue the loop
    line = input("enter the x-coordinate of the point (blank to quit): ")

#calculate the distance from the last point to the first point
distance = sqrt((firstX - x) ** 2 + (firstY - y) ** 2)
perimeter += distance

print(f"the perimeter of the polygon is {perimeter:.2f} units ")
