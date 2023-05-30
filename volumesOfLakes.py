  
def volume(lake):
  left = lake.pop(0)
  right = lake.pop()
  comp = min(left,right)
  tot = 0
  for x in lake:
    tot += comp - x
  return tot


def isSubset(compLake, lakes):
  for lake in lakes:
    if all(x in lake for x in compLake):
      return False
  return True
  #print(compLake, lakes)


def islake(lake):
  lake = lake.copy()
  start = lake.pop(0)
  end = lake.pop()
  if all(bar < start for bar in lake) and all(bar < end for bar in lake):
    return True
  return False


def volumeOfLakes(islands):
  lakes = []
  window = 0
  while window < len(islands):
    for x in range(0, len(islands) - window):
      if len(islands[x : x+window]) > 2 and islake(islands[x : x+window]): lakes.append(islands[x : x+window])
    window += 1

  #print(lakes)
  ulakes = []
  for index, value in enumerate(lakes):
    if isSubset(value, lakes[index + 1:]):
      ulakes.append(value)

  print(ulakes)
  vol = 0
  for lake in ulakes:
    vol += volume(lake)
  print(vol)

#my solution, find all possible lakes by brute force sliding window
#check each lake to see if it a valid lake
#remove subsets of lakes, so only true lakes remain
#calculate the volume of each lake by subtracting the bar's value from the lower side

lakes = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
volumeOfLakes(lakes)


#Now do it again, but use dijkstra like google wants

