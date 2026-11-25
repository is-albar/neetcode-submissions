class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        for mask in range(1 << n):
            comb = []
            for bit in range(n):
                if mask & (1 << bit):
                    comb.append(bit + 1)

            if len(comb) == k:
                res.append(comb)
        return res