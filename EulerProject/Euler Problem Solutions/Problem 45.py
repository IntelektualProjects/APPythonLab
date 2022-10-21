import time
import math
start = time.time()


def triangle_number(num):
    return (num * (num + 1)) / 2


def pentagonal_number(num):
    if (1 + math.sqrt(24 * num + 1)) % 6 == 0:
        return True
    return False


def hexagonal_number(num):
    if (1 + math.sqrt(8 * num + 1)) % 4 == 0:
        return True
    return False


count = 286
while True:
    triangle = triangle_number(count)
    if pentagonal_number(triangle) and hexagonal_number(triangle):
        print(triangle)
        end = time.time()
        print("Time", end - start)
        break
    else:
        count += 1