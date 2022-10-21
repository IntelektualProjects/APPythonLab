file = open("values.txt", "r")
data = file.read().split("\n")
file.close()

for x in data:
    for y in data:
        if int(x) + int(y) == 2020:
            print(int(x) * int(y))
            break
    else:
        continue
    break

for x in data:
    for y in data:
        for z in data:
            if int(x) + int(y) + int(z) == 2020:
                print(int(x) * int(y) * int(z))
                break
        else:
            continue
        break
