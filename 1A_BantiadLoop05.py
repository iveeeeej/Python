no = int(input("Enter a Number for Multiplication Table: "))

for num in range(1, 11):
    pro = no * num
    print(str(no) + " × " + str(num) + " = " + str(pro))