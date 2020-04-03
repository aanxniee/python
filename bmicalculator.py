print("*****body mass index*****")
#ask user for their weight and height
weight = float(input("enter your weight in pounds: "))
height = float(input("enter your height in inches: "))
#calculate the BMI
bmi = (weight * 702) / (height * height) 
print(f"your BMI is: {bmi:.2f}")

if bmi > 25:
    print("you are overweight")
elif bmi < 25 and bmi > 18.5:
    print("your weight is optimal")
else:
    print("you are underweight")
