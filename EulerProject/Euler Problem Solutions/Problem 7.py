import time

start = time.time()


def finding_primes():
    number = 2
    prime_list = []

    while True:
        if number > 1:
            for divisor in range(2, number):
                if number % divisor == 0:
                    number = number + 1
                    break
            else:
                prime_list.append(number)
                number = number + 1

        if len(prime_list) == 10001:
            end = time.time()
            print("Time", end - start)
            print(prime_list.pop())
            break


finding_primes()