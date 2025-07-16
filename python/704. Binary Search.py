# Approach 1 - Classic Binary Search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1


        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m +1
            else:
                r = m-1
        return -1
    
# Time Complexity: O(logn), because each step halves the search space
# Space Complexity: O(1)
