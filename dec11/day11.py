def step(octopuses):
  increment(octopuses)

  flashes = 0
  df = -1
  while df != 0:
    df = check_flashes(octopuses)
    flashes += df
  
  return flashes

def increment(octopuses):
  for y, row in enumerate(octopuses):
    for x, energy in enumerate(row):
      octopuses[y][x] += 1

def check_flashes(octopuses):
  flashes = 0
  for y, row in enumerate(octopuses):
    for x, energy in enumerate(row):
      if energy > 9:
        octopuses[y][x] = 0
        flashes += 1
        for dy in range(max(0, y-1), min(len(octopuses), y+2)):
          for dx in range(max(0, x-1), min(len(row), x+2)):
            if octopuses[dy][dx] != 0:
              octopuses[dy][dx] += 1

  return flashes

f = open('day11.txt', 'r')

octopuses = []

for line in f:
  row = []
  for energy in line.strip():
    row.append(int(energy))
  octopuses.append(row)


total_flashes = 0
flashes_in_generation = 0
generation = 0

while flashes_in_generation != 100 or generation < 100:
  flashes_in_generation = step(octopuses)
  
  if generation < 100:
    total_flashes += flashes_in_generation
  
  generation += 1

print("Part 1: %d" % total_flashes)
print("Part 2: %d" % generation)

