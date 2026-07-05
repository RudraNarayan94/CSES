n = int(input())

for i in range(2**n):
    gray = i ^ (i >> 1) 
    # print(gray)         
    ans = format(gray, f'0{n}b') # binary string with leading zeros
    print(ans)
