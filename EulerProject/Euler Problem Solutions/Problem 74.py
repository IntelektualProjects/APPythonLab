import time
import math
start = time.time()


def digit_factorial(num):
    solution = 0
    for x in str(num):
        solution += math.factorial(int(x))
    return solution


def repeat_chain(num):
    listed = []
    ans = digit_factorial(num)
    if ans == num:
        return 0
    else:
        while ans != num:
            listed.append(ans)
            ans = digit_factorial(ans)
            if ans in listed:
                break
        return len(listed) + 1


output = 0

for number in range(1, 1000001):
    print(number)
    if repeat_chain(number) == 60:
        output += 1

print(output)
end = time.time()
print("Time", end - start)