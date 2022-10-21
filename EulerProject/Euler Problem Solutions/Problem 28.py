import time
start = time.time()

limit = 1002001

odd_list = []
for x in range(1, limit + 1):
    if x % 2 != 0:
        odd_list.append(x)


i = 0
gap = 1
ans = 1
while odd_list[i] != limit:
    for corner in range(4):
        i += gap
        ans += odd_list[i]
    gap += 1

print(ans)
end = time.time()
print("Time", end - start)