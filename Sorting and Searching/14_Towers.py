from bisect import bisect_right

n = int(input())
cubes = list(map(int, input().split()))

towers = []

for cube in cubes:
    # the first tower whose top > cube
    idx = bisect_right(towers, cube)
    if idx < len(towers):
        towers[idx] = cube 
    else:
        towers.append(cube)  # a new tower

print(len(towers))
