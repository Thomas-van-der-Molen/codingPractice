
#buy two chocolates
def buyChoco(prices, money):
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        else:
            return money

#maximum strength of a group

def maxStrength(nums):
    if max(nums) <= 0: return max(nums)
    strength = 1
    nums.sort()
    for index, value in enumerate(nums):
        if value < 0 and index < len(nums) -1 and nums[index + 1] < 0:
            strength *= 
        elif value > 0:
            strength *= value
    return strength

nums = [3,-1,-5,2,5,-9]
print(maxStrength(nums))

nums = [-4,-5,-4]
print(maxStrength(nums))