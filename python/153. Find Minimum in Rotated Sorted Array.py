# Approach 1 - Brute Force 
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')


        for num in nums:
            mini = min(mini, num)
        return mini
# Time Complexity: O(n), checks every element
# Space Complexity: O(1)

# Approach 2 - Rotated Sorted Array & Lower Boundary
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]: # left side sorted, pivot in right side
                l = mid + 1
            else: # pivot in left side
                r = mid
        return nums[l]
# Time Complexity: O(logn)
# Space Complexity: O(1)