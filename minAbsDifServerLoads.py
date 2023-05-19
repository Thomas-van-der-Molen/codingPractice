
def minAbsDif(input):
  list1 = list()
  list2 = list()
  for item in input:

    if sum(list1) + sum(list2) <= item:
        list1.extend(list2)
        list2.clear()
        list2.append(item)
    elif sum(list1) > sum(list2):
      list2.append(item)
    else:
      list1.append(item)

  return abs(sum(list1) - sum(list2))


print(minAbsDif([1,2,3,4,5]))
print(minAbsDif([10,10,9,9,2]))
print(minAbsDif([]))
print(minAbsDif([1]))
