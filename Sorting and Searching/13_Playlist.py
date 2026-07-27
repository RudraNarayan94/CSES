n = int(input())
nums = list(map(int, input().split()))

seen = set()
ans = j = 0

for i in range(n):
    while nums[i] in seen:
        seen.remove(nums[j])
        j += 1
    seen.add(nums[i])
    ans = max(ans, i - j + 1)

print(ans)
