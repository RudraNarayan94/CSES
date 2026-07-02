n = int(input())
total = n * (n + 1) // 2

if total % 2 != 0:
    print("NO")
else:
    print("YES")
    s1, s2 = [], []
    target = total // 2

    for i in range(n, 0, -1):
        if target >= i:
            s1.append(i)
            target -= i
        else:
            s2.append(i)

    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
