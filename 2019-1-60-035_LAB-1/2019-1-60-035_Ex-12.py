

def remove_characters(string, n):
    removed_string = ""
    for i in range(n, len(string)):
        removed_string += string[i]
    return removed_string


string = input("Enter string: ")
num = int(input("Enter removed number of string: "))
print("\nThe removed string is:", remove_characters(string,num))