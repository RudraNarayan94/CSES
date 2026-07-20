n = int(input())
start, end = [] , []

for _ in range(n):
  s, e = list(map(int, input().split()))
  start.append(s)
  end.append(e)

start.sort()
end.sort()

ans = 0
maxi_overlap = 0
i = j = 0

while i < n:
  if start[i] < end[j]:
    maxi_overlap += 1
    ans = max(ans, maxi_overlap)
    i += 1

  else:
    maxi_overlap -= 1
    j += 1

print(ans)