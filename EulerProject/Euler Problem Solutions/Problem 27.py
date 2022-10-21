import time
start = time.time()


def prime_check(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


def max_primes(a, b):
    n = 0
    count = 0
    while True:
        ans = (n ** 2) + (a * n) + b
        if prime_check(ans):
            count += 1
            n += 1
        else:
            return count


solutions = 0
coefficients = []

for x in range(1, 1000):
    print(x)
    for y in range(1, 1001):
        listed = [max_primes(x, y), max_primes(-x, y), max_primes(-x, -y), max_primes(x, -y)]
        if max(listed) > solutions:
            solutions = max(listed)
            index = listed.index(max(listed))
            if index == 0:
                coefficients = [x, y]
            if index == 1:
                coefficients = [-x, y]
            if index == 2:
                coefficients = [-x, -y]
            if index == 3:
                coefficients = [x, -y]

print(coefficients[0] * coefficients[1])
end = time.time()
print("Time", end - start)
