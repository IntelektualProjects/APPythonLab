import time

start = time.time()


def reverse_string(string):
    string_r = ""
    for digit in string:
        string_r = digit + string_r
    return string_r


palindrome_list = []

for num in range(100, 1000):
    for num_two in range(100, 1000):
        palindrome = str(num * num_two)
        number = num * num_two
        reversed_palindrome = reverse_string(palindrome)
        if palindrome == reversed_palindrome:
            palindrome_list.append(number)

end = time.time()
print("Time", end - start)
print(max(palindrome_list))