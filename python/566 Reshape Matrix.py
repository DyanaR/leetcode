class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        total_elements = len(mat) * len(mat[0])
        
        if total_elements != r * c:
            return mat

        temp = []
        result = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # flatten matrix
                temp.append(mat[i][j])
        k = 0
        for i in range(r):
            for j in range(c):
                result[i][j] = temp[k]
                k += 1
        return result
