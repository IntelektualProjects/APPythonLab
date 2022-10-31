 # This program creates Punnett Squares from given parent alleles inputted by User. Also allows you to choose from 5 different types of genetic crosses.
def regular_cross():
    a_one, a_two = list(input("First Parent's Genotype: "))
    b_one, b_two = list(input("Second Parent's Genotype: "))

    if ord(a_one) < ord(b_one):
        one = a_one + b_one
    else:
        one = b_one + a_one

    if ord(a_one) < ord(b_two):
        two = a_one + b_two
    else:
        two = b_two + a_one

    if ord(a_two) < ord(b_one):
        three = a_two + b_one
    else:
        three = b_one + a_two

    if ord(a_two) < ord(b_two):
        four = a_two + b_two
    else:
        four = b_two + a_two
    print(f"The possible genotypes are {one}, {two}, {three}, and {four}")
    gene_list = [one, two, three, four]
    for x in set(gene_list):
        percentage = (gene_list.count(x) / 4) * 100
        print(f"{x} : {percentage}%")


def dihybrid_cross():
    final = []
    p_one_pairs = []
    p_two_pairs = []
    p_one = list(input("First Genotype: "))
    p_two = list(input("Second Genotype: "))
    p_one_first, p_one_second = p_one[0:2], p_one[2:4]
    p_two_first, p_two_second = p_two[0:2], p_two[2:4]

    for x in p_one_first:
        for y in p_one_second:
            p_one_pairs.append(x + y)
    for x in p_two_first:
        for y in p_two_second:
            p_two_pairs.append(x + y)
    for f in p_one_pairs:
        for s in p_two_pairs:
            f_one, f_two = list(f)
            s_one, s_two = list(s)

            if ord(f_one) < ord(s_one):
                part_one = f_one + s_one
            else:
                part_one = s_one + f_one
            if ord(f_two) < ord(s_two):
                part_two = f_two + s_two
            else:
                part_two = s_two + f_two
            final.append(part_one + part_two)
    print(f" Possible Outcomes: {final}")
    for val in set(final):
        percentage = (final.count(val) / 16) * 100
        print(f"{val} : {percentage}%")


def hemophiliac_cross():
    final = []
    choices = []
    a_one, a_two = list(input("Mother's Genotype (Ex. XhXh = hh): "))
    b_one = input("Father's Genotype (Ex. XHY = H): ")
    b_two = 'Y'

    if ord(a_one) < ord(b_one):
        final.append(a_one + b_one)
    else:
        final.append(b_one + a_one)

    if ord(a_one) < ord(b_two):
        final.append(a_one + b_two)
    else:
        final.append(b_two + a_one)

    if ord(a_two) < ord(b_one):
        fianl.append(a_two + b_one)
    else:
        final.append(b_one + a_two)

    if ord(a_two) < ord(b_two):
        final.append(a_two + b_two)
    else:
        final.append(b_two + a_two)

    for value in final:
        c = []
        if value == 'Yh' or value == 'YH':
            choice_list = list(reversed(value))
        else:
            choice_list = list(value)
        for x in choice_list:
            if x != 'Y':
                c.append('X' + x)
            else:
                c.append(x)
        choices.append(''.join(c))
    print(f"Possible genotypes are {choices[0]}, {choices[1]}, {choices[2]}, {choices[3]}")

    for y in set(choices):
        percent = (choices.count(y) / 4) * 100
        print(f"{y} : {percent}%")


def codominant_cross():
    a_one, a_two = list(input("First Parent's Genotype: "))
    b_one, b_two = list(input("Second Parent's Genotype: "))
    if ord(a_one) < ord(b_one):
        one = a_one + b_one
    else:
        one = b_one + a_one

    if ord(a_one) < ord(b_two):
        two = a_one + b_two
    else:
        two = b_two + a_one

    if ord(a_two) < ord(b_one):
        three = a_two + b_one
    else:
        three = b_one + a_two

    if ord(a_two) < ord(b_two):
        four = a_two + b_two
    else:
        four = b_two + a_two
    print(f"The possible genotypes are {one}, {two}, {three}, and {four}")
    gene_list = [one, two, three, four]
    for x in set(gene_list):
        percentage = (gene_list.count(x) / 4) * 100
        print(f"{x} : {percentage}%")


def incomplete_dominance_cross():
    a_one, a_two = list(input("First Parent's Genotype: "))
    b_one, b_two = list(input("Second Parent's Genotype: "))

    if ord(a_one) < ord(b_one):
        one = a_one + b_one
    else:
        one = b_one + a_one

    if ord(a_one) < ord(b_two):
        two = a_one + b_two
    else:
        two = b_two + a_one

    if ord(a_two) < ord(b_one):
        three = a_two + b_one
    else:
        three = b_one + a_two

    if ord(a_two) < ord(b_two):
        four = a_two + b_two
    else:
        four = b_two + a_two
    print(f"The possible genotypes are {one}, {two}, {three}, and {four}")
    gene_list = [one, two, three, four]
    for x in set(gene_list):
        percentage = (gene_list.count(x) / 4) * 100
        print(f"{x} : {percentage}%")


while True:
    r = '\033[0m'
    g = '\033[92m'
    print(f"Hello, Welcome to {g}GeneCross{r}")
    choice = int(input('''Please select a cross type
        1 = Regular punnett square
        2 = Regular Dihybrid Cross
        3 = Hemophiliac Cross
        4 = Codominant regular punnett square
        5 = Incomplete dominance punnett square
        : '''))

    while True:
        if choice == 1:
            regular_cross()
            break
        elif choice == 2:
            dihybrid_cross()
            break
        elif choice == 3:
            hemophiliac_cross()
            break
        elif choice == 4:
            codominant_cross()
            break
        elif choice == 5:
            incomplete_dominance_cross()
            break
        else:
            print("Invalid choice. Please try again: ")
            choice = int(input())

    while True:
        restart = input("Run Again? (y/n): ")
        if restart in ('y', 'n'):
            break
        print("Invalid Input")
    if restart.lower() == 'y':
        continue
    else:
        break
