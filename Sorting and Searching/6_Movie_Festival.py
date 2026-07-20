n = int(input())
movies = []

for _ in range(n):
    s, e = map(int, input().split())
    movies.append((s, e))

# sort by end time
movies.sort(key=lambda x: x[1])

ans = 0
prev_end_time = 0

for s, e in movies:
    if s >= prev_end_time:
        ans += 1
        prev_end_time = e

print(ans)
