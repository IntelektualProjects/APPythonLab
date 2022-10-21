import math
import time
start = time.time()


def eratosthenes_sieve(limit):
    prime_list = [True for numbers in range(1, limit + 1)]
    prime_list[0] = False
    prime_list[1] = False

    for num in range(2, int(math.sqrt(limit) + 1)):
        double = num * 2
        while double < limit:
            prime_list[double] = False
            double += num

    output_list = []

    for value in range(limit):
        if prime_list[value]:
            output_list.append(value)
    return output_list


def prime_check(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


primes = eratosthenes_sieve(1000000)
length = 0
largest = 0
last_val = len(primes)

for x in range(len(primes) + 1):
    for y in range(x + length, last_val):
        solution = sum(primes[x:y])
        if solution < 1000000:
            if prime_check(solution):
                length = y - x
                largest = solution
        else:
            last_val = y + 1
            break
print(largest)
end = time.time()
print("Time", end - start)