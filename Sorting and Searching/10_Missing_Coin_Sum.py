n = int(input())
nums = list(map(int, input().split()))

nums.sort()
res = 1  # smallest sum we cannot form yet

for num in nums:
    if num > res:
        break
    res += num

print(res)
