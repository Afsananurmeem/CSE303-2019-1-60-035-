num = [i for i in range(1, 1001) if True in [True for j in range(2, 10) if i % j == 0]]
print("The numbers from 1–1000 that are divisible by any single digit besides 1 (2–9) are:")
print(num)
