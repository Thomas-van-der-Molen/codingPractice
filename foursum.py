class Solution:
    def fourSum(self, nums, target):
        if len(nums) == 4 and sum(nums) == target: return [nums] 
        elif len(nums) < 4: return []
        nums.sort()
        res = []
        a = 0
        b = a+1
        d = len(nums)-1
        c = d-1
        while d - a >= 3:
            anew = a
            b = a+1
            c = d-1
            dnew = d
            while c > b:
                temp = [nums[anew], nums[b], nums[c], nums[dnew]]
                if sum(temp) == target and temp not in res:
                    res.append(temp)
                if sum(temp) <= target:
                    b+=1
                else:
                    c-=1
                if sum(temp) == target:
                    anew+=1
                    dnew-=1
            a+=1
            d-=1
        return res
    

if __name__ == "__main__":
    sol = Solution()

    nums, target = [1,0,-1,0,-2,2], 0
    print(sol.fourSum(nums,target))

    nums, target = [2,2,2,2,2], 8
    print(sol.fourSum(nums,target))

    nums, target = [1], 10
    print(sol.fourSum(nums,target))

    nums, target = [1,2,3,4], 10
    print(sol.fourSum(nums,target))

    nums, target = [-3,-1,0,2,4,5], 0
    print(sol.fourSum(nums,target))

    nums, target = [-3,-1,0,2,4,5], 2
    print(sol.fourSum(nums,target))

