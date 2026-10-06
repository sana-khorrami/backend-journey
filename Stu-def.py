firstname=input("please enter your firstname:")
lastname= input("please enter your lastname:")
def calculate_age():
    x=2026-born_year
    print('age:',x)
born_year=int(input("please enter your born_year:"))
calculate_age()
city=input("your city:")
major=input("your major:")
score=int(input("please enter your score:"))
if score>=18:
    print("excellent")
elif score>=12 and score<=18:
    print("good")
else:
    print("failed!")