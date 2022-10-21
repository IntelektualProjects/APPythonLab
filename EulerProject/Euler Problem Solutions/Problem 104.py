import time
start = time.time()


base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def first_digits(num):
    num = list(str(num))[0:9]
    digits = []

    for x in num:
        digits.append(int(x))

    if sorted(digits) == base_list:
        return True
    return False


def last_digits(num):
    num = list(str(num))[-9:]
    digits = []

    for x in num:
        digits.append(int(x))

    if sorted(digits) == base_list:
        return True
    return False


count = 2

first_num = 1
second_num = 1
third_num = 0

while True:
    third_num = first_num + second_num
    first_num = second_num
    second_num = third_num
    count += 1
    print(count)
    if first_digits(third_num) and last_digits(third_num):
        print(count)
        end = time.time()
        print("TIme", end - start)
        break
