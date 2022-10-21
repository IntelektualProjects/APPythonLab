import time
import math
start = time.time()


def sieve(limit):
    prime_list = [True for numbers in range(1, limit + 1)]
    prime_list[0] = False
    prime_list[1] = False

    for num in range(2, int(math.sqrt(limit) + 1)):
        double = num * 2
        while double < limit:
            prime_list[double] = False
            double += num

    output_list = []

    for val in range(limit):
        if prime_list[val]:
            output_list.append(val)
    return output_list


def digit_count(num):
    count = 0
    for x in str(num):
        count += 1
    return count


def rotations(num):
    rotation_list = []
    digits = digit_count(num)
    tenth_power = 10 ** (digits - 1)

    for i in range(1, digits):
        first_digit = num // tenth_power
        leftward = (num * 10 + first_digit) - (first_digit * tenth_power * 10)
        rotation_list.append(leftward)
        num = leftward

    return rotation_list


final = 0
final_list = []
primes = sieve(1000000)
for value in primes:
    print(value)
    circ_primes = rotations(value)
    if all(item in primes for item in circ_primes):
        final = final + 1
        final_list.append(value)

print(final)
end = time.time()
print("Time", end - start)