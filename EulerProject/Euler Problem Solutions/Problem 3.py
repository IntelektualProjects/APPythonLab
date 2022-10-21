import time


def prime_factors(limit):
    start = time.time()
    list_one = 0

    for num in range(2, limit + 1):
        for number in range(2, num):
            if num % number == 0:
                break
        else:
            if limit % num == 0:
                list_one = num
                print(list_one)
    print("factors found. Step 2")

    end = time.time()
    print("Time", end-start)
    return list_one


print(prime_factors(600851475143))
