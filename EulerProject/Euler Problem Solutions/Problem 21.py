import time
start = time.time()


def proper_divisors(num):
    list_one = []

    for x in range(1, num):
        if num % x == 0:
            list_one.append(x)
    return sum(list_one)


final = []
listed = []
for y in range(1, 10001):
    a = proper_divisors(y)
    b = proper_divisors(a)
    if y == b and a != b:
        final.append(a)
        final.append(b)

for z in final:
    if z not in listed:
        listed.append(z)

print(sum(listed))
end = time.time()
print("Time", end - start)