import time
import math
start = time.time()


def triangle_num(num):
    total = 0

    for x in range(1, num + 1):
        total += x
    return total


def find_divisors(num):
    count = 0

    for i in range(1, round(math.sqrt(num) + 1)):
        if not num % i:
            count = count + 2
    return count


number = 1
value = 8

while True:
    number = triangle_num(value)
    if find_divisors(number) >= 500:
        end = time.time()
        print("Time", end - start)
        print(number)
        break
    else:
        value += 1