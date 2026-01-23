#convert from celsius to fahrenheit..

def conversion():
    C = float(input("enter your degree in celsius:"))
    F = (C * 9/5) + 32
    print(f"the degree in fahrenheit is:{F}")

conversion()