

N = int(input("Enter number: "))

i = 1
sum = 0
while i < N+1:
    sum += i*i
    i+=1
    
print("The value of the series is:", sum)