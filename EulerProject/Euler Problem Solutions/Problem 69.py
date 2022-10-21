import time
import math
start = time.time()


def prime_factors(num):
    end_list = []

    while num % 2 == 0:
        end_list.append(2),
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            end_list.append(i)
            num = num / i
    if num > 2:
        end_list.append(num)
    return set(end_list)


def phi(num):
    prime_list = prime_factors(num)

    for p in prime_list:
        num *= (1.0 - (1.0 / float(p)))
    return round(num)


maxed = 0
n = 0
for y in range(1, 1000000):
    print(y)
    answer = y / phi(y)
    if answer > maxed:
        maxed = answer
        n = y

print(n)
end = time.time()
print("Time", end - start)