total_cubes = int(input())
MAX_CUBES = 10**4
# 1st level = 1
# 2nd level = 1 + 2 = 3
# 3rd level = 1 + 2 + 3 = 6
# 4th level = 1 + 2 + 3 + 4 = 10
# total cubes = 1 + 3 + 6 + 10 = 20
# 1, 4, 10, 20, 35, 56, 84, 120, 165, 220
#   3, 6, 10, 15, 21, 28, 36, 45, 55
#     3 , 4, 5, 6, 7, 8, 9, 10
#       1, 1, 1, 1, 1, 1, 1, 1

for i in range(1, MAX_CUBES + 1):
    total = i * (i + 1) * (i + 2) // 6
    if total > total_cubes:
        print(i-1)
        break
    if total == total_cubes:
        print(i)
        break