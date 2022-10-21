import time
from itertools import permutations
start = time.time()


def digit_break(number):
    num_list = number
    one = num_list[1:4]
    two = num_list[2:5]
    three = num_list[3:6]
    four = num_list[4:7]
    five = num_list[5:8]
    six = num_list[6:9]
    seven = num_list[7:10]

    if int(one) % 2 != 0:
        return False
    if int(two) % 3 != 0:
        return False
    if int(three) % 5 != 0:
        return False
    if int(four) % 7 != 0:
        return False
    if int(five) % 11 != 0:
        return False
    if int(six) % 13 != 0:
        return False
    if int(seven) % 17 != 0:
        return False
    return True


final = []
ans = 0

permutation_list = permutations(str("0123456789"))
for p in list(permutation_list):
    final.append(''.join(p))

for num in final:
    if digit_break(num):
        ans += int(num)

print(ans)
end = time.time()
print("Time", end - start)