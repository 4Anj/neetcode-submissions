class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        ro=defaultdict(set)
        bo=defaultdict(set)
        co=defaultdict(set)
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if (val in ro[r]) or (val in co[c]) or (val in bo[r//3,c//3]):
                    return False
                ro[r].add(val)
                co[c].add(val)
                bo[r//3,c//3].add(val)
        return True

