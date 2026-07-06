n = int(input())

res = []

def solve(n: int, a: int, b : int, c : int) -> None:
  if n > 0:
    solve(n - 1, a, c, b) #source, using, destination
    res.append((a, c))
    solve(n - 1, b, a, c) #source, using, destination

solve(n, 1, 2, 3)

print(len(res))

for a, c in res:
  print(a, " ", c)