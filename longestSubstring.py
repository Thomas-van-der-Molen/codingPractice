

def lengthOfLongestSubstring(s):
        longest = []
        cur = []
        s = list(s)
        if not s: return 0
        elif all(x == ' ' for x in s): return 1
        else: longest = s[0]

        for x in s:
            if x not in cur:
                cur.append(x)
            else:
                if len(cur) > len(longest):
                    longest = cur.copy()#pass by reference!!
                cur.clear()
                cur.append(x)
        return len(longest)



string = "abcabcbb"
print(lengthOfLongestSubstring(string))

string = "bbbbb"
print(lengthOfLongestSubstring(string))

string = "pwwkew"
print(lengthOfLongestSubstring(string))

string = " "
print(lengthOfLongestSubstring(string))

string = ""
print(lengthOfLongestSubstring(string))

string = "      "
print(lengthOfLongestSubstring(string))

string = "c"
print(lengthOfLongestSubstring(string))
