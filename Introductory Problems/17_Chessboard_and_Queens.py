board = [input() for _ in range(8)]

ans = 0

def solve(row, colMask, diag1Mask, diag2Mask):
    global ans

    if row == 8:
        ans += 1
        return

    for c in range(8):

        if board[row][c] == '*':
            continue

        d1, d2 = row - c + 7, row + c

        if (colMask >> c) & 1:
            continue

        if (diag1Mask >> d1) & 1:
            continue

        if (diag2Mask >> d2) & 1:
            continue

        solve(
            row + 1,
            colMask | (1 << c),
            diag1Mask | (1 << d1),
            diag2Mask | (1 << d2),
        )

solve(0, 0, 0, 0)
print(ans)