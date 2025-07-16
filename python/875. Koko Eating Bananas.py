# Approach 1 - Brute Force
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while k <= max(piles):
            count = 0
            for p in piles:
                count += math.ceil(p/k)
            if count <= h:
                return k
            else:
                k += 1
# Time Complexity: O(max(piles) * n) 
# Space Complexity: O(1)


# Approach 2 - Binary Search on Answer
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r


        while l <= r:
            k = (l+r) // 2
            hours = 0 # count
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                r = k -1
            else:
                l = k + 1
        return res
# Time Complexity: O(log(max(piles)) * n) 
# Space Complexity: O(1)
