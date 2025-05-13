class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l1 = []
        start = 0
        end = 1
        while start < len(s)-1 and end < len(s):

            if s[end] in s[start:end]:
                l1.append(len(s[start:end ]))
                start += 1

            else:

                end += 1
        l1.append(len(s[start:end]))
        return max(l1)