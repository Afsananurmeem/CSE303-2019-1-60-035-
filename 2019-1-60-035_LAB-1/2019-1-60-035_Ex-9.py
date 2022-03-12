
def largest_number_2019_1_60_035(lst):
    x = lst[0]
    for l in lst:
        if l > x:
            x = l
    return x

def smallest_number_2019_1_60_035(lst):
    x = lst[0]
    for l in lst:
        if l < x:
            x = l
    return x

lst = []
 
n = int(input("Enter number of elements: "))

for i in range(0, n):
    lst.append(int(input("Number %d: " %(i+1))))

print()
print("largest_number:", largest_number_2019_1_60_035(lst))
print("smallest_number:", smallest_number_2019_1_60_035(lst))
    
    
    
    
    
    
    
    