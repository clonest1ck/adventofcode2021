from functools import reduce

segments = { 0: [ 'a', 'b', 'c', 'e', 'f', 'g' ]
           , 1: [ 'c', 'f' ]
           , 2: [ 'a', 'c', 'd', 'e', 'g' ]
           , 3: [ 'a', 'c', 'd', 'f', 'g' ]
           , 4: [ 'b', 'c', 'd', 'f' ]
           , 5: [ 'a', 'b', 'd', 'f', 'g' ]
           , 6: [ 'a', 'b', 'd', 'e', 'f', 'g' ]
           , 7: [ 'a', 'c', 'f' ]
           , 8: [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
           , 9: [ 'a', 'b', 'c', 'd', 'f', 'g' ]
           }

def count_digits_of_unique_length_in_output(line):
  has_unique_length = 0
  test_output, display = line.split(' | ')
  for digit in display.split():
    length = len(digit)
    
    if length == len(segments[1]) \
       or length == len(segments[4]) \
       or length == len(segments[7]) \
       or length == len(segments[8]):
      has_unique_length += 1

  return has_unique_length

def decode(line):
  test_output, message = line.split(' | ')

  segment_mapping = {}
  by_length = {}
  for display in test_output.split():
    segment_length = len(display)
    if segment_length not in by_length:
      by_length[segment_length] = []
    by_length[segment_length].append(set([char for char in display]))

  one = by_length[2][0]
  four = by_length[4][0]
  seven = by_length[3][0]
  eight = by_length[7][0]

  # the a segment appears in 7 but not 1
  segment_mapping[seven.difference(one).pop()] = 'a'

  # decode 0, 6 and 9
  for digit in by_length[6]:
    if digit.union(four) == eight:
      # 0 or 6
      if digit.union(one) == digit:
        # 0
        segment_mapping[eight.difference(digit).pop()] = 'd'
      else:
        # 6
        c_segment = eight.difference(digit).pop()
        segment_mapping[c_segment] = 'c'
        segment_mapping[one.difference(set(c_segment)).pop()] = 'f'
    else:
      # 9
      segment_mapping[eight.difference(digit).pop()] = 'e'

  # a, d and g are all in digits with 5 segments and we already know a and d
  g_segment = reduce(lambda a,b: a.intersection(b), by_length[5]) \
              .difference(set([x for x,y in segment_mapping.items() if y == 'a' or y == 'd'])).pop()
  
  segment_mapping[g_segment] = 'g'
  
  # only b left now
  b_segment = eight.difference(segment_mapping.keys()).pop()
  segment_mapping[b_segment] = 'b'

  result = ""
  for digit in message.split():
    on_segments = []
    for segment in digit:
      on_segments.append(segment_mapping[segment])

    on_segments.sort()
    
    for digit, turned_on in segments.items():
      if turned_on == on_segments:
        result += (str(digit))
        break

  return int(result)

digits_of_unique_length = 0
sum_of_displays = 0

f = open('day8.txt', 'r')
for line in f:
  digits_of_unique_length += count_digits_of_unique_length_in_output(line)
  sum_of_displays += decode(line)

print("Part 1: %d" % digits_of_unique_length)
print("Part 2: %d" % sum_of_displays)
