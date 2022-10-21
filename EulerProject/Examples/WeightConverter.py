weight = input(" What is your weight? ")
conversion = input("pounds(L) or kilograms(k)? ")


if conversion.upper() == "K":
    weight = int(weight) / .45
    print(f"{weight} Pounds")
elif conversion.upper() == "L":
    weight = int(weight) * .45
    print(f"{weight} kilograms")
else:
    print("error")