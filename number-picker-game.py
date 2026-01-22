#random number-picker
import random
computer=random.randint(1,100)
user=int(input("input your number:"))
if(user==computer):
    print("your guess is correct")
else:
    print(f"computer chose {computer} ")
    print("try again")
    


