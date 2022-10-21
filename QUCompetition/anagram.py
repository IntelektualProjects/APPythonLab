from itertools import permutations as p


def anagram_check(listed):
    pairs = []
    for value in listed:
        permutations = set([''.join(v) for v in p(value)])
        for z in permutations:
            if z in listed and z != value:
                pairs.append((value, z))
    return int(len(set(pairs)) / 2)


times = input()
ans = []
for x in range(1, int(times) + 1):
    possibilities = []
    words = input()
    if int(words) > 0:
        for y in range(1, int(words) + 1):
            possibilities.append(input())
        ans.append(anagram_check(possibilities))
    else:
        print(0)

for val in ans:
    print(val)
