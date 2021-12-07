
def move(data):
  horizontal = 0
  depth = 0

  aim = 0
  depth_aim = 0

  for line in data:
    command, stepsize = line.split(' ')
    if command == "forward":
        horizontal += int(stepsize)
        depth_aim += (aim * int(stepsize))
    elif command == "down":
        depth += int(stepsize)
        aim += int(stepsize)
    elif command == "up":
        depth -= int(stepsize)
        aim -= int(stepsize)
    else:
        print("Error: command not found '%s'" % command)
  
  return (horizontal * depth), (horizontal * depth_aim)


f = open('day2.txt', 'r')
part1, part2 = move(f.readlines())
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)
