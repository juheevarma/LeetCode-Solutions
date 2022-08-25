class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result  = [-1, -1] 
        def binarySearch(start, end):
            if start > end:
                return
            mid = start + (end - start)//2  
            if target == nums[mid]:
                if result[0] == -1 or result[0] > mid:
                    result[0] = mid
                if result[1] == -1 or result[1] < mid: 
                    result[1] = mid
            binarySearch(start, mid - 1)
            binarySearch(mid + 1, end)
        binarySearch(0, len(nums)-1)
        return result
