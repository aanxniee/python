"""
1. ask the user to enter the shape of their choice
2. define functions and nested loops to display the shape with the desired height, length and width
3. ask the user if they would like to draw another shape
4. display the summary of shapes drawn
"""
# set variables to count the number of shapes drawn
horizontal = 0
vertical = 0
rectangle = 0
leftSlant = 0
rightSlant = 0
isoceles = 0

# define function called menu to display the menu to the user
def menu():
    print("""
    This program draws the following shapes:
    1) Horizontal Line
    2) Vertical Line
    3) Rectangle
    4) Left slant right angle triangle
    5) Right slant right angle triangle 
    6) Isosceles triangle
    """)
 
# define function called validateInput to validate the user's dimensions
def validateInput():
    # ask the user to enter the dimensions
    size = int(input("Enter dimension value (1-20): "))
    # this loop validates that the dimension is between 1 and 20
    while size < 1 or size > 20:
        print("Invalid input for dimension")
        size = int(input("\nEnter the dimension value (1-20): "))
     
    return size
        
#define a function called validateShape to validate the user's choice and display the shape chosen
def validateShape(shape):
     
    # this loop validates that the users choice is between 1 and 6
    while shape < 1 or shape > 6:
        print("Invalid input for choice")
        shape = int(input("\nEnter your choice (1-6): "))  
        
# define a function called drawHorizontalLine with the parameter length
def drawHorizontalLine(length): 
    # this loop runs until the desired length is reached
    for i in range(length):
        print("*", end = "")    
        
# define a function called drawVerticalLine with the parameter height
def drawVerticalLine(height):
    # this loop runs until the desired height is reached
    for i in range(height):
        print("*") 
    
# define a function called drawRectangle that takes in the parameters 
def drawRectangle(width, height):
    # this loop runs until the desired width is reached
    for row in range(height):
        # this loop runs until the desired height is reached
        for col in range(width):
            print("*", end = "")
            
        # drop down to the next row    
        print()

# define function called drawLeftSlantTriangle with the parameter height
def drawLeftSlantTriangle(height):
    # this loop runs until the desired height is reached
    for i in range(height):
        # this loop prints the "*" with one more per line
        for j in range(0, i + 1):
            print("*", end = "")
                
        # drop down to next row
        print()    
        
# define function called drawRightSlantTriangle with the parameter height
def drawRightSlantTriangle(height):
    # this loop runs until the desired height is reached
    for i in range(1, height + 1):
        for j in range(1, height + 1):
             # this prints the " " with one less per line
            if(j <= height - i):
                print('', end = ' ')
            # this prints the "*" with one more per line
            else:
                print('*', end = '')
                
        # drop down to the next row
        print()

# define function called drawIsocelesTriangle with the parameter height
def drawIsocelesTriangle(height):
    j = 0
    # this loop runs until the desired height is reached
    for i in range(1, height+1):
        # this prints the " " with one more per line on each side
        for space in range(1, (height-i)+1):
            print(end = " ")
            
        # this prints the "*" with two more per line
        while j != (2*i-1):
            print("*", end = "")
            j += 1
        j = 0 # set j to 0
        
        print() # drop down to the next row
        
# define function called validateResponse that validates whether the user wants to continue or not
def validateResponse():
    # this loop validates that the user input is valid
    while response != 'n' and\
          response != 'N' and\
          response != 'y' and\
          response != 'Y':
        print("Invalid input! Your input must be 'y' or 'n'")

        # ask the user for their response again
        response = input("\nWould you like to draw another one (y/n)? ")
        
# deinfe function called summary that displays the number of shapes drawn
def summary():
    # display the summary of shapes drawn     
    print()
    print("Here is a summary of the shapes that were drawn.")
    print()
    print(f"Horizontal Line                    {horizontal}")
    print(f"Vertical Line                      {vertical}")
    print(f"Rectangle                          {rectangle}")
    print(f"Left slant right angle triangle    {leftSlant}")
    print(f"Right slant right angle triangle   {rightSlant}")
    print(f"Isoceles triangle                  {isoceles}")  
    print("Thank you for using Shape Generator. Goodbye !!")
    
# main loop
print("Welcome to the Shape Generator")

# set boolean variable to to control the while loop
done = False

# this loop runs unt  il done is set as True
while done == False:
    
    menu() # invoke function to display menu
    # prompt the user to enter the shape they would like to draw
    shape = int(input("Enter your choice (1-6): ")) 
    validateShape(shape) # invoke the function to validate the shape
    
    if shape == 1:
        # validate the length by passing it through the validateInput() function
        length = validateInput()
        print()
        print(f"Here is the horizontal line with the length of {length}: ")
        drawHorizontalLine(length) # invoke the function for a horizontal line
        horizontal += 1 # update the counter
        
    if shape == 2:
        # validate the height by passing it through the validateInput() function
        height = validateInput()
        print()
        print(f"Here is the vertical line with the height of {height}: ")
        drawVerticalLine(height) # invoke the function for a vertical line
        vertical += 1 # update the counter
        
    if shape == 3:
        # validate the width and height by passing it through the validateInput() function
        width = validateInput()
        height = validateInput()
        print()
        print(f"Here is the rectangle with the width of {width} and the height of {height}: ")    
        drawRectangle(width, height) # invoke the function for a rectangle
        rectangle += 1 # update the counter
        
    if shape == 4:
        # validate the height by passing it through the validateInput() function
        height = validateInput() 
        print()
        print(f"Here is the left slant right triangle with the height of {height}: ")    
        drawLeftSlantTriangle(height) # invoke the function for a left slant triangle
        leftSlant += 1 # update the counter
        
    if shape == 5:
        # validate the height by passing it through the validateInput() function
        height = validateInput() 
        print()
        print(f"Here is the right slant right triangle with the height of {height}: ")
        drawRightSlantTriangle(height) # invoke the function for a right slant triangle
        rightSlant += 1 # update the counter
        
    if shape == 6:
        # validate the height by passing it through the validateInput() function
        height = validateInput() 
        print()
        print(f"Here is the isoceles triangle with the height of {height}: ")    
        drawIsocelesTriangle(height) # invoke the function for an isoceles triangle
        isoceles += 1 # update the counter
        
    # ask the user if they would like to draw another shape 
    response = input("\nWould you like to draw another one (y/n)? ")
    # if the user input is no, set done as True (this terminates the boolean controlled loop)
    if response == 'n' or response == 'N':
        done = True 

# display the summary of shapes drawn   
summary()

        
