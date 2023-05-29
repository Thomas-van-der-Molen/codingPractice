

def volumeOfLakes(islands):
  lakes = []
  lake = []
  for x in range(len(islands)):
    end = x + 1
    while(islands[end] < islands[end - 1]):
      lake.append(islands[end])
      end += 1
    lakes.append(lake)
  print(lakes)



lakes = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
volumeOfLakes(lakes)

