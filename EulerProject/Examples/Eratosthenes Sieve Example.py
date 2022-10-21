import math


def eratosthenes_sieve(limit):
    # create a list of boolean values all true
    prime_list = [True for numbers in range(1, limit + 1)]
    # mark 0 and 1 as false because they are not prime
    prime_list[0] = False
    prime_list[1] = False

    # sieve algorithm that finds and deletes multiples of primes
    for num in range(2, int(math.sqrt(limit) + 1)):
        double = num * 2
        while double < limit:
            prime_list[double] = False
            double += num

    # list for prime values
    output_list = []

    # adds prime values in the limit range to the output list
    for value in range(limit):
        if prime_list[value]:
            output_list.append(value)
    return output_list


print(sum(eratosthenes_sieve(2000000)))