import time
start = time.time()

# open the names file
file = open("names.txt", "r")
data = file.read()
file.close()

# makes alphabetical list of names from file as "data"
data_string = ""

for comma in data:
    if comma == '"':
        comma = ""
    else:
        data_string = data_string + comma

data = sorted(data_string.split(","))

# dictionary for alphabetical value
alphabet_dict = {}
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split(" ")

placement_list = []
for item in range(1, 27):
    placement_list.append(item)

for x in alphabet:
    for y in placement_list:
        alphabet_dict[x] = y
        placement_list.remove(y)
        break
# alphabetical value function


def alphabet_value(name):
    count = 0

    for value in name:
        letter = alphabet_dict[value]
        count = count + letter
    return count


# main program starts here
total = 0

for x in data:
    val = int(data.index(x) + 1) * alphabet_value(x)
    total = total + val

end = time.time()
print("Time", end - start)
print(total)