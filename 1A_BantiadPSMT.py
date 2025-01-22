print("——————————[ CONVERSION CALCULATOR]——————————")
print("Welcome User! How can I serve you.")
while True:
    print("Menu:\n[a] Area\n[b] Volume\n[c] Weight\n[d] Temperature\n[e] Length")
    choice0 = input("Choice: ")
    print("")

    if choice0 == "A" or choice0 == "a":
        print("Area:\n[1] Acre — Hectare\n[2] Square Foot — Square Yard")
        choice1 = input("Choice: ")

        while True:
            if choice1 == "1":
                print("\nAcre — Hectare")
                ans = float(input("Enter Acre: "))
                res = ans * 0.404
                print(f"{ans} Acre is %.2f Hectare(s)" %res)
                choice2 = input("\nDo you wish to CONTINUE Acre — Hectare conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

            if choice1 == "2":
                print("\nSquare Foot — Square Yard")
                ans = float(input("Enter Square Foot/Feet: "))
                res = ans / 9
                print(f"{ans} Square Foot/Feet is %.2f Square Yard(s)" %res)
                choice2 = input("\nDo you wish to CONTINUE Square Foot — Square Yard conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

    elif choice0 == "B" or choice0 == "b":
        print("Volume:\n[1] Milliliter - Liter\n[2] Pint — Gallon")
        choice1 = input("Choice: ")

        while True:
            if choice1 == "1":
                print("\nMilliliter - Liter")
                ans = float(input("Enter Milliliter(s): "))
                res = ans / 1000
                print(f"{ans} Milliliter(s) is %.2f Liter(s)" %res)
                choice2 = input("\nDo you wish to CONTINUE Milliliter - Liter conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

            if choice1 == "2":
                print("\nPint — Gallon")
                ans = float(input("Enter Pint(s): "))
                res = ans / 8
                print(f"{ans} Pint(s) is %.2f Gallon(s)" %res)
                choice2 = input("\nDo you wish to CONTINUE Pint — Gallon conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

    elif choice0 == "C" or choice0 == "c":
        print("Weight:\n[1] Pund — Kilogram\n[2] Gram — Carrat")
        choice1 = input("Choice: ")

        while True:
            if choice1 == "1":
                print("\nPund — Kilogram")
                ans = float(input("Enter Pund(s): "))
                res = ans / 2.205
                print(f"{ans} Pund(s) is %.2f Kilogram(s)" % res)
                choice2 = input("\nDo you wish to CONTINUE Pund — Kilogram conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

            if choice1 == "2":
                print("\nGram — Carrat")
                ans = float(input("Enter Gram(s): "))
                res = ans * 5
                print(f"{ans} Gram(s) is %.2f Carrat" % res)
                choice2 = input("\nDo you wish to CONTINUE Gram — Carrat conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

    elif choice0 == "D" or choice0 == "d":
        print("Temperature:\n[1] Celsius — Kelvin\n[2] Fahrenheit — Celsius")
        choice1 = input("Choice: ")

        while True:
            if choice1 == "1":
                print("\nCelsius — Kelvin")
                ans = float(input("Enter Celsius: "))
                res = ans + 273.15
                print(f"{ans} Celsius is %.2f Kelvin" % res)
                choice2 = input("\nDo you wish to CONTINUE Celsius — Kelvin conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

            if choice1 == "2":
                print("\nFahrenheit — Celsius")
                ans = float(input("Enter Fahrenheit: "))
                res = (ans - 32) * 5 / 9
                print(f"{ans} Fahrenheit is %.2f Celsius" % res)
                choice2 = input("\nDo you wish to CONTINUE Fahrenheit — Celsius conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

    elif choice0 == "E" or choice0 == "e":
        print("Length:\n[1] Inch — Yard\n[2] Mile — Light Year")
        choice1 = input("Choice: ")

        while True:
            if choice1 == "1":
                print("\nInch — Yard")
                ans = float(input("Enter Inch(es): "))
                res = ans / 36
                print(f"{ans} Inch(es) is %.2f Yard(s)" % res)
                choice2 = input("\nDo you wish to CONTINUE Inch — Yard conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

            if choice1 == "2":
                print("\nMile — Light Year")
                ans = float(input("Enter Mile(s): "))
                res = ans * 0.00000000000017011
                print(f"{ans} Mile(s) is {res} Light Year(s)")
                choice2 = input("\nDo you wish to CONTINUE Mile — Light Year conversion? [Y/N]: ")
                if choice2 == "N" or choice2 == "n":
                    break

    else:
        print("Invalid Input Choice!")

    choice3 = input("\nDo you wish to CONTINUE Conversion Calculator? [Y/N]: ")
    print("")
    if choice3 == "N" or choice3 == "n":
        print("......Exiting Program . . . GOODBYE!")
        break
