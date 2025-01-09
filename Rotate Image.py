#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
#8:31

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        #Output: [[7,4,1],[8,5,2],[9,6,3]]
        N = len(matrix)
        
        new_matrix = []
        for col in range(N):
            new_row = []
            for row in range(N-1,-1,-1):
                new_row.append(matrix[row][col])
            new_matrix.append(new_row)
        #copy to old matrix
        for i in range(N):
            for j in range(N):
                matrix[i][j] = new_matrix[i][j]