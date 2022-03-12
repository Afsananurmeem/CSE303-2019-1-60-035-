
def oddFromFirst_evenFromSecound(lst1,lst2):
    lst = []
    for i in lst1:
        if i % 2 != 0:
            lst.append(i)
    for i in lst2:
        if i % 2 == 0:
            lst.append(i)

    return lst

def lstInput(lst,n):
    for i in range(0, n):
        lst.append(int(input("Number %d: " %(i+1))))
    return lst



lst1 = []
n = int(input("Enter number of elements: "))
lst1 = lstInput(lst1,n)

lst2 = []
m = int(input("Enter number of elements: "))
lst2 = lstInput(lst2,m)

print("The list is: ", oddFromFirst_evenFromSecound(lst1,lst2))



    