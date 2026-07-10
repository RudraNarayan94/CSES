t = int(input())

while t:
    t -= 1
    n, a, b = map(int, input().split())

    if a + b > n or abs(a - b) > 1:
        print("NO")
        continue

    print("YES")

    tie = n - a - b

    A = list(range(1, tie + 1))
    B = list(range(1, tie + 1))

    rem = list(range(tie + 1, n + 1))

    # Rotate by a
    A += rem
    B += rem[a:] + rem[:a]

    print(*A)
    print(*B)