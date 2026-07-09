n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
ans = float("inf")

def solve(i, curr):
    global ans

    if i == n:
        ans = min(ans, abs(total - 2 * curr))
        return

    # Put nums[i] in subset 1
    solve(i + 1, curr + nums[i])

    # Put nums[i] in subset 2
    solve(i + 1, curr)

solve(0, 0)
print(ans)