class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            tg = target
            n = tg - nums[i]
            nums[i] = None
            if nums.count(n):
                j = nums.index(n)
                if j:
                    return [i, j]
