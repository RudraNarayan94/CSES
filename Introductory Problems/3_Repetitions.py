s = input()

ans = count = 1
prev = s[0]

for i in range(1, len(s)):
  if s[i - 1] == s[i]:
    count += 1
  else:
    count = 1
    prev = s[i]
  
  ans = max(ans, count)

print(ans)


