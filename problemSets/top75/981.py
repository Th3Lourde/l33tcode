class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        if key in self.d:
            self.d[key].append((timestamp, value))

        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key, timestamp):
        if key not in self.d:
            return ""

        vals = self.d[key]
        l = 0
        r = len(vals)-1

        if vals[0][0] > timestamp:
            return ""

        while l < r:
            m = (l+r)//2

            if vals[m][0] >= timestamp:
                r = m
            else:
                l = m+1

        if vals[l][0] > timestamp:
            return vals[l-1][1]

        return vals[l][1]

tm = TimeMap()

tm.set("love", "high", 10)
tm.set("love", "low", 20)
tm.get("love", 5)
tm.get("love", 10)
tm.get("love", 15)
tm.get("love", 20)
tm.get("love", 25)


tm.d
