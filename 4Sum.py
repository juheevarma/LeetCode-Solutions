class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                p1 = j+1
                l = len(nums)-1
                total = 0
                while p1 < l:
                    total = nums[i]+nums[j]+nums[p1]+nums[l]                
                    if total > target:
                        l -= 1
                    elif total < target:
                        p1 += 1
                    else:
                        result.append([nums[i],nums[j],nums[p1],nums[l]])
                        val = nums[p1]
                        while p1 < l and nums[p1] == val:
                            p1 += 1
                        val = nums[l]
                        while p1 < l and nums[l] == val:
                            l -= 1
        return result
