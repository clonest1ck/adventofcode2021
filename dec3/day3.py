from numpy import transpose

def bitwise_most_common(data, if_equal=0):
  entries = len(data)
  position_sums = map(sum, transpose(data))
    
  output = []

  for position in position_sums:
    most_common = 0
    if 2 * position > entries:
      most_common = 1
    if 2 * position == entries:
      most_common = if_equal
    
    output.append(most_common)

  return output

def invert(data):
  output = []
  for bit in data:
    if bit == 0:
      output.append(1)
    else:
      output.append(0)
  
  return output

def todec(array):
  output = 0
  base = 1
  for bit in reversed(array):
    output += (base * bit)
    base *= 2
 
  return output

def format(array):
  return list(map(int, array.strip()))

f = open('day3.txt', 'r')

data = list(map(format, f))
gamma_binary = bitwise_most_common(data)
epsilon_binary = invert(gamma_binary)

gamma = todec(gamma_binary)
epsilon = todec(epsilon_binary)

print("Part 1: %d" % (gamma * epsilon))

oxygen = data
position = 0
while len(oxygen) > 1:
  most_common = bitwise_most_common(oxygen, 1)
  oxygen = [x for x in oxygen if x[position] == most_common[position]]
  position += 1

co2 = data
position = 0
while len(co2) > 1:
  most_common = bitwise_most_common(co2, 1)
  co2 = [x for x in co2 if x[position] != most_common[position]]
  position += 1

print("Part 2: %d" % (todec(oxygen[0]) * todec(co2[0])))

