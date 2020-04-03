print("*****highest test score****")

#create a list to store the test scores
lst = []
#prompt the user to enter the number of students
numStudent = int(input("how many students do you have?: "))

#this loop process all students
s = 0
while s < numStudent:
    print()
    print(f"student {s+1}")
    print("------------------")
    
    #process test scores for each student
    score = float(input(f"input test score: "))
    lst.append(score)
    
    #validate the score. the valid score is between 0 and 100
    while score < 0 or score > 100:
        score = float(input(f"input {t+1} score (0-100): "))
                
    #update LCV
    s += 1
    
print()   
print("the highest score is: ", max(lst))
print("the second highest score is: ", sorted(lst)[-2])

