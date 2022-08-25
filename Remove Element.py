class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for n in range(len(nums)):
            if val != nums[n]:
                nums[index] = nums[n]
                index += 1
        return index
