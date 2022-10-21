def sequenced_powers(limit):
    list_one = []
    list_two = []
    output = 0

    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            ab = a ** b
            list_one.append(ab)

    for value in list_one:
        if value not in list_two:
            list_two.append(value)
            output = output + 1

    return output


print(sequenced_powers(100))
