def prime_find_2019_1_60_176( num ):
    if num < 1:
        return False
    
    for i in range(2, int(num/2) + 1, 1):
        if num % i == 0:
            return False
        
    return True

num = int(input("enter the number: "))

if prime_find_2019_1_60_176(num) == True:
    print("The number %d is prime!" %num)
else:
    print("The number %d is not prime!" %num)