def self_powers(total, amount):
    for x in range(0, amount + 1):
        x = x ** x
        total += x
    listed = list(str(total))
    return listed[-10:]


print(self_powers(-1, 1000))