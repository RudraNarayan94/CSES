s = input().strip()
n = len(s)

counter = [0] * 26

maxFreq = 0
for ch in s:
    ind = ord(ch) - ord('A')
    counter[ind] += 1
    maxFreq = max(maxFreq, counter[ind])

if maxFreq > (n + 1) // 2:
    print(-1)
    exit()

ans = []
prev = -1

for i in range(n):
  remaining = n - i - 1
  for k in range(26):
      if counter[k] == 0 or k == prev:
          continue
      
      counter[k] -= 1
      mx = max(counter)

      if mx <= (remaining + 1) // 2:
          ans.append(chr(ord('A') + k))
          prev = k
          break
      counter[k] += 1

print("".join(ans))