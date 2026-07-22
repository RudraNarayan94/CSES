n = int(input())
nums = list(map(int, input().split()))

ans = max(nums)
Sum = 0

for num in nums:
  Sum += num
  ans = max(ans, Sum)
  if Sum < 0:
    Sum = 0

print(ans)