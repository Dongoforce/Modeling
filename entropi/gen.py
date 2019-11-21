import random

file = open("number.txt", "w")
for i in range(1, 20001):
    numbers = [f"{random.randint(10000, 99999)}" for i in range(10)]
    line = " ".join(numbers)
    file.write(line + ("\n" if i != 20000 else ""))
file.close()