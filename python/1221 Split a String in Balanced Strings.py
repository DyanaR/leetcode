class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0 
        match = 0
        for x in s:
            if x == 'R':
                count += 1
            if x == 'L':
                count -= 1
            if count == 0:
                match += 1
        return match
