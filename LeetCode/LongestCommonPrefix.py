class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""


        for i in range(len(strs[0])) :
            for j in range(len(strs)) :
                if i >= len(strs[j]) :
                    return prefix
                elif strs[j][i] == strs[0][i] :
                    continue
                else:
                    return prefix
            prefix += strs[0][i]
        return prefix