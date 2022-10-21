file = open("passwords.txt", "r")
data = file.read().split("\n")

counter = 0


def read_range(string):
    start, end = string.split("-")
    return int(start), int(end)


# Part 1
for part in data:
    key, code = part.split(": ")
    ranged, letter = key.split(" ")
    minimum = read_range(ranged)[0]
    maximum = read_range(ranged)[1]
    count = 0

    for x in code:
        if x == letter:
            count += 1

    if maximum >= count >= minimum:
        counter += 1

print(counter)

# Part 2
counter_two = 0

for part in data:
    key, code = part.split(": ")
    ranged, letter = key.split(" ")
    index_one = read_range(ranged)[0] - 1
    index_two = read_range(ranged)[1] - 1
    count = 0

    if code[index_one] == letter:
        count += 1
    if code[index_two] == letter:
        count += 1

    if count == 1:
        counter_two += 1
print(counter_two)
