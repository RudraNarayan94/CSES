n, x = map(int, input().split())
children = list(map(int, input().split()))

children.sort()

i, j = 0, n - 1
gondolas = 0

while i <= j:
  if i == j:
      gondolas += 1
      break

  if children[i] + children[j] <= x:
      i += 1
      j -= 1
  else:
      j -= 1

  gondolas += 1

print(gondolas)