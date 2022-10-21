import time
start = time.time()

pandigital_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
final = []


def pandigital_check(list_num):
    if sorted(list_num) == pandigital_list:
        return True
    return False


def multiple_generator(num):
    digit_list = []
    for x in range(1, 10):
        list_one = list(str(num * x))

        if '0' in list_one:
            return False

        digit_list.extend(list_one)

        if len(digit_list) >= 9:
            break

    old_list = ''.join(digit_list)
    digit_list = [int(i) for i in digit_list]

    if len(digit_list) == 9 and pandigital_check(digit_list):
        final.append(int(old_list))
        return True

    return False


for y in range(1, 10000):
    multiple_generator(y)

print(max(final))
end = time.time()
print("Time", end - start)