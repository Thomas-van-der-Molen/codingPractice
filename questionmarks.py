def questionMarks(string):
  string = list(string)
  seqs = []
  for x in range(len(string)):
    if string[x] >= '0' and string[x] <='9':
      newSeq = []
      newSeq.append(string[x])
      for y in range(x+1, len(string)):
        if y < len(string):
          newSeq.append(string[y])
          if string[y] >= '0' and string[y] <= '9':
            break
      seqs.append(newSeq)

  new = []
  for seq in seqs:
    if len(seq) > 1 and int(seq[0]) + int(seq[-1]) == 10:
      new.append(seq)
  if len(new) > 0:
    for seq in new:
      if seq.count('?') != 3:
        return False
  else:
    return False
  return True


def questionMarksTwo(string):
  qu = []
  string = list(string)
  for x in range(len(string)):
    if string[x] >= '0' and string[x] <= '9':
      qu.append(string[x])
      for y in range(x+1, len(string)):
        if y < len(string):
          if string[y] <= '9' and string[y] >= '0' and string[x] >='0' and string[x] <= '9':
            if int(string[y]) + int(string[x]) == 10 and qu.count('?') != 3: return False
            elif int(string[y]) + int(string[x]) == 10 and qu.count('?') == 3: break
        else:
          if qu[o] <= '9' and qu[o] >= '0' and qu[-1] >='0' and qu[-1] <= '9':
            if int(qu[0]) + int(qu[-1]) != 10 and qu.count('?') != 3: return False            
        qu.append(string[y])
        print(qu)
      qu.clear()
      x = y
  return True



string = "arrb6???4xxbl5???eee5"  #true
print(questionMarks(string))

string = "acc?7??sss?3rr1??????5"  #true
print(questionMarks(string))

string = "5??aaaaaaaaaaaaaaaaaaa?5?5" #false
print(questionMarks(string))

string = "9???1???9???1???9" #true
print(questionMarks(string))

string = "aa6?9" #false
print(questionMarks(string))

