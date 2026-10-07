class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        visit = set(deadends)
        if "0000" in visit:
            return -1

        q = deque(["0000"])
        visit.add("0000")
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        nextLock = lock[:i] + digit + lock[i+1:]
                        if nextLock in visit:
                            continue
                        if nextLock == target:
                            return steps
                        q.append(nextLock)
                        visit.add(nextLock)
        return -1