num = [max([j for j in range(1, 10) if i % j == 0]) for i in range(1, 1001)]
print("The highest single digit any of the numbers is divisible by in between 1 - 1000:")
print(num)
