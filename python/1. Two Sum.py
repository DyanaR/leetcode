# BRUTE FORCE
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] 
        return {}
        
# OPTIMIZED SOLUTION
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in mp:
                return[mp[complement], i]
            
            mp[nums[i]] = i

        return []



