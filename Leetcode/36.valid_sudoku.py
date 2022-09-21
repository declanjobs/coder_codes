from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        h = [set() for _ in range(9)]
        v = [set() for _ in range(9)]
        c = [set() for _ in range(9)]

        def which_cube(i,j):

            i = i // 3
            j = j // 3

            #print(i,j, i*3 + j)
            return i*3 + j

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in h[i] or \
                    board[i][j] in v[j] or \
                    board[i][j] in c[which_cube(i,j)]:

                    return False

                h[i].add(board[i][j])
                v[j].add(board[i][j])
                c[which_cube(i,j)].add(board[i][j])

        return True