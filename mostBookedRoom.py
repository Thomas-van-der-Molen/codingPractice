def mostBookedRoom(inputList):
  inputSet = set(inputList)
  inputSet = [item for item in inputSet if '-' not in item]
  inputSet.sort(reverse=True)#for case 2, where two rooms are booked equally frequently
  outputDict = {}
  for item in inputSet:
    outputDict[inputList.count(item)] = item
  maximum = outputDict[max(outputDict)]#max will return the last largest element if two are the same, so the set needs to be sorted in reverse
  return ''.join(list(maximum)[1:])


print(mostBookedRoom(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))
print(mostBookedRoom(["+3E", "-3E", "+3E", "+4F", "+1A", "-3E"]))
print(mostBookedRoom(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+3E", "-3E", "-4F", "+4F", "-4F", "+4F"]))
print(mostBookedRoom(["+1A", "+-1A", "+4F", "-4F"]))
print(mostBookedRoom(["+4F", "+-4F", "+1A", "-1A"]))