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
    return len(set(end_list)) == 4


count = 1
final = []
while True:
    one = prime_factors(count)
    two = prime_factors(count + 1)
    three = prime_factors(count + 2)
    four = prime_factors(count + 3)
    if one is True and two is True and three is True and four is True:
        print(count)
        end = time.time()
        print("Time", end - start)
        break
    else:
        count += 1