import time
start = time.time()


def even(num):
    answer = num / 2
    return answer


def odd(num):
    ans = (3 * num) + 1
    return ans


count_list = []

for number in range(2, 1000000):
    value = number
    counter = 0
    print(number)
    while True:
        if value % 2 == 0:
            value = even(value)
            counter += 1
        if value == 1:
            count_list.append(counter)
            break
        if value % 2 != 0:
            value = odd(value)
            counter = counter + 1


end = time.time()
print("Time", end - start)
print(count_list.index(max(count_list)) + 2)