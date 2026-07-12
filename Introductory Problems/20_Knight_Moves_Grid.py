from collections import deque

n = int(input())

grid = [[float("inf")] * n for _ in range(n)]

q = deque([(0, 0, 0)])
grid[0][0] = 0

directions = [(-2, 1), (-1, 2), (1, 2), (2, 1),
              (2, -1), (1, -2), (-1, -2), (-2, -1)]

while q:
  length = len(q)

  for _ in range(length):
    step, r, c = q.popleft()

    for dx, dy in directions:
      nr, nc = r + dx, c + dy

      if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > step + 1:
        grid[nr][nc] = step + 1
        q.append((step + 1, nr, nc))

for i in range(n):
  print(*grid[i])
  # print()
