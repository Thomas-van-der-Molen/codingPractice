def compressionDecompression(strInput):
  strInput = list(strInput)
  myStack = []
  for x in range(len(strInput)):
    if strInput[x] >= '0' and strInput[x] <= '9':
      myStack.append(strInput[x])
    else:
      if myStack:
        num = "".join(myStack)
        num = int(num)
        myStack.clear()
        for y in range(num):
            compressionDecompression(''.join(strInput[x:]))
      filter(lambda chara: chara !='[]', strInput)
      print(''.join(strInput),end="")



#compressionDecompression("")
compressionDecompression("10[a]")
print()

compressionDecompression("abc")
print()

compressionDecompression("2[3[a]b]")
print()