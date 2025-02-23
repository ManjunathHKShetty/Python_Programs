class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

X = Solution()
result_1 = X.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(result_1)
