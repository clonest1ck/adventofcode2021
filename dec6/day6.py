from functools import reduce

def step(fishes):
  next_step = {timer: 0 for timer in range(0,9)}

  for timer, fish in fishes.items():
    if timer == 0:
      next_step[6] += fish
      next_step[8] += fish
    else:
      next_step[timer - 1] += fish

  return next_step

def count(fishes):
  return reduce(lambda c1, c2: c1 + c2, fishes.values())

f = open('day6.txt', 'r')

fishes = {}
initial_state = map(int, f.readline().split(','))

for fish in initial_state:
  if not fish in fishes:
    fishes[fish] = 0
  
  fishes[fish] += 1

for generation in range(80):
  fishes = step(fishes)

amount = count(fishes)
print("Part 1: there are %d fishes after 80 days" % amount)

for generation in range(256 - 80):
  fishes = step(fishes)

amount = count(fishes)
print("Part 2: there are %d fishes after 256 days" % amount)
