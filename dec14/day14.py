rules = {}
patterns = {}

def sum_dicts(a, b):
  for key, value in b.items():
    if key not in a:
      a[key] = value
    else:
      a[key] += value

def grow(polymer, depth):
  global rules
  global patterns

  pattern = polymer + str(depth)
  if pattern in patterns:
    return patterns[pattern]

  addition = rules[polymer]
  elements = { addition: 1 }

  if depth != 1:
    sum_dicts(elements, grow(polymer[0] + addition, depth - 1))
    sum_dicts(elements, grow(addition + polymer[1], depth - 1))

  patterns[pattern] = elements
  return elements

def grow_generations(polymer, generations):
  elements = {}
  for element in polymer:
    if element not in elements:
      elements[element] = 0
    elements[element] += 1
  
  for i in range(len(polymer) - 1):
    sum_dicts(elements, grow(polymer[i:i+2], generations))
  
  data = sorted(elements.items(), key=lambda x: x[1])

  return data[0][1], data[-1][1]

f = open('day14.txt', 'r')

polymer = f.readline().strip()
f.readline() # empty

for line in f:
  pattern, addition = line.split(' -> ')
  rules[pattern] = addition.strip()

min, max = grow_generations(polymer, 10)
print("Part 1: %d" % (max - min))

min, max = grow_generations(polymer, 40)
print("Part 2: %d" % (max - min))
