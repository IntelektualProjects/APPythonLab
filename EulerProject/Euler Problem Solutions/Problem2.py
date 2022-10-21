def fibonacci_sequence():
    first_num = 1
    second_num = 1
    output = 0
    third_num = 0

    while third_num <= 4000000:
        third_num = first_num + second_num
        if third_num % 2 == 0:
            output = output + third_num
        first_num = second_num
        second_num = third_num

    return output


print(fibonacci_sequence())
