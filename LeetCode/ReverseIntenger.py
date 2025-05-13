class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = str(x)
            if x[-1] != 0:
                k = int(x[::-1])
                return k if -(2 ** 31) <= k <= (2 ** 31) - 1 else 0
            else:
                x = x[:-1]
                k = int(x[::-1])
                return k if -(2 ** 31) <= k <= (2 ** 31) - 1 else 0
        elif x == 0:
            return 0
        else:
            x = str(x)
            x = x[1:]
            if x[-1] != 0:
                k = (int(x[::-1]))
                return k * (-1) if -(2 ** 31) <= k <= (2 ** 31) - 1 else 0
            else:
                x = x[:-1]
                k = (int(x[::-1]))
                return k * (-1) if -(2 ** 31) <= k <= (2 ** 31) - 1 else 0

