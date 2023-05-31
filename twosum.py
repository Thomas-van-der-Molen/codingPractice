

def twoSum(nums, target):
    nums.sort()
    negatives = [x for x in nums if x <= 0]
    positives = [x for x in nums if x > 0]
    print(negatives)
    print(positives)



nums, target = [2,7,11,15] , 9
print(twoSum(nums, target))

nums, target = [3,2,4], 6
print(twoSum(nums, target))

nums, target = [3,3], 6
print(twoSum(nums, target))

nums = [-123,-43,-659,-1,-2,-3,-4,-5-6,0,0,0,0,1,2,3,4,5,6,7,8,9,9,8,7,32456,4365,78,23,7,9]
target = -654
print(twoSum(nums, target))

target = 1
print(twoSum(nums, target))