
class Solution(object):
    def hasGroupsSizeX(self, deck):
        from fractions import gcd
        from functools import reduce
        from collections import Counter
        
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2

if __name__ == "__main__":
    s = Solution()
    l0 = s.hasGroupsSizeX([1,1,1,2,2,2,3,3])
