password = input("Enter your password: ")

if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
    print("Strong password")
else:
    print("Weak password")
