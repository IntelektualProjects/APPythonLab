def sum_of_squares(output):
    for x in range(101):
        x = x ** 2
        output += x
    return output


def square_of_sum (output_2):
    for y in range(101):
        output_2 += y

    output_2 **= 2
    return output_2


sumofsquares = sum_of_squares(0)
squareofsum = square_of_sum(0)

print(squareofsum - sumofsquares)