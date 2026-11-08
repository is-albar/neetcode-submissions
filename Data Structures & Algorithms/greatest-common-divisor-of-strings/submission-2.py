class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        if m < n:
            m, n = n, m
            str1, str2 = str2, str1

        for l in range(n, 0, -1):
            if m % l != 0 or n % l != 0:
                continue

            valid = True
            for i in range(m):
                if str1[i] != str2[i % l]:
                    valid = False
                    break
            if not valid: continue

            for i in range(l, n):
                if str2[i] != str2[i % l]:
                    valid = False
                    break
            if valid: return str2[:l]

        return ""