import time
import math
start = time.time()


def abundant_check(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    if sum(list(set(divisors))) > n:
        return True
    return False


abundant_list = []

for value in range(12, 28124):
    if abundant_check(value):
        abundant_list.append(value)

sum_list = []
full_list = [i for i in range(1, 28124)]

for x in abundant_list:
    for y in abundant_list:
        if x + y <= 28124:
            sum_list.append(x + y)
sum_list = set(sum_list)
full_list = set(full_list)

print(sum(list(full_list - sum_list)))
end = time.time()
print("Time", end - start)
