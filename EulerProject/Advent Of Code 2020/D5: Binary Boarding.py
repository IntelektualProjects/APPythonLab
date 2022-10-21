import math

file = open("seats.txt", "r")
data = file.read().split("\n")
file.close()


def lower_half(start, end):
    rate = end - start
    end = start + math.floor(.5 * rate)
    return start, end


def upper_half(start, end):
    rate = end - start
    start = start + math.ceil(.5 * rate)
    return start, end


# Part 1

pass_list = []

for seat in data:
    s, e = 0, 7
    rows = seat[0: 7]
    columns = seat[7:]
    for x in columns:
        if x == "R":
            s, e = upper_half(s, e)
        if x == "L":
            s, e = lower_half(s, e)
    column = s
    s, e = 0, 127
    for val in rows:
        if val == "F":
            s, e = lower_half(s, e)
        if val == "B":
            s, e = upper_half(s, e)

    pass_list.append((s * 8) + column)

print(max(pass_list))

# Part 2

for x in range(min(pass_list), max(pass_list)):
    if x not in pass_list:
        print(x)
