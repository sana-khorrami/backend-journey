firstname=input("please enter your firstname:")
lastname= input("please enter your lastname:")
age=int(input("please enter your age:"))
city=input("your city:")
major=input("your major:")
score=int(input("please enter your score:"))
if score>=18:
    print("excellent")
elif score>=12 and score<=18:
    print("good")
else:
    print("failed!")