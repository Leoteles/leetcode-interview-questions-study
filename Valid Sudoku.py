# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
#28:30

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        I = len(board)
        J = len(board[0])
        
        def valid_line(line):
            line = [i for i in line if i !='.']
            if len(set(line)) == len(line):
                return True
            else:
                return False
        #row
        print('row')
        for row in board:
            if not valid_line(row):
                return False
        #col
        print('col')
        for j in range(J):
            col = [board[i][j] for i in range(I)]
            if not valid_line(col):
                return False
        #box
        print('box')
        for bi in range(0,I,3):
            for bj in range(0,J,3):
                box = board[bi][bj:bj+3] + board[bi+1][bj:bj+3] + board[bi+2][bj:bj+3]
                if not valid_line(box):
                    return False
                
        return True