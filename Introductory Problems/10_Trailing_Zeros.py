n = int(input())

ans = 0
multiple = 5

while multiple <= n:
  ans += n // multiple  
  multiple *= 5


print(ans)