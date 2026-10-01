class Solution:
    def totalNQueens(self, n: int) -> int:
        col = 0
        posDiag = 0
        negDiag = 0
        res = 0

        def backtrack(r):
            nonlocal col, posDiag, negDiag, res
            if r == n:
                res += 1
                return
            for c in range(n):
                if ((col & (1 << c)) or (posDiag & (1 << (r + c)))
                    or (negDiag & (1 << (r - c + n)))):
                    continue
                col ^= (1 << c)
                posDiag ^= (1 << (r + c))
                negDiag ^= (1 << (r - c + n))

                backtrack(r + 1)

                col ^= (1 << c)
                posDiag ^= (1 << (r + c))
                negDiag ^= (1 << (r - c + n))

        backtrack(0)
        return res