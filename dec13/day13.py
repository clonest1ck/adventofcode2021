from functools import reduce

def fold(paper, axis, index):
  removed_dots = set()
  added_dots = set()

  for dot in paper:
    dot_index = dot[0] # default to x
    if axis == 'y':
      dot_index = dot[1]

    if dot_index >= index:
      removed_dots.add(dot)

    new_dot = None
    if dot_index > index:
      new_dot_index = (2  * index) - dot_index
      if axis == 'y':
        new_dot = (dot[0], new_dot_index)
      else:
        new_dot = (new_dot_index, dot[1])

      added_dots.add(new_dot)

  return (paper - removed_dots) | added_dots

f = open('day13.txt', 'r')

paper = set()
folds = []
reading_folds = False

for line in f:
  if line == "\n":
    reading_folds = True
    continue

  if reading_folds:
   axis,index = line.strip().split()[2].split('=')
   folds.append((axis, int(index)))
  else:
    x,y = map(int, line.strip().split(','))
    paper.add((x,y))

first = True

for axis, index in folds:
  paper = fold(paper, axis, index)
  if first:
    first = False
    print("Part 1: %d dots are visible after the first fold" % len(paper))


max_x, max_y = reduce(lambda a, b: (max(a[0], b[0]), max(a[1], b[1])), list(paper))

print("\nLicense:")
for y in range(max_y + 1):
  for x in range(max_x + 1):
    if (x,y) in paper:
      print("#", end="")
    else:
      print(" ", end="")

  print("")

