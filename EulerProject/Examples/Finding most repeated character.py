# Finding most repeated character in a string
def most_repeated(text):
    char_list = []
    num_list = []
    list1 = list(text)

    for x in list1:
        z = x
        x = list1.count(x)
        if z not in char_list:
            char_list.append(z)
        num_list.append(x)
    listed = dict(zip(char_list, num_list))

    sorted_dict = sorted(listed.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_dict[0]


print(most_repeated("Hello there"))