


def validAnagramTwo(s, t):
  if len(s) != len(t): return False
  letters = {}
  for letterS, letterT in zip(s,t):
    if letterS not in letters:
      letters[letterS] = 1
    else:
      letters[letterS] += 1
    if letterT not in letters:
      letters[letterT] = -1
    else:
      letters[letterT] -= 1
  return all(letters[letter] == 0 for letter in letters)

def validAnagram(s, t):
  import collections
  if len(s) != len(t): return False
  seen = collections.defaultdict(int)
  for x in s: seen[x] += 1
  for x in t: seen[x] -= 1
  return all(value == 0 for value in seen.values())

print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "car"))