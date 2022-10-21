import time
import math
start = time.time()

file = open("words", "r")
data = file.read()
file.close()

string = ""
for item in data:
    if item == '"':
        item = ""
    else:
        string = string + item
data = string.split(",")

# alphabet / number dictionary
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


def word_count(word):
    count = 0
    for letter in word:
        value = alphabet_dict[letter]
        count = count + value
    return count


def triangle_num_check(number):
    if number < 0:
        return False
    ans, n = 0, 1
    while ans <= number:
        ans = ans + n
        if ans == number:
            return True
        n += 1
    return False


counter = 0
for file_word in data:
    valu = word_count(file_word)
    if triangle_num_check(valu):
        counter = counter + 1
end = time.time()
print("Time", end - start)
print(counter)
