class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        mid = (len(nums1) + len(nums2)) / 2

        if mid % 1 == 0:
            mid1 = int(mid - 1)
            mid2 = int(mid)
        else:
            mid1 = mid2 = int(mid)
        index1 = 0
        index2 = 0
        a_sum = 0
        current = None
        for i in range(len(nums1) + len(nums2)):
            if not nums2 or index2 == len(nums2):
                current = nums1[index1]
                index1 += 1
            elif not nums1 or index1 == len(nums1):
                current = nums2[index2]
                index2 += 1
            elif nums1[index1] <= nums2[index2]:
                current = nums1[index1]
                index1 += 1
            else:
                current = nums2[index2]
                index2 += 1
            # print('`'*10)
            # print(mid1, mid2)
            # print(index1, index2)
            # print(current)
            # print('`'*10)
            if i == mid1:
                a_sum += current
            if i == mid2:
                a_sum += current
                break
        return a_sum / 2


solu =Solution()
print(solu.findMedianSortedArrays([1,2], [3,4]))


class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

