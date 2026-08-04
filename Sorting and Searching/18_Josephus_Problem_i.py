from collections import deque

def solve(N):
    q = deque(range(1, N+1))
    flag = False

    while q:
        ele = q.popleft()
        if flag:
            print(ele)
        else:
            q.append(ele)
        flag = not flag

n = int(input())
solve(n)

