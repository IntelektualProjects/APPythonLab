numbers = [5,6,7,5,3,4,6,7,]
set_two = []

numbers.sort()
for number in numbers:
    if number not in set_two:
        set_two.append(number)
print(set_two)