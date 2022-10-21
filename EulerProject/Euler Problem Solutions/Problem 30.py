def digit_fifth(num):
    ans = 0
    for digit in str(num):
        ans = ans + (int(digit) ** 5)

    if ans == num:
        return True
    return False


count = 2
output = 0

while True:
    if digit_fifth(count):
        output += count
        print(output)
        count += 1
    else:
        count += 1