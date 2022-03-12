
string = input("Enter your string: ")
given_string = "CSE303"
count = 0
for i in range(0,len(string)):
    if string[i:i+len(given_string)] == given_string:
        count += 1
print("The count of the substring “CSE303” is: ", count)
