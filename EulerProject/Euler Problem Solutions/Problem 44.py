import time
import math
start = time.time()


def generate_pentagonal_numbers(n):
    return (n * (3 * n - 1)) / 2


def pentagonal_check(n):
    if (1 + math.sqrt(24 * n + 1)) % 6 == 0:
        return True
    return False


pentagon_list = [1]
count = 2

while True:
    num = generate_pentagonal_numbers(count)
    print(num)
    pentagon_list.append(num)
    for x in pentagon_list:
        if pentagonal_check(num + x) and pentagonal_check(num - x):
            print(abs(num - x))
            end = time.time()
            print("Time", end - start)
            break
    else:
        count += 1
        continue
    break
