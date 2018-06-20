#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-28 14:19
#!@Author : LYC
#!@File : Leecode_isValidSudoku_function1_.PY
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(len(board)):
            for j in range(len(board)):
                nums = board[i][j]
                if nums == ".":
                    continue
                if nums not  in dic_row[i] and nums not  in dic_col[j] and nums not  in dic_box[3*(i//3)+(j//3)]:
                    dic_row[i][nums] = 1
                    dic_col[j][nums] = 1
                    dic_box[3 * (i // 3) + (j // 3)][nums] = 1
                else:
                    return False
        return True,dic_row,dic_col,dic_box,
if __name__ == '__main__':
    isn = Solution()
    board =[["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    print(isn.isValidSudoku(board))
    print(3*(0//3)+4//3)