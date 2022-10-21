def peaks(heights):
    count = 0
    for x in range(1, len(heights) - 1):
        if heights[x] > heights[x - 1] and heights[x] > heights[x + 1]:
            count += 1
    return count


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    H = [int(s) for s in input().split(" ")]
    print(f"Case #{ i }: {peaks(H)}")