#check if the string is palindrome or not
pal=input("enter your string:")
lap=pal[::-1]

if(pal==lap):
    print("it is a palindrome")
else:
    print("it is not a palindrome")