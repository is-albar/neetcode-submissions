class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> [value, frequency, timestamp]
        self.timestamp = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache[key][1] += 1
        self.timestamp += 1
        self.cache[key][2] = self.timestamp
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        self.timestamp += 1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.timestamp
            return

        if len(self.cache) >= self.capacity:
            min_freq = float('inf')
            min_timestamp = float('inf')
            lfu_key = None

            for k, (_, freq, ts) in self.cache.items():
                if freq < min_freq or (freq == min_freq and ts < min_timestamp):
                    min_freq = freq
                    min_timestamp = ts
                    lfu_key = k
            if lfu_key is not None:
                del self.cache[lfu_key]

        self.cache[key] = [value, 1, self.timestamp]