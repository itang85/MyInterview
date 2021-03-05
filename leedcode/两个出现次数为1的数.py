import functools


class Solution:
    def singleNumbers(self, nums):
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
            print(div)
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


solu = Solution()
print(solu.singleNumbers([1,2,10,4,1,4,3,3]))
