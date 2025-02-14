class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

X = Solution()
print(X.removeElement([2,3,3,2],2))
print(X.removeElement([0,1,2,3,0,4,3,2],3))