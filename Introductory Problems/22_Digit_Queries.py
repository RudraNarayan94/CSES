q = int(input())

def digit_query(k):
  length = 1
  count = 9
  while k > length * count:
      k -= length * count
      length += 1
      count *= 10
  
  index = (k - 1) // length
  digit_index = (k - 1) % length
  number = 10**(length - 1) + index
  # print("k - 1 -> ", k - 1, " index -> ",index, " digit_ind ->", digit_index)
  return str(number)[digit_index]

while q:
   q -= 1
   k = int(input())
   ans = digit_query(k)
   print(ans)