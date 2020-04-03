print("Processing Employee Hours")

# open the file for reading
file = open("employeeHours.txt", "r")

for employee in file: # read each line and put it in a list
    employee = employee.strip()
    employee = employee.split()

    total = 0 # set the total of hours worked to 0
    # this loop runs until the number of times worked by the employee is reached
    for i in range(1, len(employee)): 
        hour = float(employee[i]) # find the hours and turn it into a float
        total += hour # add the hours to the total

    print("total hours worked by {}: {}".format(employee[0], total))

