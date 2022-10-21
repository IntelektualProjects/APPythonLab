t = int(input())
for i in range(1, t + 1):
    n, b = [int(s) for s in input().split(" ")]
    A = sorted([int(s) for s in input().split(" ")])
    print(f"Case #{ i }: {n, b, A}")
