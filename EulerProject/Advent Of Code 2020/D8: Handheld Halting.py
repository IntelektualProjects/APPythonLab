file = open("instructions.txt", "r")
data = file.read().split("\n")
file.close()


def read_instruction(string):
    command, increment = string.split(" ")
    if increment[0] == "+":
        increment = int(increment[1:])
    else:
        increment = -1 * int(increment[1:])
    return command, increment


traveled = []
accumulator = 0
i = 0

while i not in traveled:
    for x in range(i, len(data)):

        traveled.append(i)
        call, num = read_instruction(data[x])
        if call == "acc":
            accumulator += num
            i += 1
            break
        if call == "jmp":
            i += num
            break
        if call == "nop":
            i += 1
            break
print(accumulator)

