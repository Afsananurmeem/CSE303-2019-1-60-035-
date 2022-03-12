def secound_largest_number_2019_1_60_035(lst):
    large = lst[0]
    secound_large = lst[0]
    for l in lst:
        if l > secound_large:
            if l > large:
                secound_large = large
                large = l
            else: secound_large = l
    return secound_large
            
lst = []
 
n = int(input("Enter number of elements: "))

for i in range(0, n):
    lst.append(int(input("Number %d: " %(i+1))))

print()
print("Secound largest number:", secound_largest_number_2019_1_60_035(lst))
