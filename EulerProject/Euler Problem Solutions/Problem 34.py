import math


def digit_factorial():
    count = 3
    output = 0
    fact_sum = 0

    while True:
        for digit in str(count):
            fact_digit = math.factorial(int(digit))
            output = output + fact_digit
        if count == output:
            fact_sum = fact_sum + output
            print(fact_sum)
        else:
            count = count + 1
            output = 0


digit_factorial()
