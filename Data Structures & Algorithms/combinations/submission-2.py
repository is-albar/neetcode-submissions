class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        i = 0
        comb = [0] * k

        while i >= 0:
            comb[i] += 1
            if comb[i] > n:
                i -= 1
                continue

            if i == k - 1:
                res.append(comb.copy())
            else:
                i += 1
                comb[i] = comb[i - 1]

        return res