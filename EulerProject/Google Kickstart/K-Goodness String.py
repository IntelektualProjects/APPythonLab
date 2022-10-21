def goodness_identifier(length, string, goodness):
    count = 0
    p = 10**5
    val = int((length / 2) * p + 0.5) / p
    for x in range(1, round(length / 2) + 1):
        if string[x - 1] != string[length - x]:
            count += 1
    return goodness - count


t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    S = input()
    print(f"Case #{ i }: {goodness_identifier(n, S, k)}")