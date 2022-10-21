import time
start = time.time()

num = 1
string_num = ""

while len(string_num) <= 1000000:
    string_num = string_num + str(num)
    num = num + 1

product = 1
list_num = [int(string_num[0]), int(string_num[9]), int(string_num[99]), int(string_num[999]), int(string_num[9999]),
            int(string_num[99999]), int(string_num[999999])]

for x in list_num:
    product = product * x

end = time.time()
print("Time", end - start)
print(product)