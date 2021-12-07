class Line(object):
  def __init__(self, line_str):
    start, end = line_str.split(' -> ')
    start_x, start_y = map(int, start.split(','))
    end_x, end_y = map(int, end.split(','))

    self.start = (start_x, start_y)
    self.end = (end_x, end_y)

  def is_vertical(self):
    return self.start[0] == self.end[0]

  def is_horizontal(self):
    return self.start[1] == self.end[1]

  def get_points(self):
    if self.is_vertical():
      start_y = min(self.start[1], self.end[1])
      end_y = max(self.start[1], self.end[1])
      return [(self.start[0], y) for y in range(start_y, end_y + 1)]
    elif self.is_horizontal():
      start_x = min(self.start[0], self.end[0])
      end_x = max(self.start[0], self.end[0])
      return [(x, self.start[1]) for x in range(start_x, end_x + 1)]
    else:
      delta_x = 1 if self.end[0] > self.start[0] else -1
      delta_y = 1 if self.end[1] > self.start[1] else -1
      return zip(range(self.start[0], self.end[0] + delta_x, delta_x), range(self.start[1], self.end[1] + delta_y, delta_y))

f = open('day5.txt', 'r')

lines = []

for line in f:
  lines.append(Line(line))

grid = {}
for line in lines:
  if line.is_vertical() or line.is_horizontal():
    for point in line.get_points():
      if point not in grid:
        grid[point] = 0
      grid[point] += 1

overlaps = sum([1 if x > 1 else 0 for x in grid.values()])

print("Part 1: there are %d points with at least 2 overlapping vertical or horizontal lines" % overlaps)

grid = {}
for line in lines:
  for point in line.get_points():
    if point not in grid:
      grid[point] = 0
    grid[point] += 1

overlaps = sum([1 if x > 1 else 0 for x in grid.values()])
print("Part 2: there are %d points with at least 2 overlapping lines" % overlaps)
