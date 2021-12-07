
def increases(data):
  larger_than_previous = 0
  previous = data[0]
  for point in data[1:]:
    if previous < point:
      larger_than_previous += 1
  
    previous = point

  return larger_than_previous

f = open('day1.txt', 'r')
data = list(map(int, f.readlines()))

part_1 = increases(data)
part_2 = increases([data[i] + data[i+1] + data[i+2] for i in range(0,len(data) - 2)])

print("There are %d measurements that are larger than the previous measurement" % part_1)
print("There are %d measurements that are larger than the previous measurement when using a window size of 3" % part_2)
