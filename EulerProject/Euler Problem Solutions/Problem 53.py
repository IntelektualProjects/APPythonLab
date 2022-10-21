import time
import math
start = time.time()


def combinatoric(number_one, number_two):
    a = math.factorial(number_one)
    b = math.factorial(number_two)
    c = math.factorial(number_one - number_two)
    ans = a / (b * c)
    return ans


count = 0

for n in range(23, 101):
    for r in range(1, n + 1):
        if combinatoric(n, r) > 1000000:
            count += 1

end = time.time()
print("Time", end - start)
print(count)