import time
import math
start = time.time()


data = open('bases', 'r')
data_list = data.read().split('\n')
data.close()

largest = 0
count = 0
final = 0

for x in data_list:
    base, exp = x.split(',')
    ans = int(exp) * math.log10(int(base))
    count += 1
    if ans > largest:
        largest = ans
        final = count


print(final)