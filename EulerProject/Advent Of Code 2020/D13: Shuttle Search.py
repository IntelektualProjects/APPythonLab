file = open("ShuttleTimes.txt", "r")
number, timings = file.read().split("\n")
file.close()
timings = list(set(timings.split(",")))
timings.remove("x")
timings = list(map(int, timings))
number = int(number)

# Part 1

lowest_id = 0
minutes = number

for x in timings:
    ans = x
    while ans < number:
        ans += x
    if ans - number < minutes:
        minutes = ans - number
        lowest_id = x
print(lowest_id * minutes)

# Part 2

file = open("ShuttleTimes.txt", "r")
number, timings = file.read().split("\n")
file.close()
timings = timings.split(",")

ids = []

for value in timings:
    if value != "x":
        ids.append((int(value), timings.index(value)))

print(ids)

i = 1

while True:
    count = 0
    for x in ids:
        if (i + x[1]) % x[0] == 0:
            count += 1
    if count == len(ids):
        print(i)
        break
    else:
        print(i)
        i += 1
