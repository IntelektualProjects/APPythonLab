import time
import math
start = time.time()


def perfect_squares(num):
    square_list = []
    number = math.ceil(math.sqrt(1))
    n2 = number * number
    number = (number * 2) + 1

    while 1 <= n2 <= num:
        square_list.append(n2)
        n2 = n2 + number
        number += 2
    return square_list


def prime_check(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


def goldbachs_conjecture(num):
    squares = perfect_squares(num)
    counter = 0

    for x in squares:
        if prime_check(num - (2 * x)):
            counter += 1
            break

    if counter > 0:
        return True
    return False


def composite_check(num):
    if num <= 3:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return True
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return True
        i += 6
    return False


count = 1
while True:
    if composite_check(count) and count % 2 != 0:
        if not goldbachs_conjecture(count):
            print(count)
            end = time.time()
            print("Time", end - start)
            break
    count += 1
