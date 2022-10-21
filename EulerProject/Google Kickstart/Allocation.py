
def min_houses(listed, budget):
    output = 0
    count = 0
    if listed[0] > budget:
        return 0

    for y in listed:
        output += y
        if output > budget:
            return count
        count += 1
    return count


t = int(input())
for i in range(1, t + 1):
    n, b = [int(s) for s in input().split(" ")]
    A = sorted([int(s) for s in input().split(" ")])
    print(f"Case #{ i }: {min_houses(A, b)}")

