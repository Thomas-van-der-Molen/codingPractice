def maximumTime(inputString):
  inputString = list(inputString)#array of characters in the input string
  if inputString[0] == '?' and inputString[1] == '?':
    inputString[0] = '2'
    inputString[1] = '3'
  elif inputString[0] == '?' and inputString[1] != '?' and int(inputString[1]) <=3:
    inputString[0] = '2'
  elif inputString[0] == '?':
    inputString[0] = '1'
  if int(inputString[0]) == 2 and inputString[1] == '?':
    inputString[1] = '3'
  elif int(inputString[0]) <= 1 and inputString[1] == '?':
    inputString[1] = '9'
  if inputString[3] == '?':
    inputString[3] = '5'
  if inputString[4] == '?':
    inputString[4] = '9'
  inputString = ''.join(inputString)
  return inputString

def maximumTime2(inputString):
  inputString = list(inputString)
  if inputString[0] == '?':
    inputString[0] = '2' if inputString[1] == '?' or inputString[1] <= '3' else '1'
  if inputString[1] == '?': inputString[1] = '3' if inputString[0] == '2' else '9'
  if inputString[3] == '?': inputString[3] = '5'
  if inputString[4] == '?': inputString[4]  = '9' 
  return ''.join(inputString)



print(maximumTime2("?4:5?"))
print(maximumTime2("23:5?"))
print(maximumTime2("2?:22"))
print(maximumTime2("0?:??"))
print(maximumTime2("??:??"))