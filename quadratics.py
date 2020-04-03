print("*****quadratics calculator*****")
#ask user for values of a, b and c
a = eval(input("enter value for a: "))
b = eval(input("enter value for b: "))
c = eval(input("enter value for c: "))
#calculate the disc
disc = b**2 - 4 * a * c
if disc > 0:
    x1 = (-b + disc ** 0.5)/(2 * a)
    x2 = (-b - disc ** 0.5)/(2 * a)
    print(f"{x1: .1f}")
    print(f"{x2: .1f}")
elif disc == 0:
    x1 = (-b + disc ** 0.5)/(2 * a)
    print(f"{x1: .1f}")
else:
    print("there is no solution")
 
