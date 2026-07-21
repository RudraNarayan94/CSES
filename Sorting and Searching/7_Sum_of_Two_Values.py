n, x = map(int, input().split())
nums = list(map(int, input().split()))
nums = [(nums[i], i) for i in range(n)]

nums.sort()
i, j = 0, n - 1

ans = ()
while i < j:
  if nums[i][0] + nums[j][0] == x:
    ans = (nums[i][1], nums[j][1])
    break
  elif nums[i][0] + nums[j][0] < x:
    i += 1
  else:
    j -= 1

if ans:
  print(ans[0] + 1, ans[1] + 1)
else:
  print("IMPOSSIBLE")