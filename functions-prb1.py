# write a program to print the greatest of three number using functions.
def greatestnumber():
    n1=int(input("enter your number-1:"))
    n2=int(input("enter your number-2:"))
    n3=int(input("enter your number-3:"))
    if(n1>n2 and n1>n3):
        print(f"{n1} is greatest")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is greatest")
    elif(n3>n1 and n3>n2):
        print(f"{n3} is greatest")

greatestnumber()


