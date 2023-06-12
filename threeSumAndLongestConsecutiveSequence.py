
#thank you to neetcode for the solutions
#three sum

def threeSum(nums):
    nums.sort()#o of log n
    left, middle, right = -1,1,len(nums)-1
    res = []

    while left < right - 1:
        left +=1
        middle = left + 1
        right = len(nums)-1

        if left > 0 and nums[left] == nums[left-1]:
            continue
        else:
            while middle < right:
                mySum = nums[left] + nums[middle] + nums[right]
                if mySum == 0:
                    res.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    while middle < right and nums[middle] == nums[middle-1]:
                        middle += 1
                elif mySum < 0:
                    middle += 1
                else:
                    right -= 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
nums = [0,1,1]
print(threeSum(nums))
nums = [0,0,0]
print(threeSum(nums))



#longest consecutive sequence

def longestConsecutiveSequence(nums):
    mySet = set(nums)
    longest, current = 0, 0
    for num in nums:
        if num - 1 not in mySet:
            while num in mySet:
                current += 1
                num += 1
            longest = max(longest, current)
            current = 0
    return longest

nums = [100,4,200,1,3,2]
print(longestConsecutiveSequence(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutiveSequence(nums))