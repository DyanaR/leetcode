class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force O(n^2)
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]: 
        #             return True
        # return False

        # O(n)
        set_nums = set(nums) # O(n)
        if len(set_nums) != len(nums): # O(1)
            return True
        else:
            return False
