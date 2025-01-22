sum = 0
for num in range(1, 11):
    if(num % 2 == 1):
        print(str(num))
        sum += num

print("Sum of odd nos. in range: ", sum)