file = open("passports.txt", "r")
data = file.read().split('''

''')
file.close()


def filter_escape(string):
    newstring = ""
    for x in list(string):
        if x != "\n":
            newstring += x
        else:
            newstring += " "
    return newstring


# Part 1


def data_check(string):
    counter = 0
    criteria = ["ecl", "iyr", "eyr", "hgt", "hcl", "pid", "byr"]

    listed = string.split(" ")
    if len(listed) < 7:
        return False

    for val in listed:
        identity, stuff = val.split(":")
        if identity in criteria:
            counter += 1

    if counter >= 7:
        return True
    return False


valid = 0

for passports in data:
    if data_check(filter_escape(passports)):
        valid += 1
print(valid)


# Part 2


def byr(string):
    if len(string) != 4:
        return False
    if 1920 <= int(string) <= 2002:
        return True
    return False


def iyr(string):
    if len(string) != 4:
        return False
    if 2010 <= int(string) <= 2020:
        return True
    return False


def eyr(string):
    if len(string) != 4:
        return False
    if 2020 <= int(string) <= 2030:
        return True
    return False


def hgt(string):
    if string[-2:] == "cm":
        if 150 <= int(string[:-2]) <= 193:
            return True
        return False
    if string[-2:] == "in":
        if 59 <= int(string[:-2]) <= 76:
            return True
        return False
    return False


def hcl(string):
    if len(string) != 7:
        return False
    if string[0] == "#":
        for x in string[1:]:
            if (48 <= ord(x) <= 57) or (97 <= ord(x) <= 102):
                continue
            else:
                return False
    else:
        return False
    return True


def ecl(string):
    listed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if string in listed:
        return True
    return False


def pid(string):
    return len(string) == 9


def data_limits(string):
    listed = string.split(" ")
    for x in listed:
        identity, value = x.split(":")
        if identity == "ecl":
            if not ecl(value):
                return False
        elif identity == "pid":
            if not pid(value):
                return False
        elif identity == "hcl":
            if not hcl(value):
                return False
        elif identity == "hgt":
            if not hgt(value):
                return False
        elif identity == "eyr":
            if not eyr(value):
                return False
        elif identity == "iyr":
            if not iyr(value):
                return False
        elif identity == "byr":
            if not byr(value):
                return False
    return True


valid = 0
for val in data:
    val = filter_escape(val)
    if data_check(val):
        if data_limits(val):
            valid += 1
print(valid)
