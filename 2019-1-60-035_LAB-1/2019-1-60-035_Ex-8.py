
lst = []
n = int(input("Enter number of elements: "))
sum = 0

for i in range(0, n):
    lst.append(int(input("Number %d: " %(i+1))))
    if i % 2 == 0:
        sum += lst[i]
        
print()
print("The sum of the even-indexed elements:",sum)