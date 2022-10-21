import time
start = time.time()

count = 0


for x in range(1, 10):
    power = 1
    while True:
        if power == len(str(x ** power)):
            count += 1
        else:
            break
        power += 1

print(count)
end = time.time()
print("Time", end - start)