def pandigital_check(num):
    digit_count = 0
    digit_list = []
    count_list = []

    for digit in str(num):
        digit_count += 1
        digit_list.append(int(digit))

    digit_list = sorted(digit_list)
    for value in range(1, digit_count + 1):
        count_list.append(value)

    if count_list == digit_list:
        return True
    return False


def prime(num):
    for val in range(2, num):
        if num % val == 0:
            return False
    return True


count = 1
largest = 0

while True:
    if pandigital_check(count) and prime(count):
        largest = count
        print(largest)
        count += 1
    else:
        count += 1