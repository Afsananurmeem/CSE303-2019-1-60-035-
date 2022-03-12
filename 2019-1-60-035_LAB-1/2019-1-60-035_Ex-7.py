
lst = []
 
n = int(input("Enter number of elements: "))
sum = 0

for i in range(0, n):
    lst.append(int(input("Number %d: " %(i+1))))
    sum += lst[i]

print("The sum is:",sum)

     