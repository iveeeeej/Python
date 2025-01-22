string = input("Enter a String: ")

digits = letters = 0

for i in string:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1

print("Number of letters: ", letters)
print("Number of digits: ", digits)