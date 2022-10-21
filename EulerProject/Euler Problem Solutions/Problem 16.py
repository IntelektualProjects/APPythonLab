def exponent(base_number, power, total):
    result = base_number ** power
    digits = list(str(result))
    for added_digits in digits:
        total += int(added_digits)
    return total


print(exponent(2, 1000, 0))