class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        result = []
        rows, cols = len(mat), len(mat[0])
        r, c = 0, 0
        direction = 1 # 1 for arrow up right, -1 for arrow down left

        while len(result) < rows * cols:
            result.append(mat[r][c])
            
            if direction == 1: 
                if c == cols - 1: # Hit right boundary
                    r +=1  # move down
                    direction = -1 # switch to next direction
                elif r == 0: # Hit top boundary
                    c += 1 # move right
                    direction = -1 # switch to next direction
                else: # no boundary, keep moving in regular direction
                    r -= 1 # up
                    c += 1 # right
            
            else: # moving down left
                if r == rows - 1: # hit bottom boundary
                    c += 1 # move right
                    direction = 1
                elif c == 0: # hit left boundary
                    r += 1 # move down
                    direction = 1
                else:
                    r += 1
                    c -= 1
        return result
                    
