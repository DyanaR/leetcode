class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # since sorted and needs O(log n), we should use binary search
        low = 0
        high = len(nums)-1

        while (low <= high):
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else: # target > nums[mid]
                low = mid + 1
        return low