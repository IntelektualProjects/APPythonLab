import time
start = time.time()


def solution_calculator(p):
    solution_list = []

    for x in range(1, p):
        for y in range(1, p - x):
            z = p - x - y
            a, b, c = sorted([x, y, z])
            if a ** 2 + b ** 2 == c ** 2:
                if sorted([x, y, z]) not in solution_list:
                    solution_list.append(sorted([x, y, z]))

    return len(solution_list)


max_num = 0
max_count = 0

for value in range(1, 1001):
    print(value)
    count = solution_calculator(value)
    if count > max_count:
        max_count = count
        max_num = value

print(max_num)
end = time.time()
print("Time", end - start)
