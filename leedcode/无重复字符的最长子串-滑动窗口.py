class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_len = 1
        window = s[:1]
        for i in range(1, len(s)):
            if window.count(s[i]):
                window = window[window.index(s[i]) + 1:] + s[i]
            else:
                window = window + s[i]
            if len(window) > max_len:
                max_len = len(window)
        return max_len
