n = int(input())
nums = list(map(int, input().split()))

xor =  0

for i in range(1, n + 1):
  xor ^= i

for num in nums:
  xor ^= num

print(xor)