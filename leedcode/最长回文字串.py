class Solution:
    def longestPalindrome(self, s):
        begin = 0
        end = 0
        for i in range(0, len(s) - 1):

            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)

            if right1 - left1 > end - begin:
                begin, end = left1, right1
            if right2 - left2 > end - begin:
                begin, end = left2, right2

        return s[begin: end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s):

            if s[left] == s[right]:
                left = left - 1
                right = right + 1
            else:
                break
        return left + 1, right - 1

solu = Solution()
solu.longestPalindrome('bb')
