n = 7
i = 0

while i >= 0:
    one_b = (6 + n) / (6 * n)
    if one_b.is_integer():
        print(n + one_b)
        break
    else:
        n += 1
