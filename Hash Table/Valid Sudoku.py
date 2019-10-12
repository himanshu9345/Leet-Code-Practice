class Solution(object):
    def isValidSudoku(self, board):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        for i in range(9):
            dict1[i] = set()
        for i in range(9):
            dict2[i] = set()
        for i in range(9):
            dict3[i] = set()
        count = 0
        for i in range(9):
            for j in range(9):
                # print i,j
                if board[i][j] != ".":
                    count = 3 * (i / 3) + j / 3
                    # print count
                    num = board[i][j]
                    if board[i][j] in dict1[count]:
                        # print dict1[count]
                        return False
                    else:
                        dict1[count].add(board[i][j])
                    # print dict1[count],num

                    if num in dict2[i]:
                        # print(dict2[i])
                        return False
                    else:
                        dict2[i].add(num)
                    if num in dict3[j]:
                        return False
                    else:
                        dict3[j].add(num)
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
