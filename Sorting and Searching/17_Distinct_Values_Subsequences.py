MOD = 10**9 + 7

n = int(input())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

ans = 1
for f in freq.values():
    ans = (ans * (f + 1)) % MOD

print((ans - 1) % MOD)