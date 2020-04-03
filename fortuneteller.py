print("*****fortune teller app*****")
print("""i am a fortune teller. look into my crystal screen and enter 4 careers you would like to have. for example,

chef
FBI agent
astronaut
app developer

then i will predict what you will be
""")

#ask the user for 4 careers
career1 = input("career choice 1: ")
career2 = input("career choice 2: ")
career3 = input("career choice 3: ")
career4 = input("career choice 4: ")

#randomly select a career
import random
randomNumber = random.randint(1,4)
if randomNumber == 1:
    print(f"you will be a {career1}")
elif randomNumber == 2:
    print(f"you will be a {career2}")
elif randomNumber == 3:
    print(f"you will be a {career3}")
else:
    print(f"you will be a {career4}"
