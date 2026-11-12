class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_set=[[set([]) for _ in range(3)] for _ in range(3)]
        for i in range(9):
            i_set=set([])
            j_set=set([])
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in sub_set[i//3][j//3]:
                        return False
                    sub_set[i//3][j//3].add(board[i][j])
                    if board[i][j] in i_set:
                        return False
                    i_set.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in j_set:
                        return False
                    j_set.add(board[j][i])
        return True
