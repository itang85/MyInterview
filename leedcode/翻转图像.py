class Solution:
    def flipAndInvertImage(self, A):
        result = []
        for line in A:
            result.append([1 - (1 * num) for num in line[::-1]])
        return result
