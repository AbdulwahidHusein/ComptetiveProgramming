class Solution:
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][-1] = max(out[-1][-1], i[1])
                out[-1][0] = min(out[-1][0], i[0])
            else:
                out.append(i)
        return out

