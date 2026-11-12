class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_set=[[set([]) for _ in range(3)] for _ in range(3)]
        sub=[[[] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            i_set=set([])
            j_set=set([])
            il=[]
            jl=[]
            for j in range(9):
                if board[i][j] != '.':
                    sub[int(i/3)][int(j/3)].append(board[i][j])
                    sub_set[int(i/3)][int(j/3)].add(board[i][j])
                    il.append(board[i][j])
                    i_set.add(board[i][j])
                    if len(il)!=len(i_set):
                        print(f'i{i} False')
                        return False
                if board[j][i] != '.':
                    jl.append(board[j][i])
                    j_set.add(board[j][i])
                    if len(jl)!=len(j_set):
                        print(f'j{i} False')
                        return False
        for i in range(3):
            for j in range(3):
                if len(sub[i][j])!=len(sub_set[i][j]):
                    print(f'sub[{i}][{j}] False')
                    return False
        else: return True
