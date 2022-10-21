import time


def fibonacci_digit():
    start = time.time()

    first_num = 1
    second_num = 1
    third_num = 0
    num_list = [0, 0]

    while True:
        third_num = first_num + second_num
        if len(str(third_num)) == 1000:
            num_list.append(1)
            break
        else:
            num_list.append(0)
        first_num = second_num
        second_num = third_num

    end = time.time()
    print("Time", end - start)
    return num_list.index(1) + 1


print(fibonacci_digit())