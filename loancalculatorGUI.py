"""
Annie Cai
ICS2O1-04 Mr. Saleem
Loan Calculator GUI

1. Create three labels to display the annual interest rate, number of years and loan amount
2. Create three entry boxes to ask the user for their input
3. Cretae one button to call the function to calculate the payment
4. Calculate the monthly payment and total payment using the formula in a function
5. Create four labels to name and display the monthly payment and total payment
"""

from tkinter import *
import math

# Create a screen
screen = Tk()
screen.title("Loan Calculator")
screen.geometry("298x165")

"""
AMORTIZED LOAN PAYMENT FORMULA

monthly payment = p
total loan = a
periodic interest rate (annual rate divided by 12 months) = r
number of payment periods (numbber of years multiplied by 12 months) = n

p = a / (((1 + r) ** n) - 1) / (r * (1 + r) ** n)
"""

#----------------------------------------------------------
def getPayment():

    # Get the interest, year and amount from the entry box and convert it to a float
    interest = float(interestRate.get())
    year = float(numYears.get())
    amount = float(loanAmount.get())

    # Find the variables needed for the amortized loan payment formula
    a = amount
    r = float((interest/100) / 12)
    n = float(12 * year)

    # Calculate the monthly payment, set it as a variable and print it to the label
    monthly = a / ((((1 + r) ** n) - 1) / (r * (1 + r) ** n))
    print(monthlyPayment.set(f"$ {monthly:.2f}"))
    # Calculate the total payment, set it as a variable and print it to the label
    total = round(monthly, 2) * n
    print(totalPayment.set(f"$ {total:.2f}"))
#----------------------------------------------------------

# Create a font
myfont = "Times 12"

# Create five labels
Label(screen, font = myfont, text = "Annual Interest Rate").grid(row = 0, column = 1, sticky = W)
Label(screen, font = myfont, text = "Number of Years").grid(row = 1, column = 1, sticky = W)
Label(screen, font = myfont, text = "Loan Amount").grid(row = 2, column = 1, sticky = W)
Label(screen, font = myfont, text = "Monthly Payment").grid(row = 3, column = 1, sticky = W)
Label(screen, font = myfont, text = "Total Payment").grid(row = 4, column = 1, sticky = W)

# Set variables for entry boxes
interestRate = StringVar()
numYears = StringVar()
loanAmount = StringVar()

# Create three entry boxes
Entry(screen, font = myfont, textvariable = interestRate, justify = "right").grid(row = 0, column = 2)
Entry(screen, font = myfont, textvariable = numYears, justify = "right").grid(row = 1, column = 2)
Entry(screen, font = myfont, textvariable = loanAmount, justify = "right").grid(row = 2, column = 2)

# Create a button
Button(screen, font = myfont, text = "Compute Payment", command = getPayment).grid(row = 5, column = 2, sticky = E)

# Set variables for labels
monthlyPayment = StringVar()
totalPayment = StringVar()

# Create two labels to display the calculations
Label(screen, font = myfont, textvariable = monthlyPayment).grid(row = 3, column = 2, sticky = E)
Label(screen, font = myfont, textvariable = totalPayment).grid(row = 4, column = 2, sticky = E)

screen.mainloop()
