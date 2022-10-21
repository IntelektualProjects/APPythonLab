import time
start = time.time()


def prime_check(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


def digit_count(num):
    limit = 0
    for x in num:
        limit += 1
    return limit


def reverse_string(num):
    string = ""
    for a in str(num):
        string = a + string
    return string


def right_to_left(num):
    num_list = []
    num = reverse_string(num)
    counted = digit_count(num)

    for z in range(0, counted):
        number = num[z:]
        num_list.append(reverse_string(number))

    for v in num_list:
        if not prime_check(int(v)):
            return False
    return True


def left_to_right(num):
    num_list = []
    num = str(num)
    counter = digit_count(num)

    for y in range(0, counter):
        number = num[y:]
        num_list.append(number)

    for item in num_list:
        item = int(item)
        if not prime_check(item):
            return False
    return True


count = 10
final_list = []

while True:
    if left_to_right(count) and right_to_left(count):
        final_list.append(count)
        print(len(final_list))
        count += 1
    else:
        count += 1

    if len(final_list) == 11:
        print(sum(final_list))
        end = time.time()
        print("Time", end - start)
        break
