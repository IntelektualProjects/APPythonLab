import time
from itertools import permutations
import math
start = time.time()


def sieve(limit):
    prime_list = [True for numbers in range(1, limit + 1)]
    prime_list[0] = False
    prime_list[1] = False

    for number in range(2, int(math.sqrt(limit) + 1)):
        double = number * 2
        while double < limit:
            prime_list[double] = False
            double += number

    output_list = []

    for valu in range(limit):
        if prime_list[valu]:
            output_list.append(valu)
    return output_list


def is_sequence(list_one):
    delta = list_one[1] - list_one[0]
    for ind in range(len(list_one) - 1):
        if not (list_one[ind + 1] - list_one[ind] == delta):
            return False
    return True


prime = sieve(9999)
listed = []
final = []

for value in prime:
    if len(str(value)) == 4:
        listed.append(value)

for x in listed:
    permute = permutations(str(x))
    permute_list = []
    final.clear()
    count = 0

    for p in list(dict.fromkeys(permute)):
        joined = ''.join(p)
        if joined[0] != '0':
            permute_list.append(int(joined))

    for y in permute_list:
        if y in listed:
            count += 1
            final.append(y)
        if count == 3:
            final = sorted(final)
            if is_sequence(final):
                print(final)
                end = time.time()
                print("Time", end - start)
                break