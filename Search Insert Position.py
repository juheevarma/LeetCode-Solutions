class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ans = 0
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            ans = l
        return ans
