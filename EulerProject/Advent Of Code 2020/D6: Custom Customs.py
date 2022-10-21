file = open("groups.txt", "r")
original = file.read().split("\n\n")
data = [x.replace("\n", "") for x in original]
file.close()

# Part 1
count = 0
for i in data:
    count += len(set(i))
print(count)


# Part 2
output = 0
data = [x.replace("\n", " ") for x in original]
for i in data:
    final_count = 0
    counter = {}
    people = len(i.split(" "))
    for j in i:
        counter[j] = counter.get(j, 0) + 1
    for value in counter:
        if counter[value] == people:
            final_count += 1
    output += final_count
print(output)