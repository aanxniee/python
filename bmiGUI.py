# import library to create GUI
from tkinter import *

screen = Tk()
screen.title("BMI Calculator")
screen.geometry("300x250")
#***************************************
def getBMI():

    # get the weight and height from the entry box and convert it as a float
    weight = float(weightP.get())
    heightFeet = float(heightF.get())
    heightIn = float(heightI.get())

    # turn the height in feet to inches
    height = heightFeet * 12 + heightIn

    # calulate the BMI using the formula
    bmi = weight/(height * height) * 703
    # set the results and print it to the label
    print(result.set(f"BMI : {bmi:.2f}"))
#***************************************
# create a font
myfont = "Helvetica 12"

# create three labels

"""
1. sticky W means left allign
2. pady creates space between the rows
3. width sets the width of the entry box
4. columnspan makes the button stretch over 2 columns
"""

Label(screen, text = "Enter Weight (lbs): ", font = myfont).\
              grid(row = 0, column = 0, pady = 5, sticky = W) 
Label(screen, text = "Enter Height (ft): ", font = myfont).\
              grid(row = 1, column = 0, pady = 5, sticky = W)
Label(screen, text = "Enter Height (in): ", font = myfont).\
              grid(row = 2, column = 0, pady = 5, sticky = W)

# set variables for entry boxes
weightP = StringVar()
heightF = StringVar()
heightI = StringVar()

# create three entry boxes
Entry(screen, font = myfont, width = 10, fg = "blue", textvariable = weightP).\
              grid(row = 0, column = 1)
Entry(screen, font = myfont, width = 10, fg = "blue", textvariable = heightF).\
              grid(row = 1, column = 1)
Entry(screen, font = myfont, width = 10, fg = "blue", textvariable = heightI).\
              grid(row = 2, column = 1)

# create a button
Button(screen, text = "Calculate BMI", font = myfont, width = 20, fg = "white",\
       bg = "green", command = getBMI).grid(row = 3, columnspan = 2, pady = 5) 

# set variable to print the result
result = StringVar()

# create another label screen to display the result
Label(screen, font = myfont, fg = "white", bg = "red", width = 20,\
      textvariable = result).grid(row = 4, columnspan = 2, pady = 5)

# main loop
screen.mainloop()

