print("*****aqua park calculator*****")

#ask the user for the number of adult tickets needed
adult_tickets = int(input("enter the amount of adult tickets needed: "))
#ask the user for the number of child tickets needed
child_tickets = int(input("enter the amount of child tickets needed: "))

#assign variables
adultPrice = 15
childPrice = 11

#calculate price
total = adult_tickets * adultPrice + child_tickets * childPrice

if total > 50:
    print("you qualify for a 5% discount")
    #calculate the discounted price
    discountedTotal = total - total * 0.05
    print(f"your total is ${discountedTotal:.2f}")
else:
    print(f"your total is ${total}")
