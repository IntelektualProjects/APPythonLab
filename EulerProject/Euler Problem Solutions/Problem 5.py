import time

start = time.time()


def smallest_multiple():
    number = 1

    while True:
        count = 0
        for num in range(2, 21):
            if number % num == 0:
                count = count + 1
            else:
                number = number + 1
                count = 0

        if count == 19:
            end = time.time()
            print("Time", end - start)
            print(number)
            break


smallest_multiple()