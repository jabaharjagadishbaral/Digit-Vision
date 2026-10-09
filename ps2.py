for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


numbers = [4, 8, 15, 16, 23, 42]

total = 0

for num in numbers:
    total = total + num

print("Sum =", total)