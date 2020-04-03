print("*****student average*****")

numStudent = int(input("how many students do you have?: "))

#this loop process all students
s = 0
while s < numStudent:
    print()
    print(f"student {s+1}")
    print("------------------")
    
    #process test scores for each student
    numTests = int(input("how many tests does this student have?: "))
    
    t = 0
    total = 0 #test scores accumulator
    while t < numTests:
        score = int(input(f"input test {t+1} score: "))
        
        #validate the score. the valid score is between 0 and 100
        while score < 0 or score > 100:
            score = int(input(f"input {t+1} score (0-100): "))
            
        total += score
        #update lcv
        t += 1
        
    #calculate and display average
    average = total / numTests
    print(f"the average for student {s + 1} is {average}%")
    
    #update lcv
    s += 1
 
