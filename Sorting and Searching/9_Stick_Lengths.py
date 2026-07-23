n = int(input())
nums = list(map(int, input().split()))



nums.sort()
median = nums[n // 2]

ans = sum(abs(num - median) for num in nums)
print(ans)
