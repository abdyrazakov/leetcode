class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        def strsum(num):
            if num != 0:
                return str(num) + strsum(num-1)
            else:
                return ''
        def result(k):
            b = 1
            a = 1
            res = ''
            while n >= b :
                fac = factorial(n-b)
                if a*fac == k:
                    res += strsum(n-b)
                elif a*fac < k:
                    a += 1
                else:
                    res += str(a)
                    b += 1
                    a = 1
            return res
        return result(k)