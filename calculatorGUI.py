from tkinter import *

screen = Tk()
screen.geometry("400x400")
screen.title("Calculator")

#****************************************************
def calculate():
    inp = userInput.get()
    answer = eval(inp)

    result.set(f"{inp} = {answer}")

def clear():
    userInput.set("")
    result.set("")
#****************************************************

# create a font
myfont = "Helvetica 14"

# set the users input as a variable
userInput = StringVar()
# create an entry screen for the input
Entry(screen, width = 15, font = myfont, textvariable = userInput).\
              grid(row = 0, columnspan = 2, pady = 15, padx = 15)

# create a button to calculate the input
Button(screen, text = "Enter", width = 10, font = myfont, bg = "green",\
       fg = "white", command = calculate).grid(row = 1, column = 0, padx = 20)

# create a button to clear the input and answer
Button(screen, text = "Clear", width = 10, font = myfont, bg = "black",\
       fg = "white", command = clear).grid(row = 1, column = 1)

# set the result as a variable
result = StringVar()
# create an entry screen to display the answer
Entry(screen, width = 20, font = myfont, fg = "red", textvariable = result).\
              grid(row = 2, columnspan = 2, pady = 15, padx = 20)

screen.mainloop()

