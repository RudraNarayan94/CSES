n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

set1 = ['A', 'B']
set2 = ['C', 'D']

ans = [[''] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) & 1:
            ans[i][j] = set1[0] if grid[i][j] == set1[1] else set1[1]
        else:
            ans[i][j] = set2[0] if grid[i][j] == set2[1] else set2[1]

for row in ans:
    print("".join(row))
