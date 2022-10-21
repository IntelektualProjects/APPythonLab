import time
start = time.time()


def num_digit(num):
    digits_one = []
    digits_two = []
    digits_three = []
    digits_four = []
    digits_five = []
    digits_six = []

    for digit in str(num):
        digits_one.append(int(digit))
    digits_one = sorted(digits_one)

    for digit in str(num * 2):
        digits_two.append(int(digit))
    digits_two = sorted(digits_two)

    for digit in str(num * 3):
        digits_three.append(int(digit))
    digits_three = sorted(digits_three)

    for digit in str(num * 4):
        digits_four.append(int(digit))
    digits_four = sorted(digits_four)

    for digit in str(num * 5):
        digits_five.append(int(digit))
    digits_five = sorted(digits_five)

    for digit in str(num * 6):
        digits_six.append(int(digit))
    digits_six = sorted(digits_six)

    if digits_one == digits_two == digits_three == digits_four == digits_five == digits_six:
        return True
    else:
        return False


count = 1

while True:
    if num_digit(count):
        end = time.time()
        print("Time", end - start)
        print(count)
        break
    else:
        count = count + 1
