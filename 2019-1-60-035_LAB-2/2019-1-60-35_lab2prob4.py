def filterVowels(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if string not in vowels:
        return True
    else:
        return False


string = "Practice Problems to Drill List Comprehension in Your Head."
filteredVowels = filter(filterVowels, string)
print('After remove all of the vowels: ', end="")
for vowel in filteredVowels:
    print(vowel, end="")
