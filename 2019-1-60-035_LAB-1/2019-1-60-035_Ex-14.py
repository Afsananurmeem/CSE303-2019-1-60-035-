
def palindrome_checker_2019_1_60_035(strings):
    rev_string = strings[::-1]
    if strings == rev_string:
        return True
    else: return False


strings = input("Enter your string: ")
if palindrome_checker_2019_1_60_035(strings):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome!")
