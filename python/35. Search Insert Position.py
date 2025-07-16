# Approach 1 - Classic Binary Search
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1


        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
# Time Complexity: O(logn)
# Space Complexity: O(1)

# Approach 2 - Left / Right Boundaries
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)
       
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1 # target is in the right half
            else:
                r = mid # target could be mid or to the left
        return l
# Time Complexity: O(logn)
# Space Complexity: O(1)
