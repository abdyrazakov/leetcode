from operator import index


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        resin = []
        work = ""
        start = 0
        end = 0
        while start < len(s):
            work += s[end]
            end += 1
            if work == work[::-1]:
                res.append(work)
                resin.append(len(work))
            if end >= len(s):
                start += 1
                end = start
                work = ""

        return res[resin.index(max(resin))]