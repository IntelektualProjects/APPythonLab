import math


def factorial_sum(base, output):
    output = math.factorial(base)

    return output


def digit_addition(value, output):
    value = str(value)
    for digits in value:
        output += int(digits)
    return output


step_one = factorial_sum(100, 0)
step_two = digit_addition(step_one, 0)
print(step_two)