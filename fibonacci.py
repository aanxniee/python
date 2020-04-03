print("*****fibonacci*****")

#prompt the user to enter a number
number = int(input("enter a number: "))

#set the number as a fibos list
n = number + 1
fibos_num = [0, 1]
i = 1

#if the user input is 0, the fibonacci number is 0
if number == 0:
    print(f"the {number} term is: ", fibos_num[n-1])
    print("fibonacci series :  [0]")
    
#if the user input is 1 or 2, the fibonacci number is 1
elif n == 1 or n == 2:
    print(f"the{number}th fibonacci number is: ", fibos_num[n-1])
    print("fibonacci series : ", fibos_num)

#use the formula to calculate the nth term of the fibonacci
elif n>2:
    
    #this loop adds the fibonacci number into the fibos list
    while True:
        fib = fibos_num[i-1] + fibos_num[i]
        fibos_num.append(fib)
        
        if(len(fibos_num) == n):
            break
        else:
            i += 1
            
    print(f"the {number}th fibonacci number is {fibos_num[n-1]}")
    print("fibonacci series is: ", fibos_num)

else:
    print("error")
 
