t = int(input())
arr = []
while t:
  t -= 1
  x, y = list(map(int, input().split())) #row, col
  ans = 0
  if x <= y:
    if y & 1:
      ans = pow(y, 2) - (x - 1)
    else:
      ans = pow(y - 1, 2) + 1 + (x - 1)
  else:
    if x & 1:
      ans = pow(x - 1, 2) + 1 + (y - 1)
    else:
      ans = pow(x, 2) - (y - 1)

  arr.append(ans)

for num in arr:
  print(num)


