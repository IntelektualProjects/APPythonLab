import time
from fractions import Fraction
start = time.time()


def digit_cancel_check(numerator, denominator):
    if numerator == denominator:
        return False

    n_list = list(str(numerator))
    d_list = list(str(denominator))
    ans = numerator / denominator

    if '0' in n_list and '0' in d_list:
        return False

    for x in n_list:
        if x in d_list:
            d_list.remove(x)
            n_list.remove(x)
            break
    else:
        return False

    try:
        if int(''.join(n_list)) / int(''.join(d_list)) == ans:
            return True
        return False
    except ZeroDivisionError:
        return False


final_list = []
n = 1
d = 1

count = 11
while count <= 99:
    for num in range(10, count + 1):
        if digit_cancel_check(num, count):
            final_list.append([num, count])

    if len(final_list) == 4:
        break

    count += 1

for y in final_list:
    n *= y[0]
    d *= y[1]

print(f"Final Fraction: {Fraction(n, d)}")
end = time.time()
print("Time ", end - start)
