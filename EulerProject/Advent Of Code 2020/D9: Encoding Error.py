file = open("XMASEncoding.txt", "r")
data = file.read().split("\n")
file.close()

data = list(map(int, data))
target_num = 0

# Part 1

for x in range(25, len(data) - 24):
    num = data[x]
    factors = data[x - 25: x]
    count = 0
    for y in factors:
        if num - y not in factors:
            count += 1
    if count == 25:
        print(num)
        target_num = num
        break

# Part 2

for x in range(25, len(data) - 24):
    total = 0
    num = data[x]
    numbers = []
    for y in data[x:]:
        if total > target_num:
            break
        if total == target_num and len(numbers) >= 2:
            print(max(numbers) + min(numbers))
            break
        total += y
        numbers.append(y)

