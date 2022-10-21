import time
start = time.time()


def is_bouncy(num):
    digits = list(str(num))
    if digits == sorted(digits) or digits == sorted(digits, reverse=True):
        return False
    return True


count = 100
bouncy_count = 0

while True:
    if is_bouncy(count):
        bouncy_count += 1
    if bouncy_count / count == .99:
        break
    count += 1

print(count)
end = time.time()
print("Time", end - start)
