n = int(input())
nums = list(map(int, input().split()))
pairs = [(num, idx) for idx, num in enumerate(nums)]
pairs.sort()

ans = 1
for i in range(n - 1):
  if pairs[i][1] > pairs[i + 1][1]:
    ans += 1

print(ans)