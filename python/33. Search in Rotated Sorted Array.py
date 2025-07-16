# Approach 1 - Rotated Sorted Array Technique 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]: # left sorted
                if nums[l] <= target <= nums[mid]: # check if in sorted side
                    r = mid - 1
                else: # if not, its in pivot side
                    l = mid+1
            else: # right sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1  
# Time Complexity: O(logn)
# Space Complexity: O(1)

