class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col_l = 0
        col_r = len(matrix[0])
        row_t = 0
        row_b = len(matrix)
        result = []
        while col_l < col_r and row_t < row_b:
            # traverse right
            for i in range(col_l, col_r):
                result.append(matrix[row_t][i])
            row_t += 1
            
            #traverse bottom
            for j in range(row_t, row_b):
                result.append(matrix[j][col_r-1])
            col_r -= 1
            
            #traverse left
            if row_t < row_b:
                for k in range(col_r-1, col_l-1, -1):
                    result.append(matrix[row_b-1][k])
                row_b -= 1
            
            # traverse top
            if col_l < col_r:
                for l in range(row_b-1, row_t-1, -1):
                    result.append(matrix[l][col_l])
                col_l += 1
        return result