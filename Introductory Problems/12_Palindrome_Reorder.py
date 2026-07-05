s = input().strip()
n = len(s)

counter = [0] * 26
for ch in s:
    counter[ord(ch) - ord('A')] += 1

odd_count = sum(freq % 2 for freq in counter)
if odd_count > 1:
    print("NO SOLUTION")
    exit()

half = []
middle = ""
for i in range(26):
    freq = counter[i]

    if freq == 0: continue

    ch = chr(ord('A') + i)

    if freq % 2 == 1:
        middle = ch * freq
    else:
        half.append(ch * (freq // 2))

left = "".join(half)
right = left[::-1]

if middle:
    ans = left + middle + right
else:
    ans = left + right

print(ans)
