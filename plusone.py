class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        q = 0
        q, digits[0]  = divmod(digits[0] + 1, 10)
        for x in range(1,len(digits)):
            q, digits[x] = divmod(digits[x]+q, 10)
        if q != 0:
            digits.append(q)
        return digits[::-1]