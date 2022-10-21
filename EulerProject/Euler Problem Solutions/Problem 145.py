import time
start = time.time()


def reverse(num):
    num = str(num)
    return ''.join(reversed(num))


def odd_check(num):
    switch = reverse(num)
    if switch[0] == "0":
        return False
    value = str(num + int(switch))

    for x in value:
        if int(x) % 2 == 0:
            return False
    return True


count = 0
for number in range(1, 1000000000):
    if odd_check(number):
        print(count)
        count += 1

print(count)
end = time.time()
print("Time", end - start)