import time
start = time.time()


def digit_sum(no):
    return 0 if no == 0 else int(no % 10) + digit_sum(int(no / 10))


def power_check(num):
    listed = []
    for x in range(2, 11):
        if digit_sum(num ** x) == num:
            listed.append(num ** x)
    return listed


final = []

for y in range(2, 101):
    list_one = power_check(y)
    if len(list_one) > 0:
        for z in list_one:
            if z not in final:
                final.append(z)

print(sorted(final)[29])
end = time.time()
print("Time", end - start)