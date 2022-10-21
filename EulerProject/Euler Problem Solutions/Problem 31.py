import time
start = time.time()

count = 0
last_case = 1

for a in range(0, 3):
    for b in range(0, int(1 + ((200 - 100 * a) / 50))):
        for c in range(0, int(1 + ((200 - 100 * a - 50 * b) / 20))):
            for d in range(0, int(1 + ((200 - 100 * a - 50 * b - 20 * c) / 10))):
                for e in range(0, int(1 + ((200 - 100 * a - 50 * b - 20 * c - 10 * d) / 5))):
                    for f in range(0, int(1 + ((200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e) / 2))):
                        count += 1

print(count + last_case)
end = time.time()
print(end - start)