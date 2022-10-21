def calculate(base, power):
    number = (base ** power)
    number_step = number * 28433
    number_step2 = number_step + 1
    numbers = str(number_step2)
    print("step one complete")
    return numbers


def reverse_string(numbers):
    string = ""
    for i in numbers:
        string = i + string
    return string


calc = calculate(2, 7830457)
reversed_string = reverse_string(calc)
print(reversed_string[0:10])
