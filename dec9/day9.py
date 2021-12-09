from functools import reduce

def find_low_points(cave):
  low_points = []

  max_row = len(cave) - 1
  max_column = len(cave[0]) - 1

  for y, row in enumerate(cave):
    for x, point in enumerate(row):
      if  (x == 0 or point < cave[y][x-1]) \
      and (x == max_column or point < cave[y][x+1]) \
      and (y == 0 or point < cave[y-1][x]) \
      and (y == max_row or point < cave[y+1][x]):
        low_points.append(((x,y), point))
    
  return low_points

def find_basins(cave, low_points):
  basins = []
  for point, value in low_points:
    basins.append(trace(cave, point))

  return basins

visited = {}
def trace(cave, point):
  global visited
  if point in visited:
    return []
  visited[point] = True
  x = point[0]
  y = point[1]
  if cave[y][x] == 9:
    return []

  left = (max(0,x-1), y)
  right = (min(len(cave[0])-1, x+1),  y)
  up = (x, max(0, y-1))
  down = (x, min(len(cave)-1, y+1))  

  return [point] + trace(cave, left) + trace(cave, right) + trace(cave, up) + trace(cave, down)

f = open('day9.txt', 'r')

cave_map = []

for line in f:
  cave_map.append([int(x) for x in line.strip()])

low_points = find_low_points(cave_map)
solution_1 = sum(map(lambda x: x[1]+1, low_points))

basins = find_basins(cave_map, low_points)
solution_2 = reduce(lambda x,y: x*y, list(reversed(sorted(map(len, basins))))[0:3])

print("Part 1: %d" % solution_1)
print("Part 2: %d" % solution_2)

