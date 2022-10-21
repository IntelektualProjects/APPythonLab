import time
from itertools import permutations
start = time.time()

listed = []

permute = permutations("0123456789")

for p in list(permute):
    listed.append(int(''.join(p)))

final = sorted(listed)[999999]

print(final)
end = time.time()
print("Time", end - start)