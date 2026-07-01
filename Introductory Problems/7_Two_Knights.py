n = int(input())


for k in range(1, n + 1):
  total_combinations = ((k**2) * (k**2 - 1)) // 2
  invalid_combinations = 4 * (k - 2) * (k - 1)
  print(total_combinations - invalid_combinations)