g1 = int(input("Enter 1st Grade: "))
g2 = int(input("Enter 2nd Grade: "))
g3 = int(input("Enter 3rd Grade: "))

grade_SUM = g1 + g2 + g3
ave = grade_SUM / 3

if ave <= 50 or ave > 100:
    print("Invalid Grade!")

elif ave >= 98:
    print("Astonishing! your with HIGHEST HONORS.")

elif ave >= 95:
    print("Outstanding! your with HIGH HONORS.")

elif ave >= 90:
    print("Awesome! your with HONORS.")

elif ave >= 75:
    print("Congratulations! you PASSED.")

else:
    print("Sorry, you FAILED!")