def exponents():
    listed = []

    for a in range(1, 101):
        for b in range(1, 101):
            ans = a ** b
            value = 0
            for digits in str(ans):
                value = value + int(digits)
                listed.append(value)
    listed = max(listed)
    print(listed)


exponents()