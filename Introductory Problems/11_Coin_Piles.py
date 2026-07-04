t = int(input())



ans = []
while t:
  t -= 1
  a, b = list(map(int, input().split()))

  if (a + b) % 3 == 0 and max(a, b) <= 2 * min(a, b):
    ans.append("YES")
  else:
    ans.append("NO")

for res in ans:
  print(res)