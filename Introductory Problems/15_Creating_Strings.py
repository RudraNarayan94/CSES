s = input()

ans = []
n = len(s)
visited = [False] * n

def solve(temp: str):
    if len(temp) == n:
        ans.append(temp)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solve(temp + s[i])
            visited[i] = False

solve("")
ans = sorted(set(ans))
print(len(ans))
print(*(ans), sep="\n")