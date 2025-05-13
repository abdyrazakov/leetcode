class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(", "]":"[" , "}":"{" }
        open = 0
        l1 = []
        for c in s:
            l1.append(c)
        while open < len(l1)-1 :
            if l1[open+1] in valid and l1[open] == valid[l1[open+1]]:

                l1.pop(open+1)
                l1.pop(open)
                open = 0
            else:
                open += 1
        if not l1:
            return True
        else:
            return False