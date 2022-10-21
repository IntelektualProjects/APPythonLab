import time
start = time.time()


def reverse_string(string):
    string_r = ""
    for digit in string:
        string_r = digit + string_r
    return string_r


def binary_value(number_string):
    binary = bin(number_string).replace("0b", "")
    return binary


palindrome_list = []
for num in range(1, 1000000 + 1):
    palindrome = str(num)
    reversed_palindrome = reverse_string(palindrome)
    if palindrome == reversed_palindrome:
        palindrome_list.append(num)

final_list = []

for number in palindrome_list:
    bin_palindrome = binary_value(number)
    bin_reverse = reverse_string(bin_palindrome)
    if bin_palindrome == bin_reverse:
        final_list.append(number)

end = time.time()
print("Time", end - start)
print(sum(final_list))