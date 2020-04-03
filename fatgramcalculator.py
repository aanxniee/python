print("*****fat gram calculator*****")
#ask the user for the number of calories and fat grams
calories = float(input("enter the number of calories in the food: "))
fatGrams = float(input("enter the number of fat grams in the food: "))

#one fat gram has 9 calories
fatCalories = fatGrams * 9

if calories < fatCalories:
    print("error, the calories or fat grams were incorrectly entered")
elif calories > 0 and fatGrams > 0:
    #calculate the percent of calories from fat
    percentage = fatCalories / calories * 100
    print(f"the percentage of calories from fat is {percentage:.2f}%")
    if percentage < 30:
        print("the food is low in fat")
else:
    print("error, the calories or fat grams were incorrectly entered")
