
def productSum (a,b):
    if a*b > 1000:
        print("The sum is:", a+b)
    else:
        print("The product is:", a*b)

a = int(input("Enter 1st integer: "))
b = int(input("Enter 2nd integer: "))

print()
productSum(a, b)