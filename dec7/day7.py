
def calculate_fuel_usage_for_mean(positions, mean, use_range):
  fuel_used = 0
  for i, position in enumerate(positions):
    steps = abs(position - mean)
    if use_range:
      fuel_used += sum(range(steps+1))
    else:
      fuel_used += steps 
  
  return fuel_used

def minimize(positions, use_range_sum=False):
  mean = round(sum(positions) / len(positions))
  
  fuel_used = {}
  
  for m in range(mean - 1, mean + 2):
    fuel_used[m] = calculate_fuel_usage_for_mean(positions, m, use_range_sum)
  
  current = mean
  while fuel_used[current] > fuel_used[current + 1]:
    current += 1
    fuel_used[current + 1] = calculate_fuel_usage_for_mean(positions, current + 1, use_range_sum)
  
  while fuel_used[current] > fuel_used[current - 1]:
    current -= 1
    fuel_used[current - 1] = calculate_fuel_usage_for_mean(positions, current - 1, use_range_sum)
  
  return fuel_used[current]

f = open('day7.txt', 'r')

positions = list(map(int, f.readline().split(',')))
part1 = minimize(positions)
part2 = minimize(positions, True)

print("Part 1: %d fuel was used" % part1)
print("Part 2: %d fuel was used" % part2)

