class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        answer = [row[:] for row in matrix]        
        max_value = [0] * n

        for i in range(m):
            for j in range(n):
                max_value[j] = max(max_value[j], matrix[i][j])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    answer[i][j] = max_value[j]
        return answer