#write a program to calculate factorial of n numbers
n=int(input("enter your number:"))
def factorial(n):
    if(n==1):
        return 1
    else:
         return n * factorial(n-1)

   
print(factorial(n))

