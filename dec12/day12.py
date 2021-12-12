
f = open('day12.txt', 'r')

small_caves = {}
large_caves = {}

def add_path(start, end):
  global small_caves
  global large_caves

  cave_group = large_caves

  if start.lower() == start:
    cave_group = small_caves

  if start not in cave_group:
    cave_group[start] = []

  cave_group[start].append(end)

def trace(current, visited, allow_visit_of_small_twice=False):
  global small_caves
  global large_caves

  if current == 'end':
    return [current]

  pathlist = large_caves

  if current in small_caves:
    visited.append(current)
    pathlist = small_caves

  paths = set()
  for path in pathlist[current]:
    if path not in visited:
      new_paths = trace(path, visited, allow_visit_of_small_twice)
      paths = paths | set(map(lambda a: current + a, new_paths))

  if current in visited:
    visited.remove(current)

    if allow_visit_of_small_twice and current != 'start':
      for path in pathlist[current]:
        if path not in visited:
          new_paths = trace(path, visited, False)
          paths = paths | set(map(lambda a: current + a, new_paths))

  return paths

for path in f:
  a,b = path.strip().split('-')

  add_path(a, b)
  add_path(b, a)

paths = trace('start', [])
paths_2 = trace('start', [], True)

print("Part 1: There are %d paths" % len(paths))
print("Part 2: There are %d paths" % len(paths_2))
