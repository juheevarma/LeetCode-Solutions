class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans
