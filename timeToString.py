
def timeToString(strInput, strLayout):
  strInput = list(strInput)
  strLayout = list(strLayout)
  sum = 0
  prev = 0
  for character in strInput:
    sum += abs(prev - strLayout.index(character))
    prev = strLayout.index(character)
  return sum


def timeToStringTwo(strInput, strLayout):
  strInput = list(strInput)
  strLayout = list(strLayout)
  sum = 0
  prev = 0
  for character in strInput:
    index = strLayout.index(character)
    sum += abs(prev - index)
    prev = index
  return sum


def timeToStringThree(strInput, strLayout):
  strInput = list(strInput)
  strLayout = list(strLayout)
  sum = 0
  prev = 0
  charMap = {}
  for x in range(26):
    charMap[strLayout[x]] = x
  for character in strInput:
    sum+=abs(prev - charMap[character])
    prev = charMap[character]
  return sum


def timeToStringFour(strInput, strLayout):
  strInput = list(strInput)
  strLayout = list(strLayout)
  sum = 0
  prev = 0
  charMap = {char : index for index, char in enumerate(strLayout)}
  for char in strInput:
    sum += abs(prev - charMap[char])
    prev = charMap[char]
  return sum


layout = "abcdefghijklmnopqrstuvwxyz"
text = "cba"

print(timeToString(text, layout))
print(timeToStringTwo(text, layout))
print(timeToStringThree(text, layout))
print(timeToStringFour(text, layout))


layout = "qazwsxedcrfvtgbyhnujmikolp"
text = "cba"

print(timeToString(text, layout))
print(timeToStringTwo(text, layout))
print(timeToStringThree(text, layout))
print(timeToStringFour(text, layout))



#