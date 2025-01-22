for num0 in range(1, 11):
    print(num0, end=" ")

even = 0
odd = 0

for num in range(1, 11):
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nNumber of even numbers: ", even)
print("Number of odd numbers: ", odd)

