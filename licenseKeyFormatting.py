#my intuitive approach, terrible and took too long to come up with
def licenseKeyFormatTwo(s, k):
  s = list(s)
  while '-' in s: s.remove('-')
  secondList = []
  charsAppended = 1
  for x in range(len(s)):
    secondList.append(s.pop().upper())
    if charsAppended == k and s:
      secondList.append('-')
      charsAppended = 0
    charsAppended += 1
  secondList = secondList[::-1]
  return ''.join(secondList)

#instead create a number of sub groups determined by len(s)/k and join them at the end
#stolen from leetcode
def licenseKeyFormat(s, k):
    s = s.replace('-','').upper()
    start = len(s) % k
    res = []

    if start:
        res.append(s[:start])
        #something

    for x in range(start, len(s), k):
        res.append(s[x:x+k])

    return "-".join(res)


s, k = "5F3Z-2e-9-w", 4
print(licenseKeyFormat(s,k))

s, k = "2-5g-3-J", 2
print(licenseKeyFormat(s,k))